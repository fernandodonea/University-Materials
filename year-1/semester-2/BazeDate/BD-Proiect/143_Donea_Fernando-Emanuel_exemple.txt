
--------------------------- ex 12--------------------------------


--------------------------- Cererea 1--------------------------------

---Care sunt utilizatorii care au comandat albumele personalizate care includ
-- melodii din cele mai multe albume diferite.

WITH albume_per_cd AS (
    SELECT cp.cd_pers_id, cp.utilizator_id, cp.titlu AS titlu_cd,
           COUNT(DISTINCT m.album_id) AS numar_albume_diferite
    FROM cd_personalizat cp
    JOIN playlist p ON cp.cd_pers_id = p.cd_pers_id
    JOIN melodie m ON p.melodie_id = m.melodie_id
    GROUP BY cp.cd_pers_id, cp.utilizator_id, cp.titlu
),
max_albume AS (
    SELECT MAX(numar_albume_diferite) AS max_albume_diferite
    FROM albume_per_cd
)
SELECT u.utilizator_id, u.nume, u.prenume,
       apc.cd_pers_id, apc.titlu_cd, apc.numar_albume_diferite,
       (SELECT COUNT(DISTINCT album_id)
        FROM melodie m
        JOIN playlist p ON m.melodie_id = p.melodie_id
        WHERE p.cd_pers_id = apc.cd_pers_id) AS total_albume
FROM utilizator u
JOIN albume_per_cd apc ON u.utilizator_id = apc.utilizator_id
JOIN max_albume ma ON apc.numar_albume_diferite = ma.max_albume_diferite
ORDER BY u.nume, u.prenume;



--------------------------- Cererea 2--------------------------------

--Pentru fiecare gen muzical să se afișeze numărul de albume comandate
--și numărul de albume incluse în playlisturi.


SELECT gm.gen_id, gm.denumire,
       NVL(albume_comandate.nr_albume, 0) AS numar_albume_comandate,
       NVL(albume_playlist.nr_albume, 0) AS numar_albume_playlist,
       DECODE(
           SIGN(NVL(albume_comandate.nr_albume, 0) - NVL(albume_playlist.nr_albume, 0)),
           1, 'Mai popular în comenzi',
           0, 'Popularitate egală',
          -1, 'Mai popular în playlisturi'
       ) AS comparatie_popularitate
FROM gen_muzical gm
LEFT JOIN (
    SELECT agm.gen_id, COUNT(DISTINCT ca.album_id) AS nr_albume
    FROM album_gen_muzical agm
    JOIN comanda_albume ca ON agm.album_id = ca.album_id
    GROUP BY agm.gen_id
) albume_comandate ON gm.gen_id = albume_comandate.gen_id
LEFT JOIN (
    SELECT agm.gen_id, COUNT(DISTINCT m.album_id) AS nr_albume
    FROM album_gen_muzical agm
    JOIN album a ON agm.album_id = a.album_id
    JOIN melodie m ON a.album_id = m.album_id
    JOIN playlist p ON m.melodie_id = p.melodie_id
    GROUP BY agm.gen_id
) albume_playlist ON gm.gen_id = albume_playlist.gen_id
ORDER BY numar_albume_comandate + numar_albume_playlist DESC;



--------------------------- Cererea 3--------------------------------

--Afișarea artiștilor care au albume cu rating-ul mediu mai mare decât media rating-urilor tuturor albumelor,
--alături de numărul de albume și numărul de utilizatori care au albume ale artistului în wishlist.

SELECT a.artist_id, a.nume,
       NVL(COUNT(DISTINCT alb.album_id), 0) AS numar_albume,
       AVG(alb.rating) AS rating_mediu,
       DECODE(COUNT(DISTINCT wa.wishlist_id), 0, 'Niciun wishlist',
              TO_CHAR(COUNT(DISTINCT wa.wishlist_id))) AS numar_wishlist
FROM artist a
LEFT JOIN album alb ON a.artist_id = alb.artist_id
LEFT JOIN (SELECT wa.album_id, w.wishlist_id
           FROM wishlist_album wa
           JOIN wishlist w ON wa.wishlist_id = w.wishlist_id) wa
     ON alb.album_id = wa.album_id
GROUP BY a.artist_id, a.nume
HAVING AVG(alb.rating) > (SELECT AVG(rating) FROM album)
ORDER BY rating_mediu DESC, numar_wishlist DESC;



--------------------------- Cererea 4--------------------------------

--Afișarea informațiilor despre comenzi cu detalii despre status, vechime,
-- timpul trecut de la plasare și valoarea totală,
-- analizând cât reprezintă costul transportului din total.


SELECT c.comanda_id,
       UPPER(u.nume) || ' ' || INITCAP(u.prenume) AS client,
       TO_CHAR(c.data_plasare, 'DD-MON-YYYY') AS data_plasare,
       ROUND(MONTHS_BETWEEN(SYSDATE, c.data_plasare), 1) AS vechime_luni,
       CASE
           WHEN MONTHS_BETWEEN(SYSDATE, c.data_plasare) < 1 THEN 'Comandă recentă'
           WHEN MONTHS_BETWEEN(SYSDATE, c.data_plasare) < 6 THEN 'Comandă din ultimele 6 luni'
           WHEN MONTHS_BETWEEN(SYSDATE, c.data_plasare) < 12 THEN 'Comandă din ultimul an'
           ELSE 'Comandă veche'
       END AS vechime,
       c.status,
       c.cost_total,
       c.cost_transport,
       ROUND((c.cost_transport / c.cost_total) * 100, 2) || '%' AS procent_transport,
       TO_CHAR(ADD_MONTHS(c.data_plasare, 12), 'DD-MON-YYYY') AS data_limita_garantie
FROM comanda c
JOIN utilizator u ON c.utilizator_id = u.UTILIZATOR_ID
ORDER BY c.data_plasare DESC;



--------------------------- Cererea 5--------------------------------

--Afișarea artiștilor și a evenimentelor lor viitoare,cu numărul total de albume, rating mediu
-- și numărul de fani (utilizatori cu albume ale artistului în wishlist).

WITH artisti_populari AS (
    SELECT a.artist_id, a.nume, COUNT(DISTINCT alb.album_id) AS nr_albume,
           AVG(alb.rating) AS rating_mediu
    FROM artist a
    JOIN album alb ON a.artist_id = alb.artist_id
    GROUP BY a.artist_id, a.nume
),
fani_artist AS (
    SELECT a.artist_id, COUNT(DISTINCT w.utilizator_id) AS nr_fani
    FROM artist a
    JOIN album alb ON a.artist_id = alb.artist_id
    JOIN wishlist_album wa ON alb.album_id = wa.album_id
    JOIN wishlist w ON wa.wishlist_id = w.wishlist_id
    GROUP BY a.artist_id
)
SELECT ap.artist_id, ap.nume, ap.nr_albume, ap.rating_mediu,
       NVL(fa.nr_fani, 0) AS numar_fani,
       e.eveniment_id, e.nume AS nume_eveniment, e.data, e.locatie, e.capacitate
FROM artisti_populari ap
LEFT JOIN fani_artist fa ON ap.artist_id = fa.artist_id
JOIN lineup l ON ap.artist_id = l.artist_id
JOIN eveniment e ON l.eveniment_id = e.eveniment_id
ORDER BY e.data, ap.rating_mediu DESC;















--------------------------- ex 13--------------------------------

--------------------------- Operatia 1--------------------------------

--Actualizarea rating-ului albumelor pe baza mediei recenziilor

--Descriere: Actualizarea rating-ului pentru toate albumele pentru a reflecta
-- media rating-urilor din recenziile utilizatorilor.


UPDATE album a
SET rating = (
    SELECT AVG(r.rating)
    FROM recenzie r
    WHERE r.album_id = a.album_id
    GROUP BY r.album_id
)
WHERE EXISTS (
    SELECT 1
    FROM recenzie r
    WHERE r.album_id = a.album_id
);



--------------------------- Operatia 2--------------------------------

--Actualizarea nivelului de loialitate pentru utilizatori

--Descriere: Actualizarea nivelului de loialitate pentru utilizatori
-- în funcție de numărul total de comenzi plasate și valoarea acestora.


UPDATE loialitate l
SET nivel = (
    CASE
        WHEN (SELECT COUNT(*) FROM comanda c WHERE c.utilizator_id = l.utilizator_id) >= 5
             OR (SELECT SUM(cost_total) FROM comanda c WHERE c.utilizator_id = l.utilizator_id) > 500
        THEN 'Platină'
        WHEN (SELECT COUNT(*) FROM comanda c WHERE c.utilizator_id = l.utilizator_id) >= 3
             OR (SELECT SUM(cost_total) FROM comanda c WHERE c.utilizator_id = l.utilizator_id) > 300
        THEN 'Aur'
        WHEN (SELECT COUNT(*) FROM comanda c WHERE c.utilizator_id = l.utilizator_id) >= 2
             OR (SELECT SUM(cost_total) FROM comanda c WHERE c.utilizator_id = l.utilizator_id) > 150
        THEN 'Argint'
        ELSE 'Bronz'
    END
)
WHERE EXISTS (
    SELECT 1 FROM comanda c WHERE c.utilizator_id = l.utilizator_id
);



--------------------------- Operatia 3--------------------------------

-- Ștergerea melodiilor din CD-urile personalizate pentru care durata totală depășește un anumit prag

-- Descriere: Ștergerea melodiilor care au cea mai mică durată din CD-urile personalizate pentru care durata totală a
-- melodiilor depășește 60 de minute (3600 secunde).

DELETE FROM playlist p
WHERE p.melodie_id IN (
    SELECT m.melodie_id
    FROM playlist p2
    JOIN melodie m ON p2.melodie_id = m.melodie_id
    WHERE p2.cd_pers_id = p.cd_pers_id
    AND m.durata = (
        SELECT MIN(m2.durata)
        FROM playlist p3
        JOIN melodie m2 ON p3.melodie_id = m2.melodie_id
        WHERE p3.cd_pers_id = p.cd_pers_id
    )
)
AND p.cd_pers_id IN (
    SELECT cd.cd_pers_id
    FROM cd_personalizat cd
    WHERE (
        SELECT SUM(m3.durata)
        FROM playlist p4
        JOIN melodie m3 ON p4.melodie_id = m3.melodie_id
        WHERE p4.cd_pers_id = cd.cd_pers_id
    ) > 3600
)
AND ROWNUM = 1;

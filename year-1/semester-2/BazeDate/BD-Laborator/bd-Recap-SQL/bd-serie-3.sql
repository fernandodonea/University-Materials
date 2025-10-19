-------RECAP SQL------------
----BD SERIE 3 exercitii----


--ex 1
SELECT
    C.NUME AS "NUME",
    COALESCE(SUM(CT.PRET),0)
FROM CITITORI C
JOIN CUMPARAT CUMP ON C.ID_CITITOR=CUMP.ID_CITITOR
JOIN CARTI CT ON CUMP.ID_CARTE=CT.ID_CARTE
WHERE TO_CHAR(CUMP.DATA,'YYYY')='2025'
GROUP BY C.NUME;


--ex 2
select c.nume
from CITITORI c
join CUMPARAT cump on c.id_cititor = cump.id_cititor
join CARTI ct on cump.id_carte = ct.id_carte
join AUTORI a on ct.id_autor = a.id_autor
where extract(year from c.data_nastere) between 1990 and 1999
group by c.id_cititor, c.nume
having count(distinct a.id_autor) >= 2;


--ex 3
with lib_hum as (
    SELECT
        COUNT(CT.CARTE_ID) AS "N"
    FROM LIBRARIE L
    JOIN CUMPARAT CUMP ON CUMP.ID_LIBRARIE=L.ID_LIBRARIE
    JOIN CARTI CT ON CUMP.ID_CARTE=CT.ID_CARTE
    WHERE L.NUME='HUMANITAS'
)
SELECT
    T."nume",
    T."rating",
    ROWNUM
FROM (
    SELECT
    CT.NUME "nume",
    AVG(O.RATING) "rating"
    FROM CARTI CT
    JOIN OPINIE O ON CT.ID_CARTE=O.ID_CARTE
    GROUP BY CT.NUME
    ORDER BY AVG(O.RATING)
     )T
where ROWNUM < (
    select n from lib_hum
    )





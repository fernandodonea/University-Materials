

---sgbd tema 1
-- Donea Fernando-Emanuel
-- grupa 243

---ex a)

SET ECHO OFF
SET FEEDBACK OFF

SPOOL sterge_tabele.sql

------stergere tabele asociative

SELECT 'DROP TABLE ' || table_name || 'CASCADE CONSTRAINTS;'
FROM user_tables
WHERE table_name in ('PLAYLIST','LINEUP','COMANDA_CD_PERSONALIZAT','COMANDA_ALBUME',
                     'WISHLIST_ALBUM','ALBUM_GEN_MUZICAL');

----stergere tabele cu chei straine
SELECT 'DROP TABLE ' || table_name || 'CASCADE CONSTRAINTS;'
FROM user_tables
WHERE table_name in ('BILET','RECENZIE','LOIALITATE','WISHLIST','CD_PERSONALIZAT',
                     'COMANDA','MELODIE','ALBUM');

------ stergere tabele principale


SELECT 'DROP TABLE ' || table_name || 'CASCADE CONSTRAINTS;'
FROM user_tables
WHERE table_name IN ('EVENIMENT','GEN_MUZICAL','ARTIST','UTILIZATOR');


SPOOL OFF
SET ECHO ON



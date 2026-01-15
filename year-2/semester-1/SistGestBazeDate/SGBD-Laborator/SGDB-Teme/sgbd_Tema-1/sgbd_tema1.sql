--SGBD Tema 1

-- E1. Identificați diagrama conceptuală definită în proiectul prezentat la materia Baze de Date din anul I. Dacă
-- nu aveți o astfel de diagramă, atunci definiți un model simplificat pentru acest exercițiu.
    -- a. adăugați ca poză diagrama conceptuală identificată;
    -- b. adaptați cerințele exercițiilor 17 și 23 pentru diagrama conceptuală utilizată la punctul a (formulați
    -- cerința în limbaj natural, apoi rezolvați cererea propusă în SQL).






---------------------------- REZOLVARE----------------------------

---cerinta 17
--Generaţi automat un script SQL care să conţină comenzi de ştergere a tuturor tabelelor personale create.
-- Indicaţie: Folosiţi comenzile SPOOL …/sterg_tabele.sql şi SPOOL OFF.

SET ECHO OFF;
SET FEEDBACK OFF;


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


SPOOL OFF;
SET ECHO ON;





---cerinta 23
-- Folosind tabelul departments generaţi automat script-ul SQL de inserare a înregistrărilor în acest tabel.

SET ECHO OFF;
SET FEEDBACK OFF;

SPOOL insereaza_artisti.sql;

SELECT 'INSERT INTO ARTIST (artist_id, nume, biografie) VALUES (' ||
       artist_id || ',''' || nume || ''',''' || biografie || ''');'
FROM ARTIST
ORDER BY artist_id;

SPOOL OFF;
SET ECHO ON
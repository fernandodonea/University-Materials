
---sgbd tema 1
-- Donea Fernando-Emanuel
-- grupa 243

---ex b)

SET ECHO OFF
SET FEEDBACK OFF

SPOOL insereaza_artisti.sql

SELECT 'INSERT INTO ARTIST (artist_id, nume, biografie) VALUES (' ||
       artist_id || ',''' || nume || ''',''' || biografie || ''');'
FROM ARTIST
ORDER BY artist_id;

SPOOL OFF;
SET ECHO ON
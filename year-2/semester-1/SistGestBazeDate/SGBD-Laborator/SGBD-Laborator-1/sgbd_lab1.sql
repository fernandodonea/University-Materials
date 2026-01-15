---SGBD Laborator 1

------------------SQL Recapitulare 1----------------

CREATE TABLE emp AS
SELECT *
FROM employees;

--ex 11
-- Adăugaţi un comentariu tabelei emp_***.
-- COMMENT ON TABLE emp_*** IS 'Informaţii despre angajati';

COMMENT ON TABLE emp IS 'Informatii despre angajati';



--ex 12
--Folosind vizualizarea user_tab_comments afişaţi comentariul adăugat tabelului emp_***.

select table_name, comments from user_tab_comments where table_name='EMP';



--ex 13
-- Modificaţi formatul datei calendaristice setat la nivel de sesiune astfel încât datele calendaristice să
-- respecte următoarea formă 01.10.2011 16:10:05.
-- Indicaţie: Folosiţi comanda
--          ALTER SESSION SET NLS_DATE_FORMAT = 'formatul dorit';

ALTER SESSION SET NLS_DATE_FORMAT = 'DD.MM.YYYY HH24:MI::SS';

select hire_date from employees;



--ex 14
-- Rulaţi următoarea cerere SQL:
--      SELECT EXTRACT(YEAR FROM SYSDATE)
--      FROM dual;
SELECT EXTRACT(YEAR FROM SYSDATE)
FROM dual;

--ex 15
--Modificaţi cererea anterioară astfel încât să obţineţi ziua, respectiv luna datei curente.

SELECT EXTRACT(DAY FROM SYSDATE),EXTRACT( MONTH FROM SYSDATE)
FROM dual;


--ex 16
-- Afişaţi numele tuturor tabelelor personale create (nume_tabel_***).
-- Indicaţie: Folosiţi vizualizarea user_tables.

select table_name from user_tables;
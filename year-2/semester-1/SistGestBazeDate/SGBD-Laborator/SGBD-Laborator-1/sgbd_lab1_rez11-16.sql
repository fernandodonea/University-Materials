CREATE TABLE emp AS
SELECT *
FROM employees;

--ex 11
COMMENT ON TABLE emp IS 'Informatii despre angajati';

--ex 12
select table_name, comments from user_tab_comments where table_name='EMP';

--ex 13
ALTER SESSION SET NLS_DATE_FORMAT = 'DD.MM.YYYY HH24:MI::SS';

select hire_date from employees;


--ex 14
SELECT EXTRACT(YEAR FROM SYSDATE)
FROM dual;

--ex 15
SELECT EXTRACT(DAY FROM SYSDATE),EXTRACT( MONTH FROM SYSDATE)
FROM dual;


--ex 16
select table_name from user_tables;
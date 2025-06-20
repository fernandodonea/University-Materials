--------BD Laborator 5------

--ex 1
SELECT
    COUNT(T.MANAGER_ID)
FROM (
    SELECT
        DISTINCT MANAGER_ID
    FROM EMPLOYEES
     )T;

--ex 2
SELECT
    EMPLOYEE_ID,LAST_NAME,SALARY
FROM EMPLOYEES
WHERE SALARY >
        (
        SELECT
            AVG(SALARY)
        FROM EMPLOYEES
        );

--ex 3
SELECT
    E.MANAGER_ID, MIN(E.SALARY)
FROM EMPLOYEES E
WHERE E.MANAGER_ID IS NOT NULL
GROUP BY E.MANAGER_ID
HAVING MIN(E.SALARY) > 4000;


--ex 4
SELECT
    MAX("salariu")
FROM (
    SELECT
        ROUND(AVG(SALARY),2) as "salariu"
    FROM EMPLOYEES
    GROUP BY DEPARTMENT_ID
     );
--sau
SELECT
    MAX(ROUND(AVG(SALARY),2))
FROM EMPLOYEES
GROUP BY DEPARTMENT_ID;



--ex 5
SELECT
    E.DEPARTMENT_ID, E.JOB_ID, SUM(E.SALARY)
FROM EMPLOYEES E
WHERE E.DEPARTMENT_ID > 80
GROUP BY E.DEPARTMENT_ID, E.JOB_ID;

--ex 6
SELECT
    SUM(COMMISSION_PCT)/COUNT(*)
FROM EMPLOYEES;

SELECT
    AVG(NVL(COMMISSION_PCT,0))
FROM EMPLOYEES;


--ex8

SELECT
    D.DEPARTMENT_ID,D.DEPARTMENT_NAME,
    COUNT(E.EMPLOYEE_ID) idk
FROM EMPLOYEES E
JOIN DEPARTMENTS D ON E.DEPARTMENT_ID = D.DEPARTMENT_ID
GROUP BY D.DEPARTMENT_ID, D.DEPARTMENT_NAME
HAVING COUNT(E.EMPLOYEE_ID)<4;

--ex 8
SELECT
    AVG(SALARY)
FROM EMPLOYEES
GROUP BY JOB_ID
HAVING AVG(SALARY)=(
    SELECT
        MIN(AVG(SALARY))
    FROM EMPLOYEES
    GROUP BY JOB_ID
    );

--ex 9
SELECT
    DEPARTMENT_ID,MIN(SALARY)
FROM EMPLOYEES
GROUP BY DEPARTMENT_ID
HAVING AVG(SALARY)=(
    SELECT
        MAX(AVG(SALARY))
    FROM EMPLOYEES
    GROUP BY DEPARTMENT_ID
);


--ex 10
SELECT
    D.DEPARTMENT_NAME "nume",
    E.DEPARTMENT_ID "id_dep",
    COUNT(E.EMPLOYEE_ID) "nr_angajati",
    round(AVG(E.SALARY),2) "salariu_mediu"
FROM EMPLOYEES E
JOIN DEPARTMENTS D ON E.DEPARTMENT_ID = D.DEPARTMENT_ID
GROUP BY D.DEPARTMENT_NAME, E.DEPARTMENT_ID;



--ex 10
SELECT
    "nume_dep",
    "id_dep",
    "nr_angajati",
    "salariu_mediu",
    E2.LAST_NAME,
    E2.JOB_ID,
    E2.SALARY
FROM (
    SELECT
        D.DEPARTMENT_NAME "nume_dep",
        E.DEPARTMENT_ID "id_dep",
        COUNT(E.EMPLOYEE_ID) "nr_angajati",
        round(AVG(E.SALARY),2) "salariu_mediu"
    FROM EMPLOYEES E
    JOIN DEPARTMENTS D ON E.DEPARTMENT_ID = D.DEPARTMENT_ID
    GROUP BY D.DEPARTMENT_NAME, E.DEPARTMENT_ID
     )T
JOIN EMPLOYEES E2 ON E2.DEPARTMENT_ID=T."id_dep";











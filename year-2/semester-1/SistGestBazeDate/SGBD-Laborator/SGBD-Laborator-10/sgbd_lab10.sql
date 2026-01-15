--- SGBD Laborator 10




-----------------------------------PACHETE---------------------------------

--ex E1
-- Definiţi un pachet care să permită gestiunea angajaţilor companiei.
-- Pachetul va conţine:
-- a. o procedură care determină adăugarea unui angajat, dându-se informaţii complete despre acesta:
        -- - codul angajatului va fi generat automat utilizându-se o secvenţă;
        -- - informaţiile personale vor fi date ca parametrii (nume, prenume, telefon, email);
        -- - data angajării va fi data curentă;
        -- - salariul va fi cel mai mic salariu din departamentul respectiv, pentru jobul respectiv
    -- (se vor obţine cu ajutorul unei funcţii stocate în pachet);
        -- - nu va avea comision;
        -- - codul managerului se va obţine cu ajutorul unei funcţii stocate în pachet care va avea ca
    -- parametrii numele şi prenumele managerului);
        -- - codul departamentului va fi obţinut cu ajutorul unei funcţii stocate în pachet, dându-se
    -- ca parametru numele acestuia;
        -- - codul jobului va fi obţinut cu ajutorul unei funcţii stocate în pachet, dându-se ca parametru numele acesteia.
-- Observaţie: Trataţi toate excepţiile.


DROP SEQUENCE  seq_angajati;

CREATE SEQUENCE seq_angajati
    START WITH 690
    INCREMENT BY 1
NOCACHE;



CREATE OR REPLACE PACKAGE pachet_E1 AS


    FUNCTION f_find_manager(v_cod_departament DEPARTMENTS.MANAGER_ID%type)
        RETURN NUMBER;

    FUNCTION f_find_departament(v_nume_departament DEPARTMENTS.DEPARTMENT_NAME%type)
        RETURN NUMBER;

    FUNCTION f_find_job(v_nume_job JOBS.JOB_TITLE%type)
        RETURN JOBS.JOB_ID%TYPE;

    FUNCTION f_salariu_minim (v_cod_departament DEPARTMENTS.DEPARTMENT_ID%TYPE, v_cod_job JOBS.JOB_ID%TYPE)
        return NUMBER;



    PROCEDURE p_adaugare_angajat(v_nume EMPLOYEES.LAST_NAME%type,
                                 v_prenume EMPLOYEES.FIRST_NAME%type,
                                v_telefon EMPLOYEES.PHONE_NUMBER%type,
                                v_email EMPLOYEES.EMAIL%type,
                                v_nume_job JOBS.JOB_TITLE%type,
                                v_nume_departament DEPARTMENTS.DEPARTMENT_NAME%type);






END pachet_E1;
/
CREATE OR REPLACE PACKAGE BODY pachet_E1 AS

    FUNCTION f_find_departament(v_nume_departament DEPARTMENTS.DEPARTMENT_NAME%type)
        RETURN NUMBER IS
        cod_departament NUMBER;
    BEGIN
        SELECT DEPARTMENT_ID
        INTO cod_departament
        FROM DEPARTMENTS
        WHERE DEPARTMENT_NAME = v_nume_departament;
    RETURN cod_departament;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            DBMS_OUTPUT.PUT_LINE('Nu exista departamentul ' || v_nume_departament);
            RETURN NULL;
    END f_find_departament;


    FUNCTION f_find_manager(v_cod_departament DEPARTMENTS.MANAGER_ID%type)
        RETURN NUMBER IS
        cod_manager NUMBER;
    BEGIN
        SELECT MANAGER_ID
        INTO cod_manager
        FROM DEPARTMENTS
        WHERE DEPARTMENT_ID = v_cod_departament;
    RETURN cod_manager;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            DBMS_OUTPUT.PUT_LINE('Nu exista manager in departamentul dat ');
            RETURN NULL;
    END f_find_manager;


    FUNCTION f_find_job(v_nume_job JOBS.JOB_TITLE%type)
        RETURN JOBS.JOB_ID%type IS
        cod_job JOBS.JOB_ID%TYPE;
    BEGIN
        SELECT JOB_ID
        INTO cod_job
        FROM JOBS
        WHERE JOB_TITLE=v_nume_job;
    RETURN cod_job;
    END f_find_job;

    FUNCTION f_salariu_minim (v_cod_departament DEPARTMENTS.DEPARTMENT_ID%TYPE, v_cod_job JOBS.JOB_ID%TYPE)
        return NUMBER IS
        v_salariu_minim NUMBER;
    BEGIN
        SELECT MIN(E.SALARY)
        INTO v_salariu_minim
        FROM EMPLOYEES E
        WHERE E.DEPARTMENT_ID=v_cod_departament AND E.JOB_ID=v_cod_job;
    RETURN v_salariu_minim;
    END f_salariu_minim;


    PROCEDURE p_adaugare_angajat(v_nume EMPLOYEES.LAST_NAME%type,
                                 v_prenume EMPLOYEES.FIRST_NAME%type,
                                v_telefon EMPLOYEES.PHONE_NUMBER%type,
                                v_email EMPLOYEES.EMAIL%type,
                                v_nume_job JOBS.JOB_TITLE%type,
                                v_nume_departament DEPARTMENTS.DEPARTMENT_NAME%type) IS
        v_salariu EMPLOYEES.SALARY%type;
        v_data_angajarre EMPLOYEES.HIRE_DATE%type;
        v_cod_job EMPLOYEES.JOB_ID%type;
        v_cod_departament EMPLOYEES.DEPARTMENT_ID%type;
        v_cod_manager EMPLOYEES.MANAGER_ID%type;
    BEGIN
        v_cod_departament:=f_find_departament(v_nume_departament);
        v_cod_job:=f_find_job(v_nume_job);
        v_data_angajarre:=SYSDATE;
        v_salariu:=f_salariu_minim(v_cod_departament,v_cod_job);
        v_cod_manager:=f_find_manager(v_cod_departament);


        INSERT INTO EMPLOYEES (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER, HIRE_DATE, JOB_ID, SALARY, COMMISSION_PCT, MANAGER_ID, DEPARTMENT_ID)
        VALUES (
                seq_angajati.nextval,
                v_prenume,
                v_nume,
                v_email,
                v_telefon,
                v_data_angajarre,
                v_cod_job,
                v_salariu,
                0,
                v_cod_manager,
                v_cod_departament
               );

    END;
END pachet_E1;
/


BEGIN
    pachet_E1.p_adaugare_angajat('Fernando','Donea','243243','email','Programmer','IT');
end;

SELECT *
FROM EMPLOYEES
WHERE FIRST_NAME='Donea';
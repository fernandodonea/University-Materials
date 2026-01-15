--SGBD Laborator 11


--------------------TRIGGERI----------------------



CREATE TABLE dept_DFE (
    id_departament NUMBER(10),
    nume_dept VARCHAR2(256),
    plati NUMBER(10),
    CONSTRAINT cheie_primara PRIMARY KEY (id_departament)
);

INSERT INTO dept_DFE (id_departament, nume_dept, plati)
VALUES (10,
        'Administration',
    1000
       );

INSERT INTO dept_DFE VALUES
                         (
                          20,
                          'Marketing',
                          2000
                         );

--ex E1
-- Definiți un declanșator care să permită ștergerea informațiilor din tabelul dept_*** decât dacă
-- utilizatorul este SCOTT.


CREATE OR REPLACE TRIGGER trigger_E1_stergere_scot
BEFORE DELETE ON dept_DFE
FOR EACH ROW
BEGIN
    IF USER !='SCOTT' THEN
        RAISE_APPLICATION_ERROR(-20000, 'Doar utilizatorul scott poate sterge din tabelul dept_dfe');
    end if;
end;

DELETE dept_DFE WHERE (id_departament=10);




--ex E2
-- Creați un declanșator prin care să nu se permită mărirea comisionului astfel încât să depășească
-- 50% din valoarea salariului.

CREATE OR REPLACE TRIGGER trigger_E2_comison_salariu
BEFORE UPDATE OF COMMISSION_PCT ON EMPLOYEES
FOR EACH ROW
BEGIN
    IF(:NEW.COMMISSION_PCT > 0.5) THEN
        RAISE_APPLICATION_ERROR(-20111,'Comisiunul nu poate depasi 50% din salariu!');
    end if;
end;




UPDATE EMPLOYEES
SET COMMISSION_PCT=0.4
WHERE EMPLOYEE_ID=145;

UPDATE EMPLOYEES
SET COMMISSION_PCT=0.51
WHERE EMPLOYEE_ID=145;

rollback;
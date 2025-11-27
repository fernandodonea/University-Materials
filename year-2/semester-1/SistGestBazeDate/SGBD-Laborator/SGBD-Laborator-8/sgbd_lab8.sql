--SGBD Laborator 8
--grupa 243


----------------ex E1--------------------
CREATE TABLE info_DFE (
    nume_utilizator VARCHAR2(50),
    data_comanda DATE,
    comanda VARCHAR2(200),
    nr_linii_selectate_modificate NUMBER(10),
    eroare VARCHAR2(200)
);


----------------ex E2 ----------------------




CREATE OR REPLACE FUNCTION f2_DFE
    (v_nume employees.last_name%TYPE DEFAULT 'Bell')
RETURN NUMBER IS
    salariu employees.salary%type;

    BEGIN
        SELECT salary INTO salariu
        FROM employees
        WHERE last_name = v_nume;

        INSERT INTO info_DFE (nume_utilizator,data_comanda,comanda, nr_linii_selectate_modificate, eroare)
        VALUES (USER,
              SYSDATE,
              'Functie f2_DFE',
              1,
              NULL);
    RETURN salariu;

    EXCEPTION
    WHEN NO_DATA_FOUND THEN
        INSERT INTO info_DFE (nume_utilizator,data_comanda,comanda, nr_linii_selectate_modificate, eroare)
        VALUES (USER,
              SYSDATE,
              'Functie f2_DFE',
              1,
                'Nu exista angajati cu numele dat'
              );
        RETURN NULL;

    WHEN TOO_MANY_ROWS THEN
        INSERT INTO info_DFE (nume_utilizator,data_comanda,comanda, nr_linii_selectate_modificate, eroare)
        VALUES (USER,
              SYSDATE,
              'Functie f2_DFE',
              1,
                'Exista mai multi angajati cu numele dat'
              );
        RETURN NULL;


    WHEN OTHERS THEN
        INSERT INTO info_DFE (nume_utilizator,data_comanda,comanda, nr_linii_selectate_modificate, eroare)
        VALUES (USER,
              SYSDATE,
              'Functie f2_DFE',
              1,
                'Alta eroare!'
              );
        RETURN NULL;
END f2_DFE;
/







BEGIN
    DBMS_OUTPUT.PUT_LINE('Salariul este '|| f2_DFE);
END;
/

SELECT * FROM INFO_DFE;
/







CREATE OR REPLACE PROCEDURE p4_DFE
        (v_nume employees.last_name%TYPE)
    IS
        salariu employees.salary%TYPE;
    BEGIN
        SELECT salary INTO salariu
        FROM employees
        WHERE last_name = v_nume;

        DBMS_OUTPUT.PUT_LINE('Salariul este '|| salariu);

        INSERT INTO info_DFE (nume_utilizator,data_comanda,comanda, nr_linii_selectate_modificate, eroare)
        VALUES (USER,
              SYSDATE,
              'Procedura p4_DFE',
              1,
              NULL);

    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            INSERT INTO INFO_DFE (nume_utilizator, data_comanda, comanda, nr_linii_selectate_modificate, eroare)
            VALUES (
                    USER,
                    SYSDATE,
                    'Procedura P4',
                    1,
                    'Nu exista angajati cu numele dat'
                   );

        WHEN TOO_MANY_ROWS THEN
            INSERT INTO INFO_DFE (nume_utilizator, data_comanda, comanda, nr_linii_selectate_modificate, eroare)
            VALUES (
                    USER,
                    SYSDATE,
                    'Procedura P4',
                    1,
                    'Exista mai multi angajati cu numele dat'
                   );


        WHEN OTHERS THEN
            INSERT INTO INFO_DFE (nume_utilizator, data_comanda, comanda, nr_linii_selectate_modificate, eroare)
            VALUES (
                    USER,
                    SYSDATE,
                    'Functia P4',
                    1,
                    'Alta eroare'
                   );
    END p4_DFE;
/



BEGIN
    p4_DFE('Bell');
END;

SELECT * FROM INFO_DFE;
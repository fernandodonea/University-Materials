--SGBD Laborator 9


-----------------------------------SUBPROGRAME---------------------------------


-- ex E3
-- Definiți o funcție stocată care determină numărul de angajați care au avut cel puțin 2 joburi
-- diferite și care în prezent lucrează într-un oraș dat ca parametru. Tratați cazul în care orașul dat
-- ca parametru nu există, respectiv cazul în care în orașul dat nu lucrează niciun angajat. Inserați
-- în tabelul info_*** informațiile corespunzătoare fiecărui caz determinat de valoarea dată pentru
-- parametru.


CREATE OR REPLACE FUNCTION func_E3
    (v_oras LOCATIONS.CITY%type DEFAULT 'Seattle')
RETURN NUMBER IS
    id_oras NUMBER :=0;
    cnt_ang NUMBER :=0;

    BEGIN
        --verif ca orasul sa existe
        SELECT LOCATION_ID
        INTO id_oras
        FROM LOCATIONS
        WHERE CITY=v_oras;


        SELECT COUNT(E.EMPLOYEE_ID)
        INTO cnt_ang
        FROM EMPLOYEES E
        JOIN DEPARTMENTS D ON E.DEPARTMENT_ID = D.DEPARTMENT_ID
        WHERE D.LOCATION_ID=id_oras AND E.EMPLOYEE_ID IN (

        --subinterogare angajati cu cel putin 2 joburi
        SELECT employee_id
        FROM (
            SELECT employee_id, job_id FROM job_history
            UNION
            SELECT employee_id, job_id FROM employees
        )
        GROUP BY employee_id
        HAVING COUNT(DISTINCT job_id) >= 2
            );



        IF cnt_ang > 0 THEN
            INSERT INTO info_DFE (nume_utilizator,data_comanda,comanda, nr_linii_selectate_modificate, eroare)
        VALUES (USER,
              SYSDATE,
              'Functia func_E3',
              cnt_ang,
              NULL);

        ELSE
             INSERT INTO info_DFE (nume_utilizator,data_comanda,comanda, nr_linii_selectate_modificate, eroare)
        VALUES (USER,
              SYSDATE,
              'Functia func_E3',
              0,
              'Nu lucreaza niciun angajat cu cel putin 2 joburi in orasul' || v_oras);
        END IF;

        RETURN cnt_ang;

    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            INSERT INTO INFO_DFE (nume_utilizator, data_comanda, comanda, nr_linii_selectate_modificate, eroare)
            VALUES (
                    USER,
                    SYSDATE,
                    'Functia func_E3',
                    0,
                    'Nu exista orasul cu numele dat'
                   );
            RETURN -1;

        WHEN OTHERS THEN
            INSERT INTO INFO_DFE (nume_utilizator, data_comanda, comanda, nr_linii_selectate_modificate, eroare)
            VALUES (
                    USER,
                    SYSDATE,
                    'Functia func_E3',
                    1,
                    'Alta eroare'
                   );
            RETURN -2;

    end func_E3;
/


BEGIN
    DBMS_OUTPUT.PUT_LINE('Angajati care au avut cel putin 2 joburi diferite si acum lucreaza in Seatle : ' || func_E3());
END;
/

BEGIN
    DBMS_OUTPUT.PUT_LINE('Angajati care au avut cel putin 2 joburi diferite si acum lucreaza in Roma : ' || func_E3('Roma'));
END;
/



SELECT * FROM INFO_DFE;
/






---SGBD Tema 6

--E4 (lab suprograme)

--     Definiți o procedură stocată care mărește cu 10% salariile tuturor angajaților conduși direct sau
-- indirect de către un manager al cărui cod este dat ca parametru. Tratați cazul în care nu există
-- niciun manager cu codul dat. Inserați în tabelul info_*** informațiile corespunzătoare fiecărui
-- caz determinat de valoarea dată pentru parametru.


CREATE OR REPLACE PROCEDURE pachet_E4 (v_cod_manager EMPLOYEES.MANAGER_ID%type)
AS
    v_nr_manageri NUMBER;
    v_nr_angajati NUMBER;
BEGIN
    --verificam daca managerul exista
    SELECT COUNT(*) INTO v_nr_manageri
    FROM EMPLOYEES
    WHERE EMPLOYEE_ID=v_cod_manager;

    --verificam daca exista managerul
    IF v_nr_manageri =0 THEN
        INSERT INTO info_DFE (nume_utilizator,data_comanda,comanda, nr_linii_selectate_modificate, eroare)
        VALUES (USER,
              SYSDATE,
              'Pachetul pachet_E4',
              0,
              'Managerul nu exista');
    ELSE
        SELECT COUNT(*) INTO v_nr_angajati
        FROM EMPLOYEES
        WHERE MANAGER_ID=v_cod_manager;

        --managerul nu are angajati
        IF v_nr_angajati=0 THEN
                    INSERT INTO info_DFE (nume_utilizator,data_comanda,comanda, nr_linii_selectate_modificate, eroare)
                    VALUES (USER,
                          SYSDATE,
                          'Pachetul pachet_E4',
                          0,
                          'Managerul nu are angajati');
        ELSE
            UPDATE EMPLOYEES
            SET SALARY = SALARY*1.1
            WHERE EMPLOYEE_ID IN (
                SELECT EMPLOYEE_ID
                FROM EMPLOYEES
                WHERE MANAGER_ID=100
                );

        INSERT INTO info_DFE (nume_utilizator,data_comanda,comanda, nr_linii_selectate_modificate, eroare)
        VALUES (USER,
              SYSDATE,
              'Pachetul pachet_E4',
              v_nr_angajati,
              'NULL');
        end if;
    end if;
    COMMIT;
end pachet_E4;
/




BEGIN
    pachet_E4(100);
END;

BEGIN
    pachet_E4(1321312312312);
END;


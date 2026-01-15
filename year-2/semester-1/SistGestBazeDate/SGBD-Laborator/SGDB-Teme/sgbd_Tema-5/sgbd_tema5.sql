-- SGBD TEMA 5



--E3 (lab cursoare)

-- Modificați exercițiul anterior astfel încât să obțineți suma totală alocată lunar pentru plata
-- salariilor și a comisioanelor tuturor angajaților, iar pentru fiecare angajat cât la sută din această
-- sumă câștigă lunar.


DECLARE
    v_job_id JOBS.JOB_ID%TYPE;
    v_job_title JOBS.JOB_TITLE%TYPE;
    v_nume EMPLOYEES.LAST_NAME%TYPE;
    v_salary EMPLOYEES.SALARY%TYPE;

    -- pentru fiecare job
    nr_ordine_ang NUMBER := 0;
    nr_total_ang_job NUMBER := 0;
    venit_lunar_job NUMBER := 0;
    venit_mediu_job NUMBER := 0;

    -- pentru companie
    nr_total_ang_companie NUMBER := 0;
    venit_lunar_companie NUMBER := 0;
    venit_mediu_companie NUMBER := 0;

    -- E3
    v_suma_totala_lunar_plus_comison NUMBER := 0;
    v_comision EMPLOYEES.COMMISSION_PCT%TYPE;
    v_salariu_cu_comosion NUMBER := 0;
    v_procent_din_salariu NUMBER := 0;

    -- cursor pentru joburi
    CURSOR cursor_j IS
        SELECT J.JOB_ID, J.JOB_TITLE FROM JOBS J;

    -- cursor parametrizat pentru angajati per job
    CURSOR cursor_ang_j(p_job_id JOBS.JOB_ID%TYPE) IS
        SELECT E.LAST_NAME, E.SALARY, E.COMMISSION_PCT
        FROM EMPLOYEES E
        WHERE E.JOB_ID = p_job_id;
BEGIN
    -- calculul sumei totale (salariu + comision)
    SELECT SUM(E.SALARY + (E.SALARY * NVL(E.COMMISSION_PCT, 0)))
    INTO v_suma_totala_lunar_plus_comison
    FROM EMPLOYEES E;

    DBMS_OUTPUT.PUT_LINE('----------------------------------------');
    DBMS_OUTPUT.PUT_LINE('SUMA TOTALA LUNARA ALOCATA PENTRU PLATA SALARIILOR: ' || v_suma_totala_lunar_plus_comison);
    DBMS_OUTPUT.PUT_LINE('----------------------------------------');

    OPEN cursor_j;
    LOOP
        FETCH cursor_j INTO v_job_id, v_job_title;
        EXIT WHEN cursor_j%NOTFOUND;

        DBMS_OUTPUT.PUT_LINE(' ');
        DBMS_OUTPUT.PUT_LINE('----------------------------------------');
        DBMS_OUTPUT.PUT_LINE('JOB: ' || v_job_title);

        -- reset pentru job
        nr_ordine_ang := 0;
        nr_total_ang_job := 0;
        venit_lunar_job := 0;
        venit_mediu_job := 0;

        OPEN cursor_ang_j(v_job_id);
        LOOP
            FETCH cursor_ang_j INTO v_nume, v_salary, v_comision;
            EXIT WHEN cursor_ang_j%NOTFOUND;

            nr_total_ang_job := nr_total_ang_job + 1;
            nr_ordine_ang := nr_ordine_ang + 1;

            -- salariu cu comision
            v_salariu_cu_comosion := v_salary + (v_salary * NVL(v_comision, 0));
            venit_lunar_job := venit_lunar_job + v_salariu_cu_comosion;

            IF v_suma_totala_lunar_plus_comison > 0 THEN
                v_procent_din_salariu := (v_salariu_cu_comosion / v_suma_totala_lunar_plus_comison) * 100;
            ELSE
                v_procent_din_salariu := 0;
            END IF;

            DBMS_OUTPUT.PUT_LINE(
                nr_ordine_ang || ': ' || v_nume || ' cu salariul ' ||
                (v_salariu_cu_comosion || ' (' ||
               TO_CHAR(v_procent_din_salariu,'0.99') || '% )' )
            );
        END LOOP;
        CLOSE cursor_ang_j;

        IF nr_total_ang_job = 0 THEN
            DBMS_OUTPUT.PUT_LINE('nu exista angajati cu jobul ' || v_job_title);
        ELSE
            venit_mediu_job := venit_lunar_job / nr_total_ang_job;

            -- statistica pentru companie
            nr_total_ang_companie := nr_total_ang_companie + nr_total_ang_job;
            venit_lunar_companie := venit_lunar_companie + venit_lunar_job;

            DBMS_OUTPUT.PUT_LINE(' ');
            DBMS_OUTPUT.PUT_LINE('Nr angajati: ' || nr_total_ang_job);
            DBMS_OUTPUT.PUT_LINE('Valoarea lunara a veniturilor: ' || venit_lunar_job);
            DBMS_OUTPUT.PUT_LINE('Valoarea medie: ' || venit_mediu_job);
        END IF;
    END LOOP;
    CLOSE cursor_j;

    DBMS_OUTPUT.PUT_LINE(' ');
    DBMS_OUTPUT.PUT_LINE('----------------------------------------');
    DBMS_OUTPUT.PUT_LINE('STATISTICA COMPANIE');
    DBMS_OUTPUT.PUT_LINE('Nr angajati: ' || nr_total_ang_companie);
    DBMS_OUTPUT.PUT_LINE('Venit lunar total: ' || venit_lunar_companie);
    IF nr_total_ang_companie > 0 THEN
        venit_mediu_companie := venit_lunar_companie / nr_total_ang_companie;
    ELSE
        venit_mediu_companie := 0;
    END IF;
    DBMS_OUTPUT.PUT_LINE('Venit lunar mediu: ' || venit_mediu_companie);
END;
/

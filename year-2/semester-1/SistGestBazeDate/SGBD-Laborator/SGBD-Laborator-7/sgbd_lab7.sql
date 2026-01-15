-- SGBD Laborator 7

-----------------------------------CURSOARE---------------------------------


-- E2. Modificați exercițiul anterior astfel încât să obțineți și următoarele informații:
-- - un număr de ordine pentru fiecare angajat care va fi resetat pentru fiecare job
    -- - pentru fiecare job
            -- o numărul de angajați
            -- o valoarea lunară a veniturilor angajaților
            -- o valoarea medie a veniturilor angajaților
    -- - indiferent job
            -- o numărul total de angajați
            -- o valoarea totală lunară a veniturilor angajaților
            -- o valoarea medie a veniturilor angajaților


--a) cursor clasic
DECLARE
    v_job_id JOBS.JOB_ID%type;
    v_job_title JOBS.JOB_TITLE%type;
    v_nume EMPLOYEES.LAST_NAME%type;
    v_salary EMPLOYEES.SALARY%type;

    --pentru fiecare job
    nr_ordine_ang NUMBER;

    nr_total_ang_job NUMBER;
    venit_lunar_job NUMBER;
    venit_mediu_job NUMBER;


    --indiferent de job
    nr_total_ang_companie NUMBER;
    venit_lunar_companie NUMBER;
    venit_mediu_companie NUMBER;



    --cursor pentru joburi
    CURSOR cursor_j IS
            SELECT
                J.JOB_ID, J.JOB_TITLE
            FROM JOBS J;

    --cursor paramtrizat pentru a afla angajatii din fiecare job
    CURSOR cursor_ang_j(p_job_id JOBS.JOB_ID%type) IS
        SELECT
             E.LAST_NAME, E.SALARY
        FROM EMPLOYEES E
        WHERE E.JOB_ID=p_job_id;

BEGIN

    nr_total_ang_companie:=0;
    venit_lunar_companie:=0;
    venit_mediu_companie:=0;




    OPEN cursor_j;

    LOOP
        --preluam un job
        FETCH cursor_j INTO v_job_id,v_job_title;
        EXIT WHEN cursor_j%NOTFOUND;

        DBMS_OUTPUT.PUT_LINE(' ');
        DBMS_OUTPUT.PUT_LINE(' ');
        DBMS_OUTPUT.PUT_LINE('----------------------------------------');
        DBMS_OUTPUT.PUT_LINE('JOB:' || v_job_title);


        --resetam la zero pentru fiecare job
        nr_ordine_ang:=0;
        nr_total_ang_job:=0;
        venit_lunar_job:=0;
        venit_mediu_job:=0;

        OPEN cursor_ang_j(v_job_id);


        LOOP
            FETCH cursor_ang_j INTO v_nume, v_salary;
            EXIT WHEN cursor_ang_j%NOTFOUND;

            nr_total_ang_job:=nr_total_ang_job+1;--crestem numarul de angajati
            nr_ordine_ang:=nr_ordine_ang+1; --crestem oridnul angajatului
            venit_lunar_job:=venit_lunar_job+v_salary; --valoarea lunara a veniturilor angajaților


            DBMS_OUTPUT.PUT_LINE(nr_ordine_ang||': '  ||v_nume || 'cu salariul ' || v_salary);

        end loop;
        CLOSE cursor_ang_j;



        if nr_total_ang_job=0 then
            DBMS_OUTPUT.PUT_LINE('nu exista angajati cu jobul' || v_job_title);
        else
            venit_mediu_job:=venit_lunar_job/nr_total_ang_job; --daca nu avem atunci 0/0


            --statistica pentru companie:
            nr_total_ang_companie:=nr_total_ang_companie+nr_total_ang_job;
            venit_lunar_companie:=venit_lunar_companie+venit_lunar_job;



            DBMS_OUTPUT.PUT_LINE(' ');
            DBMS_OUTPUT.PUT_LINE('Nr angajati: ' || nr_total_ang_job);
            DBMS_OUTPUT.PUT_LINE('Valoarea lunara a veniturilor: ' || venit_lunar_job);
            DBMS_OUTPUT.PUT_LINE('Valoarea medie: '|| venit_mediu_job);
        end if;

    end loop;
    CLOSE cursor_j;



    DBMS_OUTPUT.PUT_LINE(' ');
    DBMS_OUTPUT.PUT_LINE(' ');
    DBMS_OUTPUT.PUT_LINE('----------------------------------------');
    DBMS_OUTPUT.PUT_LINE('STATISTICA COMAPANIE');
    DBMS_OUTPUT.PUT_LINE(' ');
    DBMS_OUTPUT.PUT_LINE('Nr angajati: ' || nr_total_ang_companie);
    DBMS_OUTPUT.PUT_LINE('Venit lunar total: ' || venit_lunar_companie);
    venit_mediu_companie:=venit_lunar_companie/nr_total_ang_companie;
    DBMS_OUTPUT.PUT_LINE('Venit lunar mediu: ' || venit_mediu_companie);


END;










--b) ciclu cursor

DECLARE
    --cursor pentru joburi
    CURSOR cursor_j IS
            SELECT
                J.JOB_ID, J.JOB_TITLE
            FROM JOBS J;

    --cursor paramtrizat pentru a afla angajatii din fiecare job
    CURSOR cursor_ang_j(p_job_id JOBS.JOB_ID%type) IS
        SELECT
             E.LAST_NAME, E.SALARY
        FROM EMPLOYEES E
        WHERE E.JOB_ID=p_job_id;


    --pentru fiecare job
    nr_ordine_ang NUMBER;

    nr_total_ang_job NUMBER;
    venit_lunar_job NUMBER;
    venit_mediu_job NUMBER;


    --indiferent de job
    nr_total_ang_companie NUMBER;
    venit_lunar_companie NUMBER;
    venit_mediu_companie NUMBER;


BEGIN

    --pentru companie
    nr_total_ang_companie:=0;
    venit_lunar_companie:=0;
    venit_mediu_companie:=0;


    FOR v_job IN cursor_j LOOP

        --resetam la zero pentru fiecare job
        nr_ordine_ang:=0;
        nr_total_ang_job:=0;
        venit_lunar_job:=0;
        venit_mediu_job:=0;



        DBMS_OUTPUT.PUT_LINE(' ');
        DBMS_OUTPUT.PUT_LINE(' ');
        DBMS_OUTPUT.PUT_LINE('----------------------------------------');
        DBMS_OUTPUT.PUT_LINE('JOB:' || v_job.JOB_TITLE);


        for v_ang IN cursor_ang_j(v_job.JOB_ID) LOOP

            nr_total_ang_job:=nr_total_ang_job+1;--crestem numarul de angajati
            nr_ordine_ang:=nr_ordine_ang+1; --crestem oridnul angajatului
            venit_lunar_job:=venit_lunar_job+v_ang.SALARY; --valoarea lunara a veniturilor angajaților


            DBMS_OUTPUT.PUT_LINE(nr_ordine_ang ||':' || v_ang.LAST_NAME || ' cu salariul ' || v_ang.SALARY);


        end loop;

        if nr_total_ang_job=0 then
            DBMS_OUTPUT.PUT_LINE('nu exista angajati cu jobul' || v_job.JOB_TITLE);
        else
            venit_mediu_job:=venit_lunar_job/nr_total_ang_job; --daca nu avem atunci 0/0


            --statistica pentru companie:
            nr_total_ang_companie:=nr_total_ang_companie+nr_total_ang_job;
            venit_lunar_companie:=venit_lunar_companie+venit_lunar_job;


            DBMS_OUTPUT.PUT_LINE(' ');
            DBMS_OUTPUT.PUT_LINE('Nr angajati: ' || nr_total_ang_job);
            DBMS_OUTPUT.PUT_LINE('Valoarea lunara a veniturilor: ' || venit_lunar_job);
            DBMS_OUTPUT.PUT_LINE('Valoarea medie: '|| venit_mediu_job);
        end if;

    end loop;

    DBMS_OUTPUT.PUT_LINE(' ');
    DBMS_OUTPUT.PUT_LINE(' ');
    DBMS_OUTPUT.PUT_LINE('----------------------------------------');
    DBMS_OUTPUT.PUT_LINE('STATISTICA COMAPANIE');
    DBMS_OUTPUT.PUT_LINE(' ');
    DBMS_OUTPUT.PUT_LINE('Nr angajati: ' || nr_total_ang_companie);
    DBMS_OUTPUT.PUT_LINE('Venit lunar total: ' || venit_lunar_companie);
    venit_mediu_companie:=venit_lunar_companie/nr_total_ang_companie;
    DBMS_OUTPUT.PUT_LINE('Venit lunar mediu: ' || venit_mediu_companie);


end;





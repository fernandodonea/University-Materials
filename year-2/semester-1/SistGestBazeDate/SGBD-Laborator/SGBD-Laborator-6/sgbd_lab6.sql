--SGBD Laborator  6

-----------------------------------CURSOARE---------------------------------

-- E1
-- Pentru fiecare job (titlu – care va fi afișat o singură dată) obțineți lista angajaților (nume și
-- salariu) care lucrează în prezent pe jobul respectiv. Tratați cazul în care nu există angajați care
-- să lucreze în prezent pe un anumit job. Rezolvați problema folosind:
    -- a. cursoare clasice
    -- b. ciclu cursoare
    -- c. ciclu cursoare cu subcereri
    -- d. expresii cursor



--a) cursor clasic

DECLARE
    v_job_id JOBS.JOB_ID%type;
    v_job_title JOBS.JOB_TITLE%type;
    v_nume EMPLOYEES.LAST_NAME%type;
    v_salary EMPLOYEES.SALARY%type;
    k NUMBER; --contor pentru a nr cati angajati avem per job

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
    OPEN cursor_j;
    LOOP
        --preluam un job
        FETCH cursor_j INTO v_job_id,v_job_title;
        EXIT WHEN cursor_j%NOTFOUND;

        DBMS_OUTPUT.PUT_LINE(' ');
        DBMS_OUTPUT.PUT_LINE('JOB:' || v_job_title);


        k :=0; --resetam
        OPEN cursor_ang_j(v_job_id);

        LOOP
            FETCH cursor_ang_j INTO v_nume, v_salary;
            EXIT WHEN cursor_ang_j%NOTFOUND;

            k:=k+1;

            DBMS_OUTPUT.PUT_LINE(v_nume || 'cu salariul' || v_salary);
        end loop;
        CLOSE cursor_ang_j;

        if k=0 then
            DBMS_OUTPUT.PUT_LINE('nu exista angajati cu jobul' || v_job_title);
        end if;

    end loop;
    CLOSE cursor_j;
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

    k NUMBER;
BEGIN
    FOR v_job IN cursor_j LOOP

        DBMS_OUTPUT.PUT_LINE(' ');
        DBMS_OUTPUT.PUT_LINE('JOB:' || v_job.JOB_TITLE);

        k:=0;

        for v_ang IN cursor_ang_j(v_job.JOB_ID) LOOP

            DBMS_OUTPUT.PUT_LINE(v_ang.LAST_NAME || ' cu salariul ' || v_ang.SALARY);
            k:=k+1;

        end loop;

        if k=0 then
            DBMS_OUTPUT.PUT_LINE('nu exista angajati cu jobul ' || v_job.JOB_TITLE);
        end if;

    end loop;
end;





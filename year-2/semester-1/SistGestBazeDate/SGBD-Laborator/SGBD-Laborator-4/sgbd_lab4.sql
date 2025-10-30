declare
--cream tipul de date
    type INFO_ANG is record (
        COD EMPLOYEES.EMPLOYEE_ID%type,
        SALARIU EMPLOYEES.SALARY%type
    );

--cream colectia
    type PRST_PLAT is table of INFO_ANG;

--cream variabila
    V_PRST_PLATIT PRST_PLAT;
    V_SALARIU_VECHI EMPLOYEES.SALARY%type;

begin
    --selectam primii 5 angajatii cu cel mai mic salariu si salvam in colectie
    select EMPLOYEE_ID, SALARY
    bulk collect into V_PRST_PLATIT
    from (
        select EMPLOYEE_ID, SALARY
        from EMPLOYEES
        where COMMISSION_PCT is null
        order by SALARY asc
    )
    where ROWNUM <= 5;


    for i in 1..5 loop
        --salvam salariul vechi
        V_SALARIU_VECHI := V_PRST_PLATIT(i).SALARIU; 

        --marmi salariul nou cu 5%
        V_PRST_PLATIT(i).SALARIU:=V_PRST_PLATIT(i).SALARIU*1.05;

        DBMS_OUTPUT.PUT_LINE ('Angajatul cu codul ' || V_PRST_PLATIT(i).COD ||
                              ' are salariul vechi ' || V_SALARIU_VECHI ||
                              ' si salariul nou ' || (V_SALARIU_VECHI * 1.05));
    end loop;
END;
/


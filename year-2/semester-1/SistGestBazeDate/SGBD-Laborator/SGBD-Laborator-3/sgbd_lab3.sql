-- SGBD Laborator
-- Donea Fernando-Emanuel


-- EX 1

DECLARE
    numar number(3):=100;
    mesaj1 varchar2(255):='text 1';
    mesaj2 varchar2(255):='text 2';
BEGIN
        DECLARE
            numar number(3):=1;
            mesaj1 varchar2(255):='text 2';
            mesaj2 varchar2(255):='text 3';
        BEGIN
            numar:=numar+1;
            mesaj2:=mesaj2||' adaugat in sub-bloc';
        END;
    numar:=numar+1;
    mesaj1:=mesaj1||' adaugat un blocul principal';
    mesaj2:=mesaj2||' adaugat in blocul principal';
END;

-- a) subbloc numar=2
-- b) subbloc mesaj1='text 2'
-- c) subbloc mesaj2='text 3 adaugat in sub-bloc'
-- d) bloc numar=101
-- e) bloc mesaj1='text 1 adaugat in blocul principal'
-- f) bloc mesaj2='text 2 adaugat in blocul principal'





--EX 3


SET SERVEROUTPUT ON;
DECLARE
    v_nume_membru    MEMBER.LAST_NAME%TYPE := '&nume_de_la_tast';
    v_membru_id    MEMBER.MEMBER_ID%TYPE;
    v_nr_filme NUMBER;
BEGIN
    SELECT MEMBER_ID
    INTO   v_membru_id
    FROM   member
    WHERE  UPPER(last_name) = UPPER(v_nume_membru);

    SELECT COUNT(title_id)
    INTO   v_nr_filme
    FROM   rental
    WHERE  MEMBER_ID = v_membru_id;

    DBMS_OUTPUT.PUT_LINE( v_nume_membru || ''' a inchirita ' || v_nr_filme || ' filme');

EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Eroare: Nu exista membrul cu numele ''' || v_nume_membru);
    WHEN TOO_MANY_ROWS THEN
        DBMS_OUTPUT.PUT_LINE('Eroare: Exista mai mult decat un membru cu numele ''' || v_nume_membru);
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(SQLERRM);
END;
/

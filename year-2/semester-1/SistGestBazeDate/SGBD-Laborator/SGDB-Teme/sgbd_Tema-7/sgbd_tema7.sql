-- SGBD Tema 7

--ex E2 (lab pachete)
--  Adaptați cerința exercițiului 3 din partea I (pachete definite de utilizator) pentru diagrama
-- proiectului prezentată la materia Baze de Date din anul I. Rezolvați acest exercițiu în PL/SQL,
-- folosind baza de date proprie.


-- ex 3 parea I
--  Definiţi un pachet cu ajutorul căruia să se obţină salariul maxim înregistrat pentru salariaţii care
-- lucrează într-un anumit oraş şi lista salariaţilor care au salariul mai mare sau egal decât acel
-- maxim. Pachetul va conţine un cursor şi un subprogram funcţie.



-- Definiti un pachet cu ajutorul caruia sa se obtina pretul maxim al unui album pentru un anumit gen muzical (dat ca parametru)
--si lista albumelor care au pretul egal cu acel maxim. Pachetul va contine un cursor si un subprogram de tip functie


CREATE OR REPLACE PACKAGE pachet_pret_album_gen AS
    CURSOR c_album (v_pret_minim NUMBER) RETURN ALBUM%ROWTYPE;

    FUNCTION f_pret_max_gen_muzical (v_gen_muzical GEN_MUZICAL.DENUMIRE%type) RETURN NUMBER;
END pachet_pret_album_gen;
/
CREATE OR REPLACE PACKAGE BODY pachet_pret_album_gen AS

    --cursor care returneaza albumele care sunt mai scumpe decat un nr dat ca parametru
    CURSOR c_album (v_pret_minim NUMBER) RETURN ALBUM%ROWTYPE
    IS
        SELECT *
        FROM ALBUM
        WHERE PRET>=v_pret_minim;


    --functie care returneaza pretul celui mai scump album dintr-o categorie muzicala
    FUNCTION f_pret_max_gen_muzical (v_gen_muzical GEN_MUZICAL.DENUMIRE%type) RETURN NUMBER IS
        v_maxim NUMBER;
    BEGIN
        SELECT MAX(A.PRET)
        INTO v_maxim
        FROM ALBUM A
        JOIN ALBUM_GEN_MUZICAL AG ON A.ALBUM_ID = AG.ALBUM_ID
        JOIN GEN_MUZICAL G ON AG.GEN_ID = G.GEN_ID
        WHERE G.DENUMIRE=v_gen_muzical;

        return v_maxim;
    END f_pret_max_gen_muzical;


END pachet_pret_album_gen;
/



DECLARE
    v_gen GEN_MUZICAL.DENUMIRE%type := 'Hip-Hop';
    v_maxim NUMBER;
    lista ALBUM%ROWTYPE;
BEGIN
    DBMS_OUTPUT.PUT_LINE(' ');
    v_maxim:=pachet_pret_album_gen.f_pret_max_gen_muzical(v_gen);

    DBMS_OUTPUT.PUT_LINE('Albumul cel mai scump din gen-ul muzical ' || v_gen || ' costa ' || v_maxim);
    DBMS_OUTPUT.PUT_LINE('Albume care au pretul mai mare sau egal cu  ' || v_maxim || ':');


    FOR v_cursor IN pachet_pret_album_gen.c_album(v_maxim) LOOP
        DBMS_OUTPUT.PUT_LINE('------------------------------------');
        DBMS_OUTPUT.PUT_LINE(v_cursor.TITLU||' '|| v_cursor.PRET);
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('------------------------------------');
end;





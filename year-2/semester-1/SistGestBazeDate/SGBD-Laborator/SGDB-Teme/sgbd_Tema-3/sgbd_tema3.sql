--SGBD Tema 3


-- E4. Modificați problema anterioară astfel încât să afișați și următorul text:
-- - Categoria 1 (a împrumutat mai mult de 75% din titlurile existente)
-- - Categoria 2 (a împrumutat mai mult de 50% din titlurile existente)
-- - Categoria 3 (a împrumutat mai mult de 25% din titlurile existente)
-- - Categoria 4 (altfel)
-- E5. Creați tabelul member_*** (o copie a tabelului member). Adăugați în acest tabel coloana
-- discount, care va reprezenta procentul de reducere aplicat pentru membrii, în funcție de categoria
-- din care fac parte aceștia:
-- - 10% pentru membrii din Categoria 1
-- - 5% pentru membrii din Categoria 2
-- - 3% pentru membrii din Categoria 3
-- - nimic
-- Actualizați coloana discount pentru un membru al cărui cod este dat de la tastatură. Afișați un
-- mesaj din care să reiasă dacă actualizarea s-a produs sau nu.







---------------------------- REZOLVARE----------------------------

-- ex E3
-- Definiți un bloc anonim în care să se determine numărul de filme (titluri) împrumutate de un
-- membru al cărui nume este introdus de la tastatură. Tratați următoarele două situații: nu există nici
-- un membru cu nume dat; există mai mulți membrii cu același nume.
-- SET SERVEROUTPUT ON;

DECLARE

    --v_nume member.last_name%TYPE := '&p_nume'; nume de la tastatura
    v_nume member.last_name%TYPE := 'Ngao';--nume de la tastatura

   --numar membri
    v_nr_membri NUMBER;
    v_nr_filme NUMBER;
BEGIN
    --verif cati membri au numele dat
    SELECT COUNT(*)
    INTO v_nr_membri
    FROM member
    WHERE last_name = v_nume;


    IF v_nr_membri = 0 THEN
        DBMS_OUTPUT.PUT_LINE('Nu exista niciun membru cu numele ' || v_nume);

    ELSIF v_nr_membri > 1 THEN
        DBMS_OUTPUT.PUT_LINE('Exista mai multi membri cu numele ' || v_nume);

    ELSE --un singur membru

        --calc nr de titiluri distincte impr
        SELECT COUNT(DISTINCT r.title_id)
        INTO v_nr_filme
        FROM rental r
        JOIN member m ON r.member_id = m.member_id
        WHERE m.last_name = v_nume;

        --afisam rezultatul
        DBMS_OUTPUT.PUT_LINE('Membrul ' || v_nume || ' a imprumutat ' || v_nr_filme || ' titluri distincte.');

    END IF;
END;
/




--ex E4
--  Modificați problema anterioară astfel încât să afișați și următorul text:
    -- - Categoria 1 (a împrumutat mai mult de 75% din titlurile existente)
    -- - Categoria 2 (a împrumutat mai mult de 50% din titlurile existente)
    -- - Categoria 3 (a împrumutat mai mult de 25% din titlurile existente)
    -- - Categoria 4 (altfel)
SET SERVEROUTPUT ON;

DECLARE
   --v_nume member.last_name%TYPE := '&p_nume'; nume de la tastatura
    v_nume member.last_name%TYPE := 'Ngao';--nume de la tastatura

    v_nr_membri NUMBER;
    v_nr_filme NUMBER;
    v_total_filme NUMBER;
    v_procent NUMBER;
BEGIN
    SELECT COUNT(*)
    INTO v_nr_membri
    FROM member
    WHERE last_name = v_nume;

    IF v_nr_membri = 0 THEN
        DBMS_OUTPUT.PUT_LINE('Nu exista niciun membru cu numele dat.');

    ELSIF v_nr_membri > 1 THEN
        DBMS_OUTPUT.PUT_LINE('Exista mai multi membri cu acelasi nume.');

    ELSE
        -- calc nr de filme impr de membru
        SELECT COUNT(DISTINCT r.title_id)
        INTO v_nr_filme
        FROM rental r
        JOIN member m ON r.member_id = m.member_id
        WHERE m.last_name = v_nume;

        -- calc nr. total de titluri
        SELECT COUNT(*) INTO v_total_filme FROM title;

        -- nr de titluri impr
        DBMS_OUTPUT.PUT_LINE('Membrul ' || v_nume || ' a imprumutat ' || v_nr_filme || ' titluri.');

        --calculam procentul
        IF v_total_filme > 0 THEN
            v_procent := (v_nr_filme / v_total_filme) * 100;
        ELSE
            v_procent := 0;
        END IF;

        -- det si afisam categoria
        IF v_procent > 75 THEN
            DBMS_OUTPUT.PUT_LINE('Categoria 1 (a imprumutat mai mult de 75% din titlurile existente)');
        ELSIF v_procent > 50 THEN
            DBMS_OUTPUT.PUT_LINE('Categoria 2 (a imprumutat mai mult de 50% din titlurile existente)');
        ELSIF v_procent > 25 THEN
            DBMS_OUTPUT.PUT_LINE('Categoria 3 (a imprumutat mai mult de 25% din titlurile existente)');
        ELSE
            DBMS_OUTPUT.PUT_LINE('Categoria 4 (altfel)');
        END IF;

    END IF;
END;
/





--ex E5
-- Creați tabelul member_*** (o copie a tabelului member). Adăugați în acest tabel coloana
-- discount, care va reprezenta procentul de reducere aplicat pentru membrii, în funcție de categoria
-- din care fac parte aceștia:
    -- - 10% pentru membrii din Categoria 1
    -- - 5% pentru membrii din Categoria 2
    -- - 3% pentru membrii din Categoria 3
    -- - nimic
-- Actualizați coloana discount pentru un membru al cărui cod este dat de la tastatură. Afișați un
-- mesaj din care să reiasă dacă actualizarea s-a produs sau nu.



--cream tabelul
CREATE TABLE member_dfe AS SELECT * FROM member;

--adaugam coloana discount
ALTER TABLE member_dfe ADD (discount NUMBER(3));


SET SERVEROUTPUT ON;

DECLARE
    --v_cod_membru NUMBER :='&p_cod';
    v_cod_membru NUMBER := 101;
    v_nr_filme NUMBER;
    v_total_filme NUMBER;
    v_procent NUMBER;
    v_discount member_dfe.discount%TYPE;
BEGIN
    -- calc nr. de filme impr de un mebru dat
    SELECT COUNT(DISTINCT title_id)
    INTO v_nr_filme
    FROM rental
    WHERE member_id = v_cod_membru;

    -- calc nr totoal de titluri exis
    SELECT COUNT(*) INTO v_total_filme FROM title;

    -- calc procentul
    IF v_total_filme > 0 THEN
        v_procent := (v_nr_filme / v_total_filme) * 100;
    ELSE
        v_procent := 0;
    END IF;

    -- determinam discount-ul
    CASE
        WHEN v_procent > 75 THEN v_discount := 10;
        WHEN v_procent > 50 THEN v_discount := 5;
        WHEN v_procent > 25 THEN v_discount := 3;
        ELSE v_discount := 0;
    END CASE;

    -- actualizam membrul
    UPDATE member_dfe
    SET discount = v_discount
    WHERE member_id = v_cod_membru;

    -- verificam daca s-a realizat actualizarea
    IF SQL%ROWCOUNT = 0 THEN
        DBMS_OUTPUT.PUT_LINE('Actualizare esuata. Nu exista un membru cu codul ' || v_cod_membru);
    ELSE
        DBMS_OUTPUT.PUT_LINE('Actualizare realizata pentru membrul ' || v_cod_membru || '. Discount aplicat: ' || v_discount || '%.');
    END IF;
END;
/

-- SGBD Laborator 5


-----------------------------------EXERCITIU BONUS---------------------------------

-- Definiți un tip de colecție denumit tip_sesiuni_***, care va
-- reprezenta o listă de sesiuni desfășurate într-o conferință.

-- Creați tabelul program_conferinta_*** cu următoarea
-- structură:
        -- cod_conferinta NUMBER(5): Codul unic al conferinței.
        -- titlu_conferinta VARCHAR2(50): Titlul conferinței.
        -- sesiuni tip_sesiuni_***: Colecție de sesiuni în ordinea
        -- programului. fiecare sesiune include numele sesiunii și durata
        -- în ore.
        -- nr_zile NUMBER(2): Numărul de zile de desfășurare a
        -- conferinței.
        -- stare VARCHAR2(15): Starea conferinței (valori posibile:
        -- "programata", „in desfasurare", „finalizata").




-----------------------------------CERINTE---------------------------------

--Definirea tipurilor și crearea tabelului conferinței:

--Definiți un tip sesiune_obj ca obiect, care să conțină:
    -- nume_sesiune VARCHAR2(50): Numele sesiunii.
    -- durata NUMBER(2): Durata sesiunii în ore.
    -- Definiți un tip de colecție tip_sesiuni_*** ca NESTED TABLE
    -- de tip sesiune_obj, pe care îl veți folosi în coloana sesiuni din
    -- tabelul program_conferinta_***.




-- Inserarea înregistrărilor:

-- Adăugați 3 înregistrări în tabelul program_conferinta_***,
-- fiecare reprezentând o conferință cu minimum 3 sesiuni.
-- Sesiunile sunt introduse în ordinea desfășurării lor în cadrul
-- conferinței.




-- Pentru o conferință specificată prin codul său:

-- Adăugați o sesiune nouă la sfârșitul programului,
-- specificând numele și durata acesteia.

-- Inversați ordinea de desfășurare între două sesiuni
-- specificate, pe baza numelui fiecărei sesiuni (presupunând
-- că numele sesiunilor sunt unice în cadrul unei conferințe).

-- Eliminați din program o sesiune al cărei nume este dat.
-- Creșteți durata unei sesiuni specifice cu un număr dat de
-- ore (de exemplu, adăugați 1 oră la durata sesiunii).




-- Pentru o conferință identificată prin codul său:

-- Afișați numărul total de sesiuni planificate. Afișați numele
-- sesiunilor ordonate cronologic.




-- Pentru fiecare conferință:

-- Calculați durata totală a tuturor sesiunilor (în ore).

-- Identificați conferințele cu cele mai puține sesiuni (de
-- exemplu, conferințele care au mai puțin de 4 sesiuni).

-- Actualizați starea acestor conferințe la „finalizată” dacă
-- nu au sesiuni programate următoarele doua zile
-- (07.11.2025, 08.11.2025).







-----------------------------------REZOLVARE---------------------------------


-----CREARE------


--tip obiect
CREATE OR REPLACE TYPE sesiune_obj_df AS OBJECT
(
    nume_sesiune VARCHAR2(50),
    durata NUMBER(2)
);


--tip colectie
CREATE OR REPLACE TYPE tip_sesiuni_df AS TABLE OF sesiune_obj_df;


CREATE TABLE program_conferinta_df
(
    cod_conferinta NUMBER(5) PRIMARY KEY,
    titlu_conferinta VARCHAR2(50),
    sesiuni tip_sesiuni_df,
    nr_zile NUMBER(2),
    stare VARCHAR2(15)
)
NESTED TABLE sesiuni STORE AS sesiuni_tabel;





-----INSERARI------


INSERT INTO PROGRAM_CONFERINTA_DF
    (COD_CONFERINTA,TITLU_CONFERINTA, SESIUNI, NR_ZILE, STARE)
VALUES (
        101,
    'Conferinta BD',
    tip_sesiuni_df(
        SESIUNE_OBJ_DF('Intro', 2),
        SESIUNE_OBJ_DF('Join', 3),
        SESIUNE_OBJ_DF('Select', 2)
    ),
    2,
    'programata'
);



INSERT INTO PROGRAM_CONFERINTA_DF
    (COD_CONFERINTA,TITLU_CONFERINTA, SESIUNI, NR_ZILE, STARE)
VALUES (
        102,
    'Conferinta GAL',
    tip_sesiuni_df(
        SESIUNE_OBJ_DF('Mate', 2),
        SESIUNE_OBJ_DF('Geometrie', 3),
        SESIUNE_OBJ_DF('Matrici', 2)
    ),
    1,
    'finalizata'
);


INSERT INTO PROGRAM_CONFERINTA_DF
    (COD_CONFERINTA,TITLU_CONFERINTA, SESIUNI, NR_ZILE, STARE)
VALUES (
        103,
    'Conferinta POO',
    tip_sesiuni_df(
        SESIUNE_OBJ_DF('Intro', 2),
        SESIUNE_OBJ_DF('Clase', 3),
        SESIUNE_OBJ_DF('Horror', 2)
    ),
    1,
    'in desfasurare'
);

commit;




-----APLICATII------


--sesiune noua

INSERT INTO TABLE(SELECT t.sesiuni
                  FROM program_conferinta_df t
                  WHERE t.cod_conferinta = 101)
VALUES (
  sesiune_obj_df('Indexare', 1)
);



--inversare ordine

DECLARE
  v_sesiune_1 sesiune_obj_df;
  v_sesiune_2 sesiune_obj_df;
  v_idx_1 NUMBER;
  v_idx_2 NUMBER;
  v_sesiuni tip_sesiuni_df;

  v_conf_id NUMBER := 101;
  v_nume_1 VARCHAR2(50) := 'Intro';
  v_nume_2 VARCHAR2(50) := 'Join';
BEGIN

  SELECT sesiuni INTO v_sesiuni
  FROM program_conferinta_df
  WHERE cod_conferinta = v_conf_id;

  --gasim pozitiile
  FOR i IN 1..v_sesiuni.COUNT LOOP
    IF v_sesiuni(i).nume_sesiune = v_nume_1 THEN
      v_idx_1 := i;
      v_sesiune_1 := v_sesiuni(i);
    ELSIF v_sesiuni(i).nume_sesiune = v_nume_2 THEN
      v_idx_2 := i;
      v_sesiune_2 := v_sesiuni(i);
    END IF;
  END LOOP;

  --inversam
  IF v_idx_1 IS NOT NULL AND v_idx_2 IS NOT NULL THEN
    v_sesiuni(v_idx_1) := v_sesiune_2;
    v_sesiuni(v_idx_2) := v_sesiune_1;

    --actualizam tabelul
    UPDATE program_conferinta_df
    SET sesiuni = v_sesiuni
    WHERE cod_conferinta = v_conf_id;

  END IF;
END;
/

select * from PROGRAM_CONFERINTA_DF
where COD_CONFERINTA=101



-- Eliminare sesiune

DELETE FROM TABLE(SELECT t.sesiuni
                  FROM program_conferinta_df t
                  WHERE t.cod_conferinta = 101) s
WHERE s.nume_sesiune = 'Select';


select * from PROGRAM_CONFERINTA_DF
where COD_CONFERINTA=101



--crestere durata sesiune

UPDATE TABLE(SELECT t.sesiuni
             FROM program_conferinta_df t
             WHERE t.cod_conferinta = 101) s
SET s.durata = s.durata + 1
WHERE s.nume_sesiune = 'Intro';


select * from PROGRAM_CONFERINTA_DF
where COD_CONFERINTA=101




--sesiuni totale si ord cron

SELECT CARDINALITY(sesiuni) AS "Numar Total Sesiuni"
FROM program_conferinta_df
WHERE cod_conferinta = 102;


SELECT s.nume_sesiune
FROM program_conferinta_df p, TABLE(p.sesiuni) s
WHERE p.cod_conferinta = 102;




--durata sesiunilor

SELECT
  p.cod_conferinta,
  p.titlu_conferinta,
  SUM(s.durata) AS "Durata Totala (ore)"
FROM
  program_conferinta_df p,
  TABLE(p.sesiuni) s
GROUP BY
  p.cod_conferinta, p.titlu_conferinta;




--conferinte cu cele mai putine sesiuni
SELECT titlu_conferinta, CARDINALITY(sesiuni) AS "Nr Sesiuni"
FROM program_conferinta_df
WHERE CARDINALITY(sesiuni) < 4;


--Donea Fernando-Emanuel
--grupa 243

--Lab 5


-----------------------------------CREARE---------------------------------


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





-------------------------------INSERARI-----------------------------


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





------------------------------ APLICATII ------------------------------


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






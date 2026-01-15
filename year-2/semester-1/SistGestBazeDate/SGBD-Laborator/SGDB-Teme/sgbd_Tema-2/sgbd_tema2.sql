--SGBD Tema 2



-- E1. Identificați în diagrama Entitate-Relație utilizată în proiectul prezentat la materia Baze de Date din anul I, o
-- relație din tip many-to-many. Dacă nu aveți o astfel de relație în acest proiect, atunci definiți una folosind
-- tema aleasă în acel proiect:
        -- a. descrieți entitățile și relația dintre acestea;
        -- b.realizați diagrama Entitate-Relație doar pentru această parte din proiect;
        -- c. descrieți modul de transformare al acestei relații în diagrama conceptuală, precizând toate cheile
    -- primare, cheile externe și alte atribute esențiale;

        -- d. realizați diagrama conceptuală doar pentru această parte din proiect;
        -- e. pe baza diagramei conceptuale de la punctul d, definiți în SQL tabelele și toate constrângerile necesare;
        -- f. adaptați una dintre cerințele exercițiilor 4-12 pentru diagrama obținută la punctul d (formulați cerința în
    -- limbaj natural, inserați 5-10 înregistrări în fiecare tabelă utilizată, apoi rezolvați cererea propusă în
    -- SQL).






---------------------------- REZOLVARE----------------------------


--ex e)
--pe baza diagramei conceptuale de la punctul d, definiți în SQL tabelele și toate constrângerile necesare;
CREATE  TABLE ALBUM (
    album_id NUMBER PRIMARY KEY,
    titlu VARCHAR2(50) NOT NULL,
    artist_id NUMBER NOT NULL,
    data_lansare DATE,
    pret NUMBER(6,2) NOT NULL,
    stoc NUMBER(5) DEFAULT 0 NOT NULL,
    rating NUMBER(3,2) CHECK (rating BETWEEN 1.00 AND 5.00),
    descriere VARCHAR2(500),
    numar_piese NUMBER(10) NOT NULL,
    format VARCHAR2(50) DEFAULT 'CD',

    FOREIGN KEY (artist_id) REFERENCES ARTIST(artist_id),
    CONSTRAINT ck_album_format CHECK ( format IN ('CD','DIGITAL') )
);

CREATE TABLE GEN_MUZICAL (
    gen_id NUMBER PRIMARY KEY,
    denumire VARCHAR2(25) NOT NULL,
    descriere VARCHAR(100)
);

CREATE TABLE ALBUM_GEN_MUZICAL (
    album_id NUMBER,
    gen_id NUMBER,

    PRIMARY KEY (album_id, gen_id),
    FOREIGN KEY (album_id) REFERENCES ALBUM(album_id),
    FOREIGN KEY (gen_id) REFERENCES GEN_MUZICAL(gen_id)
);

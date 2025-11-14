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

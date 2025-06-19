--ex 10--

----crearea secventelor----

DROP SEQUENCE seq_utilizator;
DROP SEQUENCE seq_comanda;
DROP SEQUENCE seq_cd_pers;
DROP SEQUENCE seq_playlist;
DROP SEQUENCE seq_recenzie;
DROP SEQUENCE seq_artist;
DROP SEQUENCE seq_genmus;
DROP SEQUENCE seq_melodie;
DROP SEQUENCE seq_wishlist;
DROP SEQUENCE seq_eveniment;
DROP SEQUENCE seq_bilet;


--secventa utilizator--
CREATE SEQUENCE seq_utilizator
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;

--secventa comanda--
CREATE SEQUENCE seq_comanda
START WITH 1000
INCREMENT BY 1
NOCACHE
NOCYCLE;

--secventa cd personalizat--
CREATE SEQUENCE seq_cd_pers
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;

--secventa playlist--
CREATE SEQUENCE seq_playlist
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;

--secventa recenzie--
CREATE SEQUENCE seq_recenzie
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;

--secventa artist--
CREATE SEQUENCE seq_artist
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;

--secventa genmuzical
CREATE SEQUENCE seq_genmus
START WITH 50
INCREMENT BY 50
NOCACHE
NOCYCLE;

--secventa melodie--
CREATE SEQUENCE seq_melodie
START WITH 4000
INCREMENT BY 50
NOCACHE
NOCYCLE;

--secventa wishlist
CREATE SEQUENCE seq_wishlist
START WITH 500
INCREMENT BY 50
NOCACHE
NOCYCLE;

--secventa evenimen--
CREATE SEQUENCE seq_eveniment
START WITH 121
INCREMENT BY 11
NOCACHE
NOCYCLE;

--secventa bilet
CREATE SEQUENCE seq_bilet
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;



--ex 11--

----------Creare tabele principale----------

DROP TABLE PLAYLIST CASCADE CONSTRAINTS;
DROP TABLE LINEUP CASCADE CONSTRAINTS;
DROP TABLE COMANDA_ALBUME CASCADE CONSTRAINTS;
DROP TABLE COMANDA_CD_PERSONALIZAT CASCADE CONSTRAINTS;
DROP TABLE WISHLIST_ALBUM CASCADE CONSTRAINTS;
DROP TABLE ALBUM_GEN_MUZICAL CASCADE CONSTRAINTS;
DROP TABLE BILET CASCADE CONSTRAINTS;
DROP TABLE EVENIMENT CASCADE CONSTRAINTS;
DROP TABLE WISHLIST CASCADE CONSTRAINTS;
DROP TABLE LOIALITATE CASCADE CONSTRAINTS;
DROP TABLE RECENZIE CASCADE CONSTRAINTS;
DROP TABLE COMANDA CASCADE CONSTRAINTS;
DROP TABLE CD_PERSONALIZAT CASCADE CONSTRAINTS;
DROP TABLE MELODIE CASCADE CONSTRAINTS;
DROP TABLE ALBUM CASCADE CONSTRAINTS;
DROP TABLE GEN_MUZICAL CASCADE CONSTRAINTS;
DROP TABLE ARTIST CASCADE CONSTRAINTS;
DROP TABLE UTILIZATOR CASCADE CONSTRAINTS;

CREATE TABLE UTILIZATOR (
    utilizator_id NUMBER PRIMARY KEY,
    nume VARCHAR2(25) NOT NULL,
    prenume VARCHAR2(25) NOT NULL,
    email VARCHAR2(50) NOT NULL,
    parola VARCHAR2(50) NOT NULL,
    telefon NUMBER(15),
    strada VARCHAR2(100),
    numar NUMBER(5),
    oras VARCHAR2(50),
    judet VARCHAR2(50),
    cod_postal NUMBER(20),
    data_inregistrare DATE DEFAULT SYSDATE,
    CONSTRAINT ck_email_format CHECK (email LIKE '%@%.%')
);


CREATE TABLE ARTIST (
    artist_id NUMBER PRIMARY KEY,
    nume VARCHAR2(50) NOT NULL,
    biografie VARCHAR(500)
);


CREATE TABLE GEN_MUZICAL (
    gen_id NUMBER PRIMARY KEY,
    denumire VARCHAR2(25) NOT NULL,
    descriere VARCHAR(100)
);


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


CREATE TABLE MELODIE (
    melodie_id NUMBER PRIMARY KEY,
    titlu VARCHAR2(50) NOT NULL,
    album_id NUMBER NOT NULL,
    durata NUMBER(5) NOT NULL,
    pret_individual NUMBER(5,2) NOT NULL,

    FOREIGN KEY (album_id) REFERENCES ALBUM(album_id)
);


CREATE TABLE CD_PERSONALIZAT(
    cd_pers_id NUMBER PRIMARY KEY,
    utilizator_id NUMBER NOT NULL,
    titlu VARCHAR2(50) NOT NULL,
    data_creare DATE NOT NULL,
    pret_total NUMBER(6,2) NOT NULL,
    numar_piese NUMBER NOT NULL,

    FOREIGN KEY (utilizator_id) REFERENCES UTILIZATOR(utilizator_id),

    CONSTRAINT ck_cd_pers_piese CHECK (numar_piese BETWEEN 5 AND 30)
);


CREATE TABLE COMANDA (
    comanda_id NUMBER PRIMARY KEY,
    utilizator_id NUMBER NOT NULL,
    data_plasare DATE DEFAULT SYSDATE NOT NULL ,
    status VARCHAR2(20) DEFAULT 'Plasată' NOT NULL,
    adresa_livrare VARCHAR(200) NOT NULL,
    metoda_plata VARCHAR2(50) NOT NULL,
    cost_total NUMBER(10,2) NOT NULL,
    cost_transport NUMBER(5,2) NOT NULL,
    tip_comanda VARCHAR2(20) DEFAULT 'STANDARD' NOT NULL,

    FOREIGN KEY (utilizator_id) REFERENCES UTILIZATOR(utilizator_id),

    CONSTRAINT ck_comanda_status CHECK (status IN ('Plasată', 'Procesată', 'Expediată', 'Livrată', 'Anulată')),
    CONSTRAINT ck_comanda_metoda_plata CHECK (metoda_plata IN ('Card', 'Ramburs','Pe caiet')),
    CONSTRAINT ck_comanda_tip CHECK (tip_comanda IN ('STANDARD', 'PERSONALIZAT', 'MIXT'))  --adaugat dupa feedback
);


CREATE TABLE RECENZIE (
    recenzie_id NUMBER PRIMARY KEY,
    utilizator_id NUMBER NOT NULL,
    album_id NUMBER NOT NULL,
    rating NUMBER(1) NOT NULL,
    comentariu VARCHAR2(200),
    data_adaugare DATE NOT NULL,

    FOREIGN KEY (utilizator_id) REFERENCES UTILIZATOR(utilizator_id),
    FOREIGN KEY (album_id) REFERENCES ALBUM(album_id),

    CONSTRAINT ck_recenzie_rating CHECK (rating BETWEEN 1 AND 5),
    CONSTRAINT u_recenzie UNIQUE (utilizator_id, album_id)
);


CREATE TABLE LOIALITATE (
    loialitate_id NUMBER PRIMARY KEY,
    utilizator_id NUMBER NOT NULL,
    puncte NUMBER(10) DEFAULT 0 NOT NULL,
    nivel VARCHAR2(20) DEFAULT 'Bronz' NOT NULL,
    beneficii VARCHAR2(500),

    FOREIGN KEY (utilizator_id) REFERENCES UTILIZATOR(utilizator_id),

    CONSTRAINT ck_loialitate_nivel CHECK (nivel IN ('Bronz', 'Argint', 'Aur', 'Platină')),
    CONSTRAINT u_loialitate UNIQUE (utilizator_id)
);


CREATE TABLE WISHLIST (
    wishlist_id NUMBER PRIMARY KEY,
    utilizator_id NUMBER NOT NULL,

    FOREIGN KEY (utilizator_id) REFERENCES UTILIZATOR(utilizator_id),

    CONSTRAINT u_wishlist UNIQUE (utilizator_id)
);


CREATE TABLE EVENIMENT (
    eveniment_id NUMBER PRIMARY KEY,
    nume VARCHAR2(100) NOT NULL,
    data DATE NOT NULL,
    locatie VARCHAR2(100) NOT NULL,
    capacitate NUMBER(10) NOT NULL,
    descriere VARCHAR2(500)
);


CREATE TABLE BILET (
    bilet_id NUMBER PRIMARY KEY,
    eveniment_id NUMBER NOT NULL,
    pret NUMBER(5,2) NOT NULL,

    FOREIGN KEY (eveniment_id) REFERENCES EVENIMENT(eveniment_id)
);

----------Creare tabele asociative----------

CREATE TABLE ALBUM_GEN_MUZICAL (
    album_id NUMBER,
    gen_id NUMBER,

    PRIMARY KEY (album_id, gen_id),
    FOREIGN KEY (album_id) REFERENCES ALBUM(album_id),
    FOREIGN KEY (gen_id) REFERENCES GEN_MUZICAL(gen_id)
);


CREATE TABLE WISHLIST_ALBUM (
    wishlist_id NUMBER,
    album_id NUMBER,

    PRIMARY KEY (wishlist_id, album_id),
    FOREIGN KEY (wishlist_id) REFERENCES WISHLIST(wishlist_id),
    FOREIGN KEY (album_id) REFERENCES ALBUM(album_id)
);


CREATE TABLE COMANDA_ALBUME (
    comanda_id NUMBER,
    album_id NUMBER,
    cantitate NUMBER(3) DEFAULT 1 NOT NULL,

    PRIMARY KEY (comanda_id, album_id),
    FOREIGN KEY (comanda_id) REFERENCES COMANDA(comanda_id),
    FOREIGN KEY (album_id) REFERENCES ALBUM(album_id)
);

CREATE TABLE COMANDA_CD_PERSONALIZAT (
    comanda_id NUMBER,
    cd_pers_id NUMBER,
    cantitate NUMBER(3) DEFAULT 1 NOT NULL,

    PRIMARY KEY (comanda_id, cd_pers_id),
    FOREIGN KEY (comanda_id) REFERENCES COMANDA(comanda_id),
    FOREIGN KEY (cd_pers_id) REFERENCES CD_PERSONALIZAT(cd_pers_id)
);


CREATE TABLE PLAYLIST (
    playlist_id NUMBER PRIMARY KEY,
    melodie_id NUMBER NOT NULL,
    cd_pers_id NUMBER NOT NULL,

    FOREIGN KEY (melodie_id) REFERENCES MELODIE(melodie_id),
    FOREIGN KEY (cd_pers_id) REFERENCES CD_PERSONALIZAT(cd_pers_id)
);


CREATE TABLE LINEUP (
    lineup_id NUMBER PRIMARY KEY,
    artist_id NUMBER NOT NULL,
    eveniment_id NUMBER NOT NULL,

    FOREIGN KEY (artist_id) REFERENCES ARTIST(artist_id),
    FOREIGN KEY (eveniment_id) REFERENCES EVENIMENT(eveniment_id),
    CONSTRAINT u_lineup UNIQUE (artist_id, eveniment_id)
);




----------inserarea datelor in tabela UTILIZATOR----------

INSERT INTO UTILIZATOR (utilizator_id, nume, prenume,
                        email, parola, telefon,
                        strada, numar, oras, judet, cod_postal,
                        data_inregistrare)
VALUES (seq_utilizator.NEXTVAL, 'Dan', 'Fernando',
        'fernandodan@gmail.com', 'parolaparola','0767601625',
        'Str. Lalelelor', 23, 'Roman','Neamt',617466,
        TO_DATE('2020-01-15', 'YYYY-MM-DD'));


INSERT INTO UTILIZATOR (utilizator_id, nume, prenume,
                        email, parola, telefon,
                        strada, numar, oras, judet, cod_postal,
                        data_inregistrare)
VALUES (seq_utilizator.NEXTVAL, 'Popescu', 'Vlad',
        'popescuvlad22@outlook.com', 'parola456', '07787617823',
        'Str. Libertății', 15, 'Cluj-Napoca', 'Cluj', 400000,
        TO_DATE('2023-02-22', 'YYYY-MM-DD'));



INSERT INTO UTILIZATOR (utilizator_id, nume, prenume,
                        email, parola, telefon,
                        strada, numar, oras, judet, cod_postal,
                        data_inregistrare)
VALUES (seq_utilizator.NEXTVAL, 'Bejenescu', 'Cosmin',
        'cosmin_beje@yahoo.com', 'parola789', '0745678901',
        'Spl. Independentei', 68, 'Bucuresti', 'Bucuresti', 700000,
        TO_DATE('2021-03-18', 'YYYY-MM-DD'));


INSERT INTO UTILIZATOR (utilizator_id, nume, prenume,
                        email, parola, telefon,
                        strada, numar, oras, judet, cod_postal,
                        data_inregistrare)
VALUES (seq_utilizator.NEXTVAL, 'Tudor', 'Arghezi',
        'tudor_arghezi@gmail.com', 'parola012', '0756789012',
        'Str. Tudor Arghezi', 25, 'Iasi', 'Iasi', 300000,
        TO_DATE('2023-04-05', 'YYYY-MM-DD'));


INSERT INTO UTILIZATOR (utilizator_id, nume, prenume,
                        email, parola, telefon,
                        strada, numar, oras, judet, cod_postal,
                        data_inregistrare)
VALUES (seq_utilizator.NEXTVAL, 'Dumitrescu', 'Andrei',
        'andrei.dumitrescu@gmail.com', 'parola345', '0767890123',
        'Str. Avram Iancu', 30, 'Brașov', 'Brașov', 500000,
        TO_DATE('2023-05-12', 'YYYY-MM-DD'));



----------inserarea datelor in tabela ARTIST----------
INSERT INTO ARTIST (artist_id, nume, biografie)
VALUES (seq_artist.NEXTVAL, 'Queen', 'Formație britanică de rock înființată în 1970 la Londra, având ca membri pe Freddie Mercury, Brian May, Roger Taylor și John Deacon.');
INSERT INTO ARTIST (artist_id, nume, biografie)
VALUES (seq_artist.NEXTVAL, 'Taylor Swift', 'Cântăreață și compozitoare americană, cunoscută pentru versurile sale narative și pentru succesul în muzica pop și country.');
INSERT INTO ARTIST (artist_id, nume, biografie)
VALUES (seq_artist.NEXTVAL, 'Kendrick Lamar', 'Rapper, compozitor și producător american, recunoscut pentru versurile sale complexe și impactul asupra culturii hip-hop.');
INSERT INTO ARTIST (artist_id, nume, biografie)
VALUES (seq_artist.NEXTVAL, 'Daft Punk', 'Duo francez de muzică electronică, format din Guy-Manuel de Homem-Christo și Thomas Bangalter, cunoscuți pentru influența lor în muzica dance.');
INSERT INTO ARTIST (artist_id, nume, biografie)
VALUES (seq_artist.NEXTVAL, 'Metallica', 'Formație americană de heavy metal, fondată în 1981, cunoscută pentru albumele lor influente și spectacolele live energice.');



----------Inserarea datelor în tabela GEN_MUZICAL----------
INSERT INTO GEN_MUZICAL (gen_id, denumire, descriere)
VALUES (seq_genmus.NEXTVAL, 'Rock', 'Gen muzical popular caracterizat prin utilizarea chitării electrice și a tobelor.');

INSERT INTO GEN_MUZICAL (gen_id, denumire, descriere)
VALUES (seq_genmus.NEXTVAL, 'Pop','Gen muzical comercial caracterizat prin melodii accesibile și structuri simple dar captivante.');

INSERT INTO GEN_MUZICAL (gen_id, denumire, descriere)
VALUES (seq_genmus.NEXTVAL, 'Hip-Hop','Gen muzical urban ce îmbină ritmuri puternice cu versuri rap și elemente de scratching.');

INSERT INTO GEN_MUZICAL (gen_id, denumire, descriere)
VALUES (seq_genmus.NEXTVAL, 'Electronic','Gen muzical bazat pe sunete produse electronic, sintetizatoare și beat-uri programate.');

INSERT INTO GEN_MUZICAL (gen_id, denumire, descriere)
VALUES (seq_genmus.NEXTVAL, 'Heavy-Metal','Gen muzical intens caracterizat prin chitare distorsionate, tobe puternice și vocale expresive.');




----------Inserarea datelor în tabela ALBUM----------

INSERT INTO ALBUM (album_id, titlu, artist_id, data_lansare, pret, stoc, rating, descriere, numar_piese, format)
VALUES(8, 'Hot Space', 1, TO_DATE('1982-05-21', 'YYYY-MM-DD'), 29.99, 40, 3.5, 'Album funk/pop', 11, 'CD');

INSERT INTO ALBUM (album_id, titlu, artist_id, data_lansare, pret, stoc, rating, descriere, numar_piese, format)
VALUES (1, 'To Pimp a Butterfly', 2, TO_DATE('2015-03-15', 'YYYY-MM-DD'), 49.99, 100, 4.8, 'Album hip-hop revolutionar',16, 'CD');

INSERT INTO ALBUM (album_id, titlu, artist_id, data_lansare, pret, stoc, rating, descriere, numar_piese, format)
VALUES (2, 'good kid, m.A.A.d city', 2, TO_DATE('2012-10-22', 'YYYY-MM-DD'), 44.99, 75, 4.7,'Album conceptual despre viata in Compton', 12, 'CD');

INSERT INTO ALBUM (album_id, titlu, artist_id, data_lansare, pret, stoc, rating, descriere, numar_piese, format)
VALUES (3, 'DAMN.', 2, TO_DATE('2017-04-14', 'YYYY-MM-DD'), 39.99, 150, 4.6, 'Album castigator premiul Pulitzer', 14, 'CD');

INSERT INTO ALBUM (album_id, titlu, artist_id, data_lansare, pret, stoc, rating, descriere, numar_piese, format)
VALUES (4, 'Folklore', 3, TO_DATE('2020-07-24', 'YYYY-MM-DD'), 34.99, 200, 4.5, 'Album indie folk', 16, 'DIGITAL');

INSERT INTO ALBUM (album_id, titlu, artist_id, data_lansare, pret, stoc, rating, descriere, numar_piese, format)
VALUES (5, 'Evermore', 3, TO_DATE('2020-12-11', 'YYYY-MM-DD'), 34.99, 180, 4.4, 'Album sora pentru Folklore', 15,'DIGITAL');

INSERT INTO ALBUM (album_id, titlu, artist_id, data_lansare, pret, stoc, rating, descriere, numar_piese, format)
VALUES(6, 'Random Access Memories', 4, TO_DATE('2013-05-17', 'YYYY-MM-DD'), 54.99, 90, 4.9, 'Album dance electronic', 13, 'CD');

INSERT INTO ALBUM (album_id, titlu, artist_id, data_lansare, pret, stoc, rating, descriere, numar_piese, format)
VALUES(7, 'Discovery', 4, TO_DATE('2001-03-12', 'YYYY-MM-DD'), 49.99, 60, 4.8, 'Album house futuristic', 14, 'CD');

INSERT INTO ALBUM (album_id, titlu, artist_id, data_lansare, pret, stoc, rating, descriere, numar_piese, format)
VALUES(9, 'Master of Puppets', 5, TO_DATE('1986-03-03', 'YYYY-MM-DD'), 44.99, 120, 5.0, 'Album thrash metal clasic', 8,'CD');

INSERT INTO ALBUM (album_id, titlu, artist_id, data_lansare, pret, stoc, rating, descriere, numar_piese, format)
VALUES (10, 'Ride the Lightning', 5, TO_DATE('1984-07-27', 'YYYY-MM-DD'), 44.99, 100, 4.9, 'Al doilea album Metallica',8, 'CD');





----------Inserarea datelor în tabela MELODIE----------

-- Folklore
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'cardigan', 4, 239, 3.99);
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'exile', 4, 275, 3.99);
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'the 1', 4, 211, 3.99);


-- Evermore
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'willow', 5, 214, 3.99);
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'champagne problems', 5, 245, 3.99);
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'gold rush', 5, 187, 3.99);


-- To Pimp a Butterfly
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'Alright', 1, 215, 3.99);
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'King Kunta', 1, 234, 3.99);
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'The Blacker the Berry', 1, 335, 3.99);

-- Good Kid, M.A.A.D City
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'Swimming Pools (Drank)', 2, 244, 3.99);
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'Bitch, Dont Kill My Vibe', 2, 292, 3.99);
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'Backseat Freestyle', 2, 233, 3.99);


-- DAMN.
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'HUMBLE.', 3, 177, 3.99);
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'DNA.', 3, 185, 3.99);
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'LOYALTY.', 3, 244, 3.99);


-- Random Access Memories
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'Get Lucky', 6, 369, 3.99);
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'Instant Crush', 6, 337, 3.99);
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'Lose Yourself to Dance', 6, 337, 3.99);


-- Discovery
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'One More Time', 7, 320, 3.99);
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'Digital Love', 7, 300, 3.99);
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'Harder, Better, Faster, Stronger', 7, 224, 3.99);


-- Master of Puppets
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'Master of Puppets', 9, 515, 3.99);
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'Battery', 9, 312, 3.99);
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'Welcome Home (Sanitarium)', 9, 386, 3.99);


-- Ride the Lightning
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'Fade to Black', 10, 417, 3.99);
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'For Whom the Bell Tolls', 10, 305, 3.99);
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'Creeping Death', 10, 396, 3.99);


-- Hot Space
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'Under Pressure', 8, 243, 3.99);
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'Las Palabras de Amor', 8, 256, 3.99);
INSERT INTO MELODIE (melodie_id, titlu, album_id, durata, pret_individual) VALUES (seq_melodie.NEXTVAL, 'Staying Power', 8, 246, 3.99);


----------Inserarea datelor în tabela CD PERSONALIZAT----------

INSERT INTO CD_PERSONALIZAT (cd_pers_id, utilizator_id, titlu, data_creare, pret_total, numar_piese)
VALUES (seq_cd_pers.NEXTVAL, 1, 'Colecția Mea Rock', TO_DATE('2022-05-10', 'YYYY-MM-DD'), 24.95, 5);

INSERT INTO CD_PERSONALIZAT (cd_pers_id, utilizator_id, titlu, data_creare, pret_total, numar_piese)
VALUES (seq_cd_pers.NEXTVAL, 2, 'Hiturile Vechi', TO_DATE('2023-02-11', 'YYYY-MM-DD'), 29.95, 6);

INSERT INTO CD_PERSONALIZAT (cd_pers_id, utilizator_id, titlu, data_creare, pret_total, numar_piese)
VALUES (seq_cd_pers.NEXTVAL, 3, 'Cele Mai Bune Balade', TO_DATE('2024-1-12', 'YYYY-MM-DD'), 34.95, 7);

INSERT INTO CD_PERSONALIZAT (cd_pers_id, utilizator_id, titlu, data_creare, pret_total, numar_piese)
VALUES (seq_cd_pers.NEXTVAL, 4, 'Pop Mix', TO_DATE('2025-05-01', 'YYYY-MM-DD'), 39.95, 8);

INSERT INTO CD_PERSONALIZAT (cd_pers_id, utilizator_id, titlu, data_creare, pret_total, numar_piese)
VALUES (seq_cd_pers.NEXTVAL, 5, 'Muzica de cartier', TO_DATE('2024-05-14', 'YYYY-MM-DD'), 44.95, 9);





----------Inserarea datelor în tabela COMANDA----------

INSERT INTO COMANDA (comanda_id, utilizator_id, data_plasare, status, adresa_livrare, metoda_plata, cost_total, cost_transport, tip_comanda)
VALUES (seq_comanda.NEXTVAL, 1, TO_DATE('2022-01-01', 'YYYY-MM-DD'), 'Livrată', 'Str. Lalelelor nr. 23, Roman, Neamt, 617466', 'Card', 129.93, 15.00, 'MIXT');

INSERT INTO COMANDA (comanda_id, utilizator_id, data_plasare, status, adresa_livrare, metoda_plata, cost_total, cost_transport, tip_comanda)
VALUES (seq_comanda.NEXTVAL, 2, TO_DATE('2021-05-02', 'YYYY-MM-DD'), 'Procesată', 'Str. Libertății, nr. 15, Cluj-Napoca, Cluj, 400000', 'Ramburs', 94.94, 15.00, 'MIXT');

INSERT INTO COMANDA (comanda_id, utilizator_id, data_plasare, status, adresa_livrare, metoda_plata, cost_total, cost_transport, tip_comanda)
VALUES (seq_comanda.NEXTVAL, 3, TO_DATE('2020-12-03', 'YYYY-MM-DD'), 'Expediată', 'Spl. Independentei, nr. 68, Bucuresti, Bucuresti, 700000', 'Card', 93.98, 15.00, 'STANDARD');

INSERT INTO COMANDA (comanda_id, utilizator_id, data_plasare, status, adresa_livrare, metoda_plata, cost_total, cost_transport, tip_comanda)
VALUES (seq_comanda.NEXTVAL, 4, TO_DATE('2024-08-23', 'YYYY-MM-DD'), 'Plasată', 'Str. Tudor Arghezi, nr. 23, Iasi, Iasi, 300000', 'Card', 94.93, 15.00, 'MIXT');

INSERT INTO COMANDA (comanda_id, utilizator_id, data_plasare, status, adresa_livrare, metoda_plata, cost_total, cost_transport, tip_comanda)
VALUES (seq_comanda.NEXTVAL, 5, TO_DATE('2025-05-01', 'YYYY-MM-DD'), 'Anulată', 'Str. Avram Iancu nr. 30, Brașov, Brasov, 500000', 'Ramburs', 84.94, 15.00, 'STANDARD');





----------Inserarea datelor în tabela RECENZIE----------

INSERT INTO RECENZIE (recenzie_id, utilizator_id, album_id, rating, comentariu, data_adaugare)
VALUES (seq_recenzie.NEXTVAL, 1, 3, 5, 'Album extraordinar! Damn. este capodoperă.', TO_DATE('2024-05-06', 'YYYY-MM-DD'));

INSERT INTO RECENZIE (recenzie_id, utilizator_id, album_id, rating, comentariu, data_adaugare)
VALUES (seq_recenzie.NEXTVAL, 2, 9, 3, 'Nice!', TO_DATE('2024-05-07', 'YYYY-MM-DD'));

INSERT INTO RECENZIE (recenzie_id, utilizator_id, album_id, rating, comentariu, data_adaugare)
VALUES (seq_recenzie.NEXTVAL, 3, 1, 4, 'Unul dintre cele mai bune albume ale lui Kendrick.', TO_DATE('2024-05-08', 'YYYY-MM-DD'));

INSERT INTO RECENZIE (recenzie_id, utilizator_id, album_id, rating, comentariu, data_adaugare)
VALUES (seq_recenzie.NEXTVAL, 4, 5, 5, 'Vocea lui Taylor Swift este incredibilă. Albumul m-a emoționat profund.', TO_DATE('2024-05-09', 'YYYY-MM-DD'));

INSERT INTO RECENZIE (recenzie_id, utilizator_id, album_id, rating, comentariu, data_adaugare)
VALUES (seq_recenzie.NEXTVAL, 5, 6, 4, 'Daft Punk este un artist complet. Instant Crush este piesa mea preferată.', TO_DATE('2024-05-10', 'YYYY-MM-DD'));



----------Inserarea datelor în tabela LOIALITATE----------

INSERT INTO LOIALITATE (loialitate_id, utilizator_id, puncte, nivel, beneficii)
VALUES (1, 1, 500, 'Argint', '10% reducere la transportul comenzilor');

INSERT INTO LOIALITATE (loialitate_id, utilizator_id, puncte, nivel, beneficii)
VALUES (2, 2, 200, 'Bronz', '5% reducere la transportul comenzilor');

INSERT INTO LOIALITATE (loialitate_id, utilizator_id, puncte, nivel, beneficii)
VALUES (3, 3, 800, 'Aur', '15% reducere la transportul comenzilor, acces prioritar la ediții limitate');

INSERT INTO LOIALITATE (loialitate_id, utilizator_id, puncte, nivel, beneficii)
VALUES (4, 4, 1200, 'Platină', '20% reducere la transportul comenzilor, acces prioritar la ediții limitate, invitații la evenimente');

INSERT INTO LOIALITATE (loialitate_id, utilizator_id, puncte, nivel, beneficii)
VALUES (5, 5, 100, 'Bronz', '5% reducere la transportul comenzilor');




----------Inserarea datelor în tabela WISHLIST----------

INSERT INTO WISHLIST (wishlist_id, utilizator_id)
VALUES (seq_wishlist.NEXTVAL, 1);

INSERT INTO WISHLIST (wishlist_id, utilizator_id)
VALUES (seq_wishlist.NEXTVAL, 2);

INSERT INTO WISHLIST (wishlist_id, utilizator_id)
VALUES (seq_wishlist.NEXTVAL, 3);

INSERT INTO WISHLIST (wishlist_id, utilizator_id)
VALUES (seq_wishlist.NEXTVAL, 4);

INSERT INTO WISHLIST (wishlist_id, utilizator_id)
VALUES (seq_wishlist.NEXTVAL, 5);



----------Inserarea datelor în tabela EVENIMENT----------

INSERT INTO EVENIMENT (eveniment_id, nume, data, locatie, capacitate, descriere)
VALUES (seq_eveniment.NEXTVAL, 'Old rock', TO_DATE('2025-05-11', 'YYYY-MM-DD'), 'Sala Palatului, București', 4000, 'Concert tribut pentru legendara trupă Queen');

INSERT INTO EVENIMENT (eveniment_id, nume, data, locatie, capacitate, descriere)
VALUES (seq_eveniment.NEXTVAL, 'Youth Festival', TO_DATE('2022-07-20', 'YYYY-MM-DD'), 'Arena Națională, București', 55000, 'Festival cu artiști internaționali de top');

INSERT INTO EVENIMENT (eveniment_id, nume, data, locatie, capacitate, descriere)
VALUES (seq_eveniment.NEXTVAL, 'Rock-Metal Summer Fest', TO_DATE('2024-08-10', 'YYYY-MM-DD'), 'Cluj Arena, Cluj-Napoca', 30000, 'Festival de rock cu ');

INSERT INTO EVENIMENT (eveniment_id, nume, data, locatie, capacitate, descriere)
VALUES (seq_eveniment.NEXTVAL, 'Urban Festival', TO_DATE('2024-09-05', 'YYYY-MM-DD'), 'Teatrul Național, Iași', 800, 'Sesiune urban session cu artiștul Kendrick');

INSERT INTO EVENIMENT (eveniment_id, nume, data, locatie, capacitate, descriere)
VALUES (seq_eveniment.NEXTVAL, 'Electronic Dance Night', TO_DATE('2024-10-31', 'YYYY-MM-DD'), 'Berăria H, București', 2000, 'Noapte de muzică electronică cu DJ celebri');


----------Inserarea datelor în tabela Bilet----------

INSERT INTO BILET (bilet_id, eveniment_id, pret)
VALUES (seq_bilet.NEXTVAL, 121, 150.00);

INSERT INTO BILET (bilet_id, eveniment_id, pret)
VALUES (seq_bilet.NEXTVAL, 132, 250.00);

INSERT INTO BILET (bilet_id, eveniment_id, pret)
VALUES (seq_bilet.NEXTVAL, 143, 200.00);

INSERT INTO BILET (bilet_id, eveniment_id, pret)
VALUES (seq_bilet.NEXTVAL, 154, 100.00);

INSERT INTO BILET (bilet_id, eveniment_id, pret)
VALUES (seq_bilet.NEXTVAL, 165, 120.00);





----------Inserarea datelor în tabela ALBUM_GEN_MUZICAL----------

INSERT INTO ALBUM_GEN_MUZICAL (album_id, gen_id) VALUES (1, 150); -- To Pimp a Butterfly - Hip-Hop
INSERT INTO ALBUM_GEN_MUZICAL (album_id, gen_id) VALUES (2, 150); -- good kid, m.A.A.d city - Hip-Hop
INSERT INTO ALBUM_GEN_MUZICAL (album_id, gen_id) VALUES (3, 150); -- DAMN. - Hip-Hop
INSERT INTO ALBUM_GEN_MUZICAL (album_id, gen_id) VALUES (4, 100); -- Folklore - Pop
INSERT INTO ALBUM_GEN_MUZICAL (album_id, gen_id) VALUES (5, 100); -- Evermore - Pop
INSERT INTO ALBUM_GEN_MUZICAL (album_id, gen_id) VALUES (6, 200); -- Random Access Memories - Electronic
INSERT INTO ALBUM_GEN_MUZICAL (album_id, gen_id) VALUES (7, 200); -- Discovery - Electronic
INSERT INTO ALBUM_GEN_MUZICAL (album_id, gen_id) VALUES (8, 50);  -- Hot Space - Rock
INSERT INTO ALBUM_GEN_MUZICAL (album_id, gen_id) VALUES (9, 250); -- Master of Puppets - Heavy-Metal
INSERT INTO ALBUM_GEN_MUZICAL (album_id, gen_id) VALUES (10, 250); -- Ride the Lightning - Heavy-Metal
INSERT INTO ALBUM_GEN_MUZICAL (album_id, gen_id) VALUES (8, 100); -- Hot Space - Pop
INSERT INTO ALBUM_GEN_MUZICAL (album_id, gen_id) VALUES (6, 100); -- Random Access Memories - Pop



----------Inserarea datelor în tabela WISHLIST_ALBUM----------

INSERT INTO WISHLIST_ALBUM (wishlist_id, album_id) VALUES (500, 1); -- Utilizatorul 1 - To Pimp a Butterfly
INSERT INTO WISHLIST_ALBUM (wishlist_id, album_id) VALUES (500, 6); -- Utilizatorul 1 - Random Access Memories
INSERT INTO WISHLIST_ALBUM (wishlist_id, album_id) VALUES (500, 9); -- Utilizatorul 1 - Master of Puppets
INSERT INTO WISHLIST_ALBUM (wishlist_id, album_id) VALUES (550, 4); -- Utilizatorul 2 - Folklore
INSERT INTO WISHLIST_ALBUM (wishlist_id, album_id) VALUES (550, 5); -- Utilizatorul 2 - Evermore
INSERT INTO WISHLIST_ALBUM (wishlist_id, album_id) VALUES (550, 7); -- Utilizatorul 2 - Discovery
INSERT INTO WISHLIST_ALBUM (wishlist_id, album_id) VALUES (600, 2); -- Utilizatorul 3 - good kid, m.A.A.d city
INSERT INTO WISHLIST_ALBUM (wishlist_id, album_id) VALUES (600, 3); -- Utilizatorul 3 - DAMN.
INSERT INTO WISHLIST_ALBUM (wishlist_id, album_id) VALUES (650, 8); -- Utilizatorul 4 - Hot Space
INSERT INTO WISHLIST_ALBUM (wishlist_id, album_id) VALUES (650, 10); -- Utilizatorul 4 - Ride the Lightning



----------Inserarea datelor în tabela COMANDA_ALBUME----------

INSERT INTO COMANDA_ALBUME (comanda_id, album_id, cantitate) VALUES (1000, 1, 1);
INSERT INTO COMANDA_ALBUME (comanda_id, album_id, cantitate) VALUES (1000, 6, 2);
INSERT INTO COMANDA_ALBUME (comanda_id, album_id, cantitate) VALUES (1001, 4, 1);
INSERT INTO COMANDA_ALBUME (comanda_id, album_id, cantitate) VALUES (1001, 5, 1);
INSERT INTO COMANDA_ALBUME (comanda_id, album_id, cantitate) VALUES (1002, 1, 4);
INSERT INTO COMANDA_ALBUME (comanda_id, album_id, cantitate) VALUES (1002, 2, 1);
INSERT INTO COMANDA_ALBUME (comanda_id, album_id, cantitate) VALUES (1003, 7, 1);
INSERT INTO COMANDA_ALBUME (comanda_id, album_id, cantitate) VALUES (1003, 8, 1);
INSERT INTO COMANDA_ALBUME (comanda_id, album_id, cantitate) VALUES (1004, 9, 1);
INSERT INTO COMANDA_ALBUME (comanda_id, album_id, cantitate) VALUES (1004, 3, 1);
INSERT INTO COMANDA_ALBUME (comanda_id, album_id, cantitate) VALUES (1002, 8, 1);
INSERT INTO COMANDA_ALBUME (comanda_id, album_id, cantitate) VALUES (1001, 1, 1);






----------Inserarea datelor în tabela COMANDA_CD_PERSONALIZAT----------

INSERT INTO COMANDA_CD_PERSONALIZAT (comanda_id, cd_pers_id, cantitate)
VALUES (1000, 1, 1); -- Fernando comandă "Colecția Mea Rock"

INSERT INTO COMANDA_CD_PERSONALIZAT (comanda_id, cd_pers_id, cantitate)
VALUES (1001, 2, 1); -- Vlad comandă "Hiturile Vechi"

INSERT INTO COMANDA_CD_PERSONALIZAT (comanda_id, cd_pers_id, cantitate)
VALUES (1003, 3, 2); -- Tudor comandă "Cele Mai Bune Balade"

INSERT INTO COMANDA_CD_PERSONALIZAT (comanda_id, cd_pers_id, cantitate)
VALUES (1004, 3, 1); -- Cosmin comandă "Cele Mai Bune Balade"






----------Inserarea datelor în tabela PLAYLIST----------

INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 5350, 1); -- Master of Puppets
INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 5450, 1); -- Fade to Black
INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 5300, 1); -- Under Pressure
INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 5350, 1); -- Las Palabras de Amor
INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 5400, 1); -- Staying Power


INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 5050, 2); -- One More Time
INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 5300, 2); -- Under Pressure
INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 5450, 2); -- Fade to Black
INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 5350, 2); -- Master of Puppets
INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 5400, 2); -- Battery
INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 5050, 2); -- One More Time


INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 4050, 3); -- cardigan
INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 4100, 3); -- exile
INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 4250, 3); -- champagne problems
INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 5450, 3); -- Fade to Black
INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 5100, 3); -- Digital Love



INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 4050, 4); -- cardigan
INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 4100, 4); -- exile
INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 4150, 4); -- the 1
INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 4200, 4); -- willow
INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 4250, 4); -- champagne problems
INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 4300, 4); -- gold rush


INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 4350, 5); -- Alright
INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 4400, 5); -- King Kunta
INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 4450, 5); -- The Blacker the Berry
INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 4500, 5); -- Swimming Pools (Drank)
INSERT INTO PLAYLIST (playlist_id, melodie_id, cd_pers_id) VALUES (seq_playlist.NEXTVAL, 4550, 5); -- Bitch, Don't Kill My Vibe





----------Inserarea datelor în tabela LINEUP----------

INSERT INTO LINEUP (lineup_id, artist_id, eveniment_id) VALUES (1, 1, 121);  -- Queen la "Old rock"
INSERT INTO LINEUP (lineup_id, artist_id, eveniment_id) VALUES (2, 2, 132);  -- Taylor Swift la "Youth Festival"
INSERT INTO LINEUP (lineup_id, artist_id, eveniment_id) VALUES (3, 5, 143);  -- Metallica la "Rock-Metal Summer Fest"
INSERT INTO LINEUP (lineup_id, artist_id, eveniment_id) VALUES (4, 1, 143);  -- Queen la "Rock-Metal Summer Fest"
INSERT INTO LINEUP (lineup_id, artist_id, eveniment_id) VALUES (5, 3, 154);  -- Kendrick Lamar la "Urban Festival"
INSERT INTO LINEUP (lineup_id, artist_id, eveniment_id) VALUES (6, 4, 165);  -- Daft Punk la "Electronic Dance Night"
INSERT INTO LINEUP (lineup_id, artist_id, eveniment_id) VALUES (9, 3, 132);  -- Kendrick Lamar la "Youth Festival"
INSERT INTO LINEUP (lineup_id, artist_id, eveniment_id) VALUES (10, 4, 132); -- Daft Punk la "Youth Festival"

commit;





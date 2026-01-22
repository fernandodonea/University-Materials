# Intrebari Proiect SGBD


## Sintaxa
### Operatii simple sql

#### a. Crearea unui tabel
```sql
CREATE TABLE ANGAJAT 
(
    id_anagajat NUMBER(5) PRIMARY KEY,
    nume VARCHAR2(256),
    salariu NUMBER(5),
    data_angajari DATE DEFAULT SYSDATE
)
```

#### b. Inserari
```sql
INSERT INTO ANGAJAT 
VALUES (1,'POPESCU',1000);
```

#### c. Actualizarea datelor
```sql
UPDATE ANGAJAT
SET salariu = 500
WHERE id_angajat = 2;

``` 

#### d. Stergere
```sql
DELETE FROM ANGAJAT
WHERE id_angajat = 5;

``` 

#### e. Modificarea tabelului
```sql
ALTER TABLE ANGAJAT
ADD email VARCHAR2(100);

ALTER TABLE ANGAJAT
MODIFY email VARCHAR2(256);

ALTER TABLE ANGAJAT
DROP COLUMN email;
``` 


#### f. Comentariu 
```sql
COMMENT ON COLUMN ANGAJAT.SALARIU IS 'Salariu brut al angajatului';
``` 




### 2. Tipuri de Date PL/SQL (Colecții și Record)

Acestea se declară în secțiunea DECLARE a unui bloc anonim sau într-un pachet.

```sql
DECLARE
    -- A. RECORD (Structură personalizată similară unui rând de tabel)
    TYPE t_angajat_rec IS RECORD (
        id   NUMBER,
        nume VARCHAR2(50)
    );
    v_angajat t_angajat_rec; -- Instanțiere

    -- B. INDEX-BY TABLE (Associative Array)
    -- Nu are limită, nu se stochează în BD, indexare flexibilă (int sau string)
    -- NU are nevoie de constructor!
    TYPE t_index_list IS TABLE OF VARCHAR2(100) INDEX BY PLS_INTEGER;
    v_lista_idx t_index_list; 

    -- C. NESTED TABLE
    -- Dinamic, poate fi stocat în BD, indexare 1..n
    -- NECESITĂ constructor pentru inițializare!
    TYPE t_nested_list IS TABLE OF VARCHAR2(100);
    v_lista_nest t_nested_list := t_nested_list(); -- Constructor gol

    -- D. VARRAY (Variable-Size Array)
    -- Dimensiune maximă fixă, stocat în BD, dens
    -- NECESITĂ constructor!
    TYPE t_varray_list IS VARRAY(10) OF VARCHAR2(100);
    v_lista_varr t_varray_list := t_varray_list(); -- Constructor gol

BEGIN
    -- Utilizare
    v_angajat.id := 10;
    v_angajat.nume := 'Ana';
    
    v_lista_idx(1) := 'Element Index'; -- Atribuire directă
    
    v_lista_nest.EXTEND; -- Nested are nevoie de alocare spațiu
    v_lista_nest(1) := 'Element Nested';
    
    v_lista_varr.EXTEND; -- Varray are nevoie de alocare spațiu
    v_lista_varr(1) := 'Element Varray';
END;
/
```
### 3. Subprograme și Cursori

#### A. Procedură (Stocată)

Nu returnează valoare direct (folosește parametri OUT).

```SQL
CREATE OR REPLACE PROCEDURE mareste_salariu (
    p_id_angajat IN NUMBER,       -- Parametru de intrare
    p_procent    IN NUMBER,
    p_salariu_nou OUT NUMBER      -- Parametru de ieșire
) IS
BEGIN
    UPDATE angajati 
    SET salariu = salariu * (1 + p_procent/100)
    WHERE id_angajat = p_id_angajat
    RETURNING salariu INTO p_salariu_nou;
    
    COMMIT; -- Opțional, depinde de logică
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Angajatul nu există.');
END;
/
```
#### B. Funcție

Trebuie să returneze o valoare. Poate fi folosită în SELECT.

```SQL
CREATE OR REPLACE FUNCTION calculeaza_bonus (
    p_salariu IN NUMBER
) RETURN NUMBER IS 
    v_bonus NUMBER;
BEGIN
    IF p_salariu > 5000 THEN
        v_bonus := 1000;
    ELSE
        v_bonus := 500;
    END IF;
    RETURN v_bonus;
END;
/
```

#### C. Trigger (Declanșator)

Exemplu: Trigger la nivel de rând (FOR EACH ROW) pentru auto-increment sau validare.

```SQL
CREATE OR REPLACE TRIGGER trg_verificare_salariu
BEFORE INSERT OR UPDATE ON angajati
FOR EACH ROW
BEGIN
    IF :NEW.salariu < 3000 THEN
        RAISE_APPLICATION_ERROR(-20001, 'Salariul minim este 3000!');
    END IF;
    -- :NEW referă noua valoare, :OLD referă vechea valoare (la update/delete)
END;
/
```

#### D. Cursori

1. Cursor Implicit Orice SELECT ... INTO sau DML este un cursor implicit. Atribute: SQL%ROWCOUNT, SQL%FOUND.

```SQL
BEGIN
    UPDATE angajati SET salariu = salariu + 100 WHERE id_angajat = 999;
    
    IF SQL%ROWCOUNT = 0 THEN
        DBMS_OUTPUT.PUT_LINE('Niciun rând actualizat.');
    END IF;
END;
/
```
2. Cursor Explicit (Static) Definit în zona de declarare. Necesită OPEN, FETCH, CLOSE (sau FOR cursor).

```SQL
DECLARE
    CURSOR c_angajati IS 
        SELECT nume FROM angajati WHERE salariu > 4000;
    v_nume angajati.nume%TYPE;
BEGIN
    OPEN c_angajati;
    LOOP
        FETCH c_angajati INTO v_nume;
        EXIT WHEN c_angajati%NOTFOUND;
        DBMS_OUTPUT.PUT_LINE(v_nume);
    END LOOP;
    CLOSE c_angajati;
END;
/
```
3. Cursor Explicit Parametrizat Primește argumente la deschidere.

```SQL
DECLARE
    CURSOR c_dept (p_salariu_min NUMBER) IS 
        SELECT nume FROM angajati WHERE salariu >= p_salariu_min;
BEGIN
    -- Se poate deschide cu valori diferite
    FOR r IN c_dept(5000) LOOP
        DBMS_OUTPUT.PUT_LINE(r.nume);
    END LOOP;
END;
/
```
4. Ref Cursor (Dinamic) Pointer către un set de rezultate. Poate fi deschis pentru interogări diferite.

```SQL
CREATE OR REPLACE PROCEDURE lista_dinamica (
    p_tabel IN VARCHAR2,
    p_rezultat OUT SYS_REFCURSOR -- Tip predefinit pentru REF CURSOR slab tipizat
) IS
BEGIN
    IF p_tabel = 'ANGAJATI' THEN
        OPEN p_rezultat FOR SELECT * FROM angajati;
    ELSIF p_tabel = 'DEPARTAMENTE' THEN
        OPEN p_rezultat FOR SELECT * FROM departamente;
    END IF;
END;
/
```

## Intrebari 


##  Rezumat Teorie SGBD (PL/SQL)

### 1. Structura Blocului PL/SQL
Unitatea de bază în PL/SQL. Poate fi anonim sau stocat (procedură/funcție).

**Sintaxa:**
```sql
DECLARE
    -- Secțiunea declarativă (opțională)
    -- Variabile, cursori, excepții
    v_nume VARCHAR2(50);
BEGIN
    -- Secțiunea executabilă (obligatorie)
    -- Instrucțiuni SQL și PL/SQL
    SELECT nume INTO v_nume FROM utilizator WHERE id_utilizator = 1;
EXCEPTION
    -- Tratarea erorilor (opțională)
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Nu există utilizatorul.');
END;
/
```

### 2. Variabile și Tipuri de Date
* **Scalare:** `NUMBER`, `VARCHAR2`, `DATE`, `BOOLEAN` (doar în PL/SQL, nu în tabele).
* **De referință (%TYPE):** Copiază tipul unei coloane existente. E vital pentru mentenanță (dacă se schimbă tipul coloanei în bază, se schimbă și în cod).
    ```sql
    v_nume utilizator.nume%TYPE;
    ```
* **De înregistrare (%ROWTYPE):** Stochează o linie întreagă dintr-un tabel.
    ```sql
    v_utilizator utilizator%ROWTYPE;
    -- Accesare: v_utilizator.email
    ```

### 3. Colecții (Foarte important pentru colocviu)
Sunt 3 tipuri majore. Profesorul insistă pe diferențele dintre ele.

| Tip Colecție | Sintaxă Declarare | Caracteristici |
| :--- | :--- | :--- |
| **Tablou Indexat**<br>(Associative Array) | `TYPE t_nume IS TABLE OF tip INDEX BY tip_index;` | - Nu are limită (unbounded).<br>- Cheie-valoare (indexul poate fi integer sau string).<br>- **Nu** necesită constructor.<br>- Doar în PL/SQL (nu poate fi coloană în tabel). |
| **Tablou Imbricat**<br>(Nested Table) | `TYPE t_nume IS TABLE OF tip;` | - Nu are limită.<br>- Index numeric consecutiv inițial.<br>- Poate deveni "sparse" (cu goluri) prin ștergeri.<br>- **Necesită constructor**.<br>- Poate fi stocat în baza de date. |
| **Vector**<br>(Varray) | `TYPE t_nume IS VARRAY(dim) OF tip;` | - **Are limită** (bounded size).<br>- Mereu dens (fără goluri).<br>- **Necesită constructor**.<br>- Poate fi stocat în baza de date. |

**Sintaxă parcurgere colecție:**
```sql
FOR i IN v_colectie.FIRST .. v_colectie.LAST LOOP
    DBMS_OUTPUT.PUT_LINE(v_colectie(i));
END LOOP;
```

### 4. Cursori
Folosiți pentru a procesa interogări care returnează mai multe linii (SELECT-ul simplu `INTO` merge doar pentru o singură linie).

* **Cursor Explicit (Clasic):**
    1.  `DECLARE`: `CURSOR c_num IS SELECT ...;`
    2.  `OPEN`: `OPEN c_num;` (execută query-ul)
    3.  `FETCH`: `FETCH c_num INTO v_variabile;` (aduce o linie)
    4.  `CLOSE`: `CLOSE c_num;`

* **Cursor FOR LOOP (Recomandat - mai simplu):**
    Nu necesită open/fetch/close explicit.
    ```sql
    FOR v_rec IN (SELECT * FROM utilizator) LOOP
        DBMS_OUTPUT.PUT_LINE(v_rec.nume);
    END LOOP;
    ```

* **Cursor Parametrizat:**
    Permite reutilizarea cursorului cu valori diferite în WHERE.
    ```sql
    CURSOR c (p_id NUMBER) IS SELECT * FROM postare WHERE id_utilizator = p_id;
    ...
    OPEN c(5);
    ```

### 5. Excepții
* **Predefinite:** `NO_DATA_FOUND` (SELECT INTO nu găsește nimic), `TOO_MANY_ROWS` (SELECT INTO găsește mai mult de 1 linie), `DUP_VAL_ON_INDEX`.
* **Nepredefinite (interne):** Au cod de eroare (ex: -2292), dar nu au nume. Se asociază un nume folosind `PRAGMA EXCEPTION_INIT`.
    ```sql
    DECLARE
        e_fk EXCEPTION;
        PRAGMA EXCEPTION_INIT(e_fk, -2292); -- FK violation
    BEGIN 
        ... 
    EXCEPTION 
        WHEN e_fk THEN ... 
    END;
    ```
* **Definite de utilizator:**
    ```sql
    DECLARE
        e_eroarea_mea EXCEPTION;
    BEGIN
        IF conditie THEN RAISE e_eroarea_mea; END IF;
    EXCEPTION
        WHEN e_eroarea_mea THEN ...
    END;
    ```

### 6. Triggeri (Declanșatori)
Se execută automat la INSERT, UPDATE, DELETE.

**Tipuri:**
1.  La nivel de instrucțiune (o dată per comandă).
2.  La nivel de rând (`FOR EACH ROW`) - are acces la `:OLD` și `:NEW`.

**Sintaxa:**
```sql
CREATE OR REPLACE TRIGGER trg_verificare_varsta
BEFORE INSERT OR UPDATE ON utilizator
FOR EACH ROW
BEGIN
    IF :NEW.data_nasterii > SYSDATE THEN
        RAISE_APPLICATION_ERROR(-20001, 'Data nașterii invalidă!');
    END IF;
END;
/
```
> **Notă:** Nu poți face SELECT/UPDATE pe tabelul pe care e pus trigger-ul (eroare *Mutating Table*), decât dacă e trigger la nivel de instrucțiune (fără `FOR EACH ROW`).

---

## Intrebari 

### 1. Creare tabel cu un ID și un VARRAY de char-uri
**Context:** Această întrebare testează dacă știi că tipurile colecție trebuie definite la nivel de schemă (`CREATE TYPE`) înainte de a fi folosite într-un tabel. Aceasta încalcă prima formă normală (FN1 - valori atomice), dar este permisă în Oracle Object-Relational.

**Sintaxa:**
```sql
-- Pas 1: Definirea tipului (Trebuie să fie la nivel de schemă, nu în PL/SQL block)
CREATE OR REPLACE TYPE t_lista_telefoane AS VARRAY(5) OF VARCHAR2(10);
/

-- Pas 2: Crearea tabelului folosind tipul
CREATE TABLE agenda (
    id NUMBER PRIMARY KEY,
    nume VARCHAR2(50),
    telefoane t_lista_telefoane
);
/
-- Inserare (necesită constructorul tipului)
INSERT INTO agenda VALUES (1, 'Ion', t_lista_telefoane('0722222', '0744444'));
```

### 2. Cum se adaugă comentarii pe o coloană
**Sintaxa:**
```sql
COMMENT ON COLUMN utilizator.email IS 'Adresa de email unica a utilizatorului';
```
*(Verificare: tabelele de sistem `user_col_comments`)*.

### 3. De ce VARCHAR2 și nu VARCHAR?
* **Răspuns scurt:** În Oracle, `VARCHAR2` este standardul curent.
* **Explicație:** Deși momentan funcționează aproape identic, Oracle își rezervă dreptul de a modifica comportamentul `VARCHAR` în viitor pentru a se conforma standardului ANSI SQL (unde un string gol `''` este diferit de `NULL`). În Oracle `VARCHAR2`, un string gol este identic cu `NULL`. Folosim `VARCHAR2` pentru a garanta compatibilitatea codului pe termen lung.

### 4. De ce CHECK Constraint în loc de Trigger? Care e diferența?
* **CHECK Constraint:**
    * Este **declarativ** (se definește simplu în `CREATE TABLE`).
    * Este mult mai **rapid** (optimizat de SGBD).
    * Este limitat: nu poate accesa alte tabele sau date dinamice (ex: `SYSDATE`). Verifică doar linia curentă.
    * *Exemplu:* `CHECK (LENGTH(telefon)=10)`.
* **Trigger:**
    * Este **procedural** (cod PL/SQL).
    * Este mai **lent** (overhead de execuție).
    * Este flexibil: poate interoga alte tabele, poate trimite mail-uri, poate face validări complexe.
* **Concluzie:** Folosești CHECK oricând e posibil. Folosești Trigger doar când CHECK nu poate face validarea (ex: verificarea stocului într-un alt tabel).

### 5. Diferența dintre colecții (Varray, Nested, Index-by)
Vezi tabelul de la punctul 3 din teorie.
* **Punct cheie:**
    * Stocare în tabel (în BD): doar **Nested Table** sau **Varray**.
    * Indexare pe string (ex: `array['popescu']`): doar **Index-by Table** (Associative Array) și doar în PL/SQL (memorie).

### 6. Întrebări de logică și finețe

* **De ce `BULK COLLECT` într-un Nested Table?**
    * `BULK COLLECT` aduce toate datele dintr-un SELECT într-o singură operațiune, reducând "context switches" între motorul SQL și motorul PL/SQL (performanță mare).
    * Se folosește Nested Table pentru că dimensiunea lui este dinamică (se extinde singur cât e nevoie). Varray te-ar limita la dimensiunea maximă declarată.

* **Doar Nested și Varray au constructor? Index-by nu are?**
    * **DA.** Index-by table (tabelul indexat) nu are constructor. Se inițializează prin atribuire: `tabel(1) := 'ceva';`.
    * Nested și Varray sunt obiecte care pot fi `NULL`. Trebuie apelat constructorul `v_colectie := t_tip();` înainte de utilizare.

* **Fetch first n rows cu Varray?**
    * Tabelele în baze de date (mulțimi) **nu sunt ordonate**. "Primii 5" nu are sens fără un `ORDER BY`.
    * Dacă faci `SELECT ... BULK COLLECT INTO v_varray` cu `FETCH FIRST 5 ROWS ONLY`, funcționează, dar ordinea este dată de SQL, nu de Varray.

* **Ce e un REF CURSOR și de ce nu merge cu FOR?**
    * Un **Ref Cursor** este un pointer către un cursor, o variabilă care poate "arăta" spre diferite query-uri la runtime (cursor dinamic).
    * Nu merge cu `FOR x IN cursor_clasic` pentru că `FOR` cere un cursor static (cunoscut la compilare) pentru a ști ce tip de date să creeze automat pentru variabila iterator `x`.

* **Index-by table: `a('x')`**
    * Aceasta este sintaxa pentru un **Associative Array** indexat după șiruri de caractere (`INDEX BY VARCHAR2`).
    * Sintaxa `a('x') := 1;` înseamnă că elementul cu cheia `'x'` are valoarea `1`. Similar cu un `Map` sau `Dictionary`.


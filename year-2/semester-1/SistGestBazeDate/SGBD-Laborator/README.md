# 📘 SGBD Laborator

Teorie laborator

## 1. Blocuri PL/SQL și Variabile (Laborator 1)
**Structura unui bloc:**
* **Anonim:** Nu este salvat în BD, rulat o singură dată.
* **Stocat:** Proceduri, Funcții, Pachete, Triggeri (au nume, sunt compilate).

**Tipuri de date speciale:**
* [cite_start]`%TYPE`: Copiază tipul unei variabile sau coloane[cite: 186].
    * *Ex:* `v_nume UTILIZATOR.nume%TYPE;`
    * *Avantaj:* Dacă structura tabelei se schimbă, codul rămâne valid.
* [cite_start]`%ROWTYPE`: Copiază structura unei linii întregi dintr-un tabel sau cursor[cite: 187].
    * *Ex:* `v_linie UTILIZATOR%ROWTYPE;`

---

## 2. Colecții (Laborator 2) - *Esențial*
Sunt structuri de date care stochează mai multe elemente de același tip.

| Tip Colecție | Descriere | Caracteristici Cheie | Metode |
| :--- | :--- | :--- | :--- |
| **Tablouri Indexate** (Index-by Tables) | Cheie-Valoare (ca un Map/Hash). | Cheia poate fi număr sau string (`VARCHAR2`). Nu au limită. [cite_start]Nu se pot stoca în coloane de tabel [cite: 808-812]. | `COUNT`, `DELETE`, `EXISTS`. |
| **Tablouri Imbricate** (Nested Tables) | Mulțime neordonată de elemente. | Index numeric consecutiv (inițial). Pot deveni "rare" (sparse) prin ștergere. Necesită `EXTEND`. [cite_start]Pot fi stocate în tabele [cite: 897-913]. | `EXTEND`, `TRIM`, `DELETE`, `FIRST`, `LAST`. |
| **Vectori** (Varrays) | Dimensiune fixă. | Au o limită maximă definită la declarare (`VARRAY(n)`). [cite_start]Sunt mereu dense (nu poți șterge elemente din mijloc) [cite: 1011-1021]. | `EXTEND`, `LIMIT`, `COUNT`. |

**Întrebare frecventă:** "De ce ai folosit `EXTEND`?"
* *Răspuns:* Pentru Nested Tables și Varrays, memoria nu este alocată automat. [cite_start]`EXTEND` adaugă un element null la final pentru a face loc

---

## 3. Cursoare (Laborator 3)
Permit procesarea setului de rezultate linie cu linie

* **Implicit:** Creat automat de Oracle la `SELECT ... INTO` sau DML (`INSERT`, `UPDATE`).
* [cite_start]**Explicit:** Definit de programator (`CURSOR c IS ...`)[cite: 1168].
* [cite_start]**Ciclul de viață:** `DECLARE` -> `OPEN` -> `FETCH` -> `CLOSE`[cite: 1171].
* **Atribute:**
    * [cite_start]`%FOUND` / `%NOTFOUND`: Verifică dacă s-a găsit o linie[cite: 1186].
    * [cite_start]`%ROWCOUNT`: Numărul de linii procesate[cite: 1191].
    * [cite_start]`%ISOPEN`: Dacă cursorul este deschis[cite: 1192].
* [cite_start]**Cursor Parametrizat:** Primește argumente în clauza `WHERE` (ex: postările *unui anumit* utilizator)

---

## 4. Subprograme (Laborator 4)
* **Funcții:** **Trebuie** să returneze o valoare (`RETURN`). [cite_start]Se folosesc în expresii (dreapta egalului).

* **Proceduri:** Execută o acțiune. Pot returna valori doar prin parametri `OUT`.
* **Moduri Parametri:**
    * [cite_start]`IN` (default): Read-only[cite: 1687].
    * [cite_start]`OUT`: Write-only (returnează valori la final)[cite: 1688].
    * [cite_start]`IN OUT`: Citire și modificare[cite: 1687].

**Erori Predefinite:** `NO_DATA_FOUND` (select into nu găsește nimic), `TOO_MANY_ROWS` (select into găsește mai mult de 1 linie)[cite: 1735, 1737].

---

## 5. Pachete (Laborator 5)
* **Specificație (SPEC):** Ce este public (declarări de proceduri, tipuri, variabile).
* **Corp (BODY):** Codul efectiv și elementele private (ascunse).
* [cite_start]**Avantaj:** Încapsulare, variabile globale pe sesiune, performanță (se încarcă tot pachetul în memorie)[cite: 2068].

---

## 6. Declanșatori / Triggers (Laborator 6)
Blocuri executate automat la un eveniment.

* **Tipuri:**
    * **LMD (DML):** `INSERT`, `UPDATE`, `DELETE`.
    * **LDD (DDL):** `CREATE`, `DROP`, `ALTER`.
    * **INSTEAD OF:** Pentru vizualizări complexe.
* **Nivel:**
    * **Statement-level:** O dată per comandă.
    * **Row-level (`FOR EACH ROW`):** O dată pentru fiecare rând afectat. [cite_start]Permite accesul la valorile `:OLD` și `:NEW`[cite: 2617, 2672].
* **Eroare Mutating Table:** Apare la row-level triggers când încerci să citești tabelul care este modificat chiar în acel moment.
## Tehnici de căutare neinformată

Se folosesc pentru probleme care pot fi abstractizate la un graf (orientat sau neorientat).
Presupun existența unui nod de început (nodul start) și a unuia sau mai multe noduri scop (la care vrem să ajungem din nodul start).

### Breadth-First Search

Breadth-First Search (BFS - Căutare în Lățime) este un algoritm de parcurgere a unui graf sau arbore, care explorează nodurile nivel cu nivel, pe lățime.

Pași:
1. Se pune nodul start în coadă
2. Cât timp coada nu este vidă:
  - Se extrage primul nod din coadă
    - Dacă este nod scop → se returnează soluția
    - Dacă s-a ajuns la numărul dorit de soluții → algoritmul se oprește

  - Se generează (expandează) succesorii nodului
    - Se adaugă în coadă doar succesorii care nu apar deja pe drumul curent (pentru a evita ciclurile pe acea ramură)
    
    
Observație: Faptul că un nod a fost vizitat pe o altă ramură nu împiedică adăugarea lui din nou. Problema trebuie modelată ca arbore de căutare, nu ca graf cu marcaj global

### Depth-First Search

Depth-First Search (DFS - Căutare în Adâncime) este un algoritm de parcurgere a unui graf sau arbore, care explorează nodurile mergând cât mai adânc pe o ramură înainte de a reveni.

Pași:

1. Se pune nodul start pe o stivă (sau se apelează recursiv funcția pe nodul start).
2. Cât timp stiva nu este vidă:

* Se extrage ultimul nod adăugat (vârful stivei)

  * Dacă este nod scop → se returnează soluția
  * Dacă s-a ajuns la numărul dorit de soluții → algoritmul se oprește

* Se generează (expandează) succesorii nodului

  * Se adaugă pe stivă doar succesorii care nu apar deja pe drumul curent (pentru a evita ciclurile pe acea ramură)
  * Succesorii se adaugă astfel încât explorarea să continue pe ultima ramură descoperită

Observație: Faptul că un nod a fost vizitat pe o altă ramură nu împiedică explorarea lui din nou. Problema este modelată ca arbore de căutare, fără marcaj global al nodurilor vizitate.


### Uniform Cost Search

Uniform Cost Search (UCS - Căutare cu Cost Uniform) este un algoritm de căutare într-un graf sau arbore care explorează nodurile în ordinea costului total acumulat de la nodul start până la ele. La fiecare pas este extins nodul cu costul cel mai mic.

Pași:

1. Se pune nodul start într-o coadă de priorități, cu costul 0.

2. Cât timp coada de priorități nu este vidă:

* Se extrage nodul cu costul total minim

  * Dacă este nod scop → se returnează soluția (este optimă dacă toate costurile sunt pozitive)
  * Dacă s-a ajuns la numărul dorit de soluții → algoritmul se oprește

* Se generează (expandează) succesorii nodului

  * Pentru fiecare succesor se calculează costul total (cost drum până la părinte + cost muchie)
  * Se adaugă în coada de priorități doar succesorii care nu apar deja pe drumul curent (pentru a evita ciclurile pe acea ramură)

Observație: Nodurile sunt selectate după cost, nu după nivel (ca la BFS) și nici după adâncime (ca la DFS). Dacă toate costurile muchiilor sunt egale, algoritmul se comportă similar cu BFS.


### Depth-Limited Search

Depth-Limited Search (DLS - Căutare cu Limită de Adâncime) este o variantă a algoritmului DFS care explorează în adâncime, dar impune o limită maximă de adâncime până la care poate coborî în arbore.

Pași:

1. Se pornește din nodul start, cu adâncimea 0, folosind o stivă sau apel recursiv.
2. Cât timp mai există noduri de explorat:

* Se extrage ultimul nod adăugat (vârful stivei)

  * Dacă este nod scop → se returnează soluția
  * Dacă s-a ajuns la numărul dorit de soluții → algoritmul se oprește

* Dacă adâncimea nodului este mai mică decât limita impusă:

  * Se generează (expandează) succesorii
  * Se adaugă pe stivă doar succesorii care nu apar deja pe drumul curent (pentru a evita ciclurile pe acea ramură)

* Dacă adâncimea este egală cu limita → nodul nu se mai expandează (se face backtracking)

Observație: DLS previne explorarea infinită în spații foarte adânci sau infinite, dar poate rata soluții aflate dincolo de limita impusă. Dacă limita este suficient de mare, comportamentul devine similar cu DFS.

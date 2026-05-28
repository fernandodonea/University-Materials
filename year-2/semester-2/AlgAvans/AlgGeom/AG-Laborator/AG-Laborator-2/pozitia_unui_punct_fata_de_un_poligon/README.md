# Poziția unui punct față de un poligon



#### Descriere

Implementați un algoritm de complexitate de timp liniară care să determine poziția relativă a unui punct $`Q`$ față de un poligon *arbitrar* $`P_{1},\ldots,P_{n}`$.

#### Date de intrare

Programul va citi de la tastatură un număr natural $`n`$ și apoi $`n`$ perechi de numere întregi separate prin spațiu $`x_{i}y_{i}`$, pe linii distincte, reprezentând coordonatele vârfului $`P_{i}(x_{i},y_{i})`$ al poligonului.

După aceea urmează numărul natural $`m`$ și apoi $`m`$ perechi de numere întregi separate prin spațiu $`x_{j}y_{j}`$, reprezentând coordonatele punctului $`Q_{j}(x_{j},y_{j})`$.

#### Date de ieșire

Pentru fiecare dintre cele $`m`$ puncte, programul va afișa pe ecran:

- `INSIDE`: dacă punctul $`Q_{j}`$ se află în interiorul poligonului;
- `OUTSIDE`: dacă punctul $`Q_{j}`$ se află în exteriorul poligonului;
- `BOUNDARY`: dacă punctul $`Q_{j}`$ se află pe laturile poligonului.

#### Restricții și precizări

- $`3 \leq n \leq 1000`$
- $`1 \leq m \leq 1000`$
- $`- 10^{9} \leq x,y \leq 10^{9}`$

#### Exemplu

##### Input

Copy

```
12
0 6
0 0
6 0
6 6
2 6
2 2
4 2
4 5
5 5
5 1
1 1
1 6
3
3 4
7 3
3 2
```

##### Output

Copy

```
INSIDE
OUTSIDE
BOUNDARY
```

##### Explicație

Reprezentarea grafică a situației de mai sus este:

#### Indicații de rezolvare

**Varianta 1** *(O soluție incompletă, care permite obținerea unui punctaj parțial)*

Puteți folosi [problema 1 de la acest laborator](https://cms.fmi.unibuc.ro/problem/l6pb1), care rezolvă cerința în cazul poligoanelor convexe. Combinând cu soluția [problemei 3 de la L5](https://cms.fmi.unibuc.ro/problem/l5pb3), se ajunge la o soluție în cazul poligoanelor stelate.

**Varianta 2** *(O soluție completă, bazată pe o abordare diferită)*

Soluția completă se bazează pe regula "par-impar" (*"odd-even rule"*), principiu folosit pentru a delimita [interiorul unui poligon](https://web.cs.ucdavis.edu/~okreylos/TAship/Spring2000/PointInPolygon.html) sau al unei [linii poligonale cu autointersecții](https://www.sciencedirect.com/science/article/pii/S0925772101000128). Numele de "par-impar" derivă din următorul mecanism (descris pe scurt):

- Se alege un punct $`M`$ "departe" de poligon (de exemplu coordonatele lui $`M`$ să fie mai mari / mai mici decât coordonatele corespunzătoare ale tuturor vârfurilor poligonului).
- Se determină numărul de laturi intersectate de **segmentul deschis** $`(MQ)`$ **în interior**. Dacă acest număr este par, punctul $`Q`$ este situat în exteriorul poligonului, iar dacă este impar, punctul este situat în interior.
- O implementare completă trebuie să trateze corect cazul în care punctul $`Q`$ este situat pe una din laturile poligonului. De asemenea, dacă segmentul $`(MQ)`$ trece printr-un vârf al poligonului, trebuie ales un alt punct "departe" de poligon. Se demonstrează că numărul total de intersecții se poate modifica, **dar paritatea rămâne neschimbată**.
- În exemplul din figură, pentru punctele $`Q_{1}`$ și $`Q_{2}`$, numărul de intersecții dintre segmentele $`(MQ_{1})`$, respectiv $`(MQ_{2})`$ este par (4, respectiv 0), punctele fiind situate în exteriorul poligonului. Pentru punctul $`Q_{3}`$, numărul de intersecții este impar (5), punctul fiind situat în interiorul poligonului.

![Exemplu](https://cms.fmi.unibuc.ro/media/martor/838fbf22-aa65-4e13-abb2-1a15e2a0c3a3.png)

- Două segmente deschise $`(AB)`$ și $`(CD)`$ se intersectează în interior dacă și numai dacă $`A`$ și $`B`$ sunt de o parte și de alta a dreptei $`CD`$ **și** $`C`$ și $`D`$ sunt de o parte și de alta a dreptei $`AB`$. Aceste proprietăți se verifică aplicând testul de orientare.

- În figura de mai jos, segmentele deschise $`(AB)`$ și $`(CD)`$ se intersectează, fiind verificată proprietatea de mai sus. Observați că segmentele $`(AB)`$ și $`(CE)`$ **nu** se intersectează. Astfel, $`C`$ și $`E`$ sunt de o parte și de alta a dreptei $`AB`$, dar $`A`$ și $`B`$ nu sunt de o parte și de alta a dreptei $`CE`$. De asemenea, segmentele deschise $`(AB)`$ și $`(CF)`$ nu se intersectează ($`A`$ este situat pe dreapta $`CF`$, deci $`A`$ și $`B`$ nu pot fi de o parte și de alta a dreptei $`CF`$).

  ![](https://cms.fmi.unibuc.ro/media/martor/a41e83f9-d8a9-4687-bcf0-ee211f2073ac.png)

\
[proudly powered by **DMOJ**](https://dmoj.ca/) \|

català (ca) Deutsch (de) Ελληνικά (el) English (en) español (es) français (fr) Hrvatski (hr) Magyar (hu) 日本語 (ja) Қазақ (kk) 한국어 (ko) Português (pt) Română (ro) Русский (ru) srpski (latinica) (sr-latn) Türkçe (tr) Tiếng Việt (vi) 简体中文 (zh-hans) 繁體中文 (zh-hant)
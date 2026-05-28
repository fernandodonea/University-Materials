# Punct in poligon convex


#### Descriere

Se consideră un poligon convex cu $`n`$ vârfuri date în ordine trigonometrică ($`P_{1}P_{2}\ldots P_{n}`$) și $`m`$ puncte în plan ($`R_{1},R_{2},\ldots,R_{m}`$). Pentru fiecare dintre cele $`m`$ puncte să se stabilească dacă se află în **interiorul**, în **exteriorul** sau **pe una dintre laturile** poligonului.

#### Date de intrare

Se citește de la tastatură $`n`$, reprezentând numărul de vârfuri ale poligonului. Următoarele $`n`$ linii vor conține câte două numere întregi $`x_{i},y_{i}`$, coordonatele punctului $`P_{i}`$.

Pe următoarea linie se află $`m`$ reprezentând numărul de puncte pentru care trebuie să aflăm poziția față de poligon. Următoarele $`m`$ linii vor conține câte două numere întregi $`x_{i},y_{i}`$, coordonatele punctului $`R_{i}`$.

#### Date de iesire

Pentru fiecare punct $`R_{i}`$ se va afișa, pe câte un rând nou, un mesaj corespunzător poziției sale față de poligon:

- `INSIDE` (dacă punctul $`R_{i}`$ se află în poligon)
- `OUTSIDE` (dacă punctul $`R_{i}`$ se află în afara poligonului)
- `BOUNDARY` (dacă punctul $`R_{i}`$ se află pe una dintre laturile poligonului)

#### Restricții și precizări

- $`3 \leq n,m \leq 10^{5}`$.
- $`- 10^{9} \leq x_{i},y_{i} \leq 10^{9}`$

#### Exemplu

##### Input



```txt
4
0 0
5 0
5 5
0 5
3
2 2
7 7
5 2
```

##### Output

```
INSIDE
OUTSIDE
BOUNDARY
```

##### Explicație

Reprezentarea grafică a situației de mai sus este următoarea:

#### Indicații de rezolvare

O metodă simplă de a verifica dacă un punct se află în interiorul unui poligon convex este descrisă [aici](https://inginious.org/course/competitive-programming/geometry-pointinconvex) și se bazează pe efectuarea **testului de orientare** între fiecare latură a poligonului convex și punctul ales. O astfel de verificare necesită $`\mathcal{O}(n)`$ timp, deci per total soluția are complexitatea-timp $`\mathcal{O}(mn)`$.

Pentru a trece toate testele, trebuie să implementați o soluție care să ruleze în timp $`\mathcal{O}(m\log n)`$. Un astfel de algoritm, care utilizează o căutare binară, este descris [pe acest site](https://cp-algorithms.com/geometry/point-in-convex-polygon.html).


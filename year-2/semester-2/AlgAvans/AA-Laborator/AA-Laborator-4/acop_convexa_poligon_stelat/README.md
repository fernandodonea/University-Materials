
## Acoperirea convexă a unui poligon stelat


Un poligon $`P_{1}P_{2}\ldots P_{n}P_{1}`$ se numește ***stelat*** dacă există un punct $`M`$ în interiorul său astfel încât, oricum s-ar alege un punct $`X`$ pe laturile poligonului sau un vârf al acestuia, segmentul $`\lbrack MX\rbrack`$ este conținut în întregime în interiorul poligonului.

Fiind dat un poligon stelat, trebuie să implementați un algoritm cu complexitate liniară de timp care să găsească acoperirea convexă a unui poligon stelat.

#### Date de intrare

Se va citi de la tastatură un număr $`n`$, reprezentând numărul de vârfuri al poligonului și apoi $`n`$ linii care conțin perechi de numere întregi $`x_{i}y_{i}`$, separate prin spațiu, reprezentând coordonatele vârfului $`P_{i}`$, **parcurse în sens trigonometric**.

#### Date de ieșire

Programul va afișa un număr $`k`$, reprezentând numărul de vârfuri ale acoperirii convexe a mulțimii $`P_{1},P_{2},\ldots,P_{n}`$ și apoi $`k`$ perechi de numere întregi, pe linii distincte, reprezentând coordonatele acestor vârfuri, **parcurse tot în sens trigonometric** (dar puteți porni de la orice vârf).

#### Restricții și precizări

- $`1 \leq n \leq 100000`$
- $`- 10^{9} \leq x_{i},y_{i} \leq 10^{9}`$

#### Exemple

##### Exemplul 1

###### Input

Copy

```
3
-1 3
-3 -2
4 -3
```

###### Output

Copy

```
3
-1 3
-3 -2
4 -3
```

###### Explicație

Exemplul corespunde următorului poligon stelat, un triunghi oarecare:

Puteți începe să descrieți acoperirea convexă de la orice vârf al ei, cât timp parcurgerea este în sens trigonometric. $`( - 3,2),(4, - 3),( - 1,3)`$ și $`(4, - 3),( - 1,3),( - 3,2)`$ erau de asemenea soluții acceptabile.

##### Exemplul 2

###### Input

Copy

```
10
0 3
-1 1
-5 0
-2 -1
-4 -5
1 -2
5 -3
3 0
6 3
2 2
```

###### Output

Copy

```
5
-4 -5
5 -3
6 3
0 3
-5 0
```

###### Explicație

Exemplul corespunde următorului poligon stelat, o stea neregulată cu 5 colțuri:

![Stea cu cinci colțuri, a cărui acoperire convexă este formată dintr-o submulțime a vârfurilor sale](https://cms.fmi.unibuc.ro/media/martor/5eb30523-b1c5-43ec-a2cb-ce90c45146fc.png)

##### Exemplul 3

###### Input

Copy

```
8
0 2
-2 2
-2 0
-2 -2
0 -2
2 -2
2 0
2 2
```

###### Output

Copy

```
4
-2 2
-2 -2
2 -2
2 2
```

###### Explicație

Exemplul dat este o stea cu 4 colțuri degenerată, care e de fapt un pătrat:

![Pătrat](https://cms.fmi.unibuc.ro/media/martor/ed47709b-55de-41f6-9c26-ee758bb4b888.png)

\
[proudly powered by **DMOJ**](https://dmoj.ca/) \|

català (ca) Deutsch (de) Ελληνικά (el) English (en) español (es) français (fr) Hrvatski (hr) Magyar (hu) 日本語 (ja) Қазақ (kk) 한국어 (ko) Português (pt) Română (ro) Русский (ru) srpski (latinica) (sr-latn) Türkçe (tr) Tiếng Việt (vi) 简体中文 (zh-hans) 繁體中文 (zh-hant)
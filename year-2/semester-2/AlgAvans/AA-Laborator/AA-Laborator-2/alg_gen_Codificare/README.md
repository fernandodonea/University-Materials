# Algoritmi genetici - codificare 

#### Descriere

##### Context

Primul pas în rezolvarea unei probleme folosind un [algoritm genetic](https://en.wikipedia.org/wiki/Genetic_algorithm) este să stabilim **cum vom reprezenta datele**. Pentru simplitate, _cromozomii_ ar trebui să fie șiruri binare de aceeași dimensiune (fixată), ca să putem gestiona ușor populația și să aplicăm pe ea operațiile _genetice_ (selecție, crossover, mutație etc). În același timp, soluțiile pentru majoritatea problemelor sunt date structurate (trebuie să determinăm o submulțime, un număr real, un graf etc.)

Suntem astfel nevoiți să găsim o cale de a **codifica** aceste soluții ca șiruri de biți. Câteva exemple:

*   Dacă vrem să rezolvăm [_problema rucsacului_](https://en.wikipedia.org/wiki/Knapsack_problem) în _varianta discretă_, atunci vom avea un șir binar în care bitul de pe poziția i indică dacă includem sau nu obiectul i.
*   Dacă vrem să rezolvăm [_problema comisului-voiajor_](https://en.wikipedia.org/wiki/Travelling_salesman_problem), atunci am putea avea un șir binar care reprezintă un tur între orașe: etichetăm fiecare oraș cu un șir de exact k biți, iar apoi o soluție o să fie dată de n⋅k biți concatenați, care reprezintă (în ordine) etichetele orașelor pe care le vizităm.
*   Dacă vrem să rezolvăm o [_problemă de optimizare_](https://en.wikipedia.org/wiki/Optimization_problem) (i.e. să găsim maximul sau minimul unei funcții cu valori în R), atunci va trebui să discretizăm intervalul în care căutăm valoarea optimă a parametrului/parametrilor, iar șirul binar va reprezenta un număr real din această discretizare (o reprezentare [_fixed-point_](https://en.wikipedia.org/wiki/Fixed-point_arithmetic)).

##### Cerință

Pentru această problemă, veți scrie un program care va permite codificarea și decodificarea unor numere reale ca șiruri binare de precizie fixată.

Pentru intervalul [a,b] și o precizie de p zecimale, formula din curs ne spune că vom avea nevoie de l=⌈log 2⁡((b−a)10 p)⌉ biți în cromozomii noștri pentru a putea reprezenta un număr real din intervalul respectiv la precizia cerută. Pasul de discretizare va fi d=(b−a)/2 l, vom obține intervalele [a,a+d), [a+d,a+2 d), [a+2 d,a+3 d), …, [a+(2 l−1)d,b].

Pentru fiecare caz de test, va trebui să răspundeți la m întrebări de tipul:

*   `TO`: fiind dat un număr real din intervalul [a,b], determinați care este reprezentarea lui ca șir binar.
*   `FROM`: fiind dat un șir binar cu exact l biți, determinați la ce număr real din interval corespunde.

#### Date de intrare

Se citesc de la tastatură a și b, două numere reale care reprezintă capetele intervalului [a,b]. Pe următoarea linie se va citi precizia p (număr natural), iar apoi o linie pe care se regăsește m, numărul de teste.

Pe următoarele 2 m rânduri avem fie:

*   Șirul de caractere `TO`, iar pe următorul rând un număr real x i.
*   Șirul de caracter `FROM`, iar pe următorul rând un șir binar b i, format doar din caracterele `0` și `1`, de lungime l.

#### Date de ieșire

Pentru fiecare test se va afișa, pe câte un rând nou, valorea codificată/decodificată a numărului real/șirului de biți dat:

*   Dacă cerința este de tipul `TO`, se va afișa un șir binar de lungime l, care reprezintă capătul din stânga al intervalului de discretizare care conține numărul real x i.
*   Dacă cerința este de tipul `FROM`, se va afișa un număr real, care reprezintă capătul din stânga al intervalului de discretizare identificat de șirul de biți b i.

#### Restricții și precizări

*   −10≤a≤b≤10.
*   1≤p≤10
*   1≤m≤1000
*   La testele de tip `FROM`, puteți presupune că șirul de biți pe care îl veți citi va avea exact lungimea l.
*   La testele de tip `FROM`, puteți afișa numerele reale cu oricâte zecimale, dar va trebui să corespundă cu răspunsul corect cel puțin până la precizia p (i.e. o eroare absolută de cel mult 10−p).

#### Exemplul 1

##### Input

```
0 1
1
4
TO
0.2
TO
0.5
FROM
0101
FROM
0000
```

##### Output

```
0011
1000
0.3125
0.0000
```

##### Explicație

Vom lucra cu intervalul [0,1] și precizia 1. Pe baza formulei din curs, avem nevoie de l=⌈log 2⁡((b−a)10 p)⌉=⌈log 2⁡((1−0)⋅10 1)⌉=4 biți ca să codificăm numerele reale din intervalul dat. Pasul de discretizare este d=(b−a)/2 l=(1−0)/2 4=0.0625.

Avem de răspuns la 5 teste:

*   Numărul real 0.2 este în intervalul de discretizare cu index 3, acesta fiind [a+3 d,a+4 d), adică [0.1875,0.25). Numărul 3 în binar se scrie ca 0011.
*   Numărul real 0.5 este în intervalul de discretizare cu index 8, deoarece 0.5 este fix capătul din stânga al intervalului: 0.5=0+8⋅0.0625=a+8 d. Numărul 8 în binar se scrie ca 1000.
*   Șirul binar 0101 corespunde la numărul 5 (în baza 10), deci va trebui să afișăm capătul din stânga al celui de al 5-lea interval de discretizare, a+5 d=0+5⋅0.0625=0.3125.
*   Șirul binar 0000 corespunde la numărul 0 (în baza 10), deci va trebui să afișăm capătul din stânga al celui de al 0-lea interval de discretizare, a+0 d=0.

#### Exemplul 2

##### Input

```
-1 1
2
3
FROM
00000001
FROM
11111111
TO
0.9999
```

##### Output

```
-0.9921875
0.9921875
11111111
```

##### Explicație

Vom lucra cu intervalul [−1,1] și precizia 2. Pe baza formulei din curs, avem nevoie de l=⌈log 2⁡((b−a)10 p⌉=⌈log 2⁡((1−(−1))⋅10 2)⌉=8 biți ca să codificăm numerele reale din intervalul dat. Pasul de discretizare este d=(b−a)/2 l=(1−(−1))/2 8=0.0078125.

Avem de răspuns la 3 teste:

*   Șirul binar 00000001 corespunde la numărul 1 (în baza 10), deci va trebui să afișăm capătul din stânga al intervalului de discretizare cu indexul 1, a+1 d=−1+1⋅0.0078125=−0.9921875.
*   Șirul binar 11111111 corespunde la numărul 255 (în baza 10), deci va trebui să afișăm capătul din stânga al celui de al 255-lea interval de discretizare, a+255 d=−1+255⋅0.0078125=0.9921875.
*   Numărul real 0.9999 este în al 255-lea interval de discretizare, deoarece acesta este [a+255 d,a+256 d), adică [0.9921875,1). Numărul 255 în binar se scrie ca 11111111.
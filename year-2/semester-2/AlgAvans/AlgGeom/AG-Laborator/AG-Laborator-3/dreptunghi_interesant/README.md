# Poziția unui punct față de semiplane orizontale și verticale



#### Descriere

Se dau $`m`$ puncte $`Q_{j}`$ și $`n`$ semiplane din $`\mathbb{R}^{2}`$, oricare dintre ele **orizontal** (paralel cu axa $`Ox`$) sau **vertical** (paralel cu axa $`Oy`$), toate fiind definite prin inecuații de forma $`a_{i}x + b_{i}y + c_{i} \leq 0`$.

Spunem că un dreptunghi este **interesant** dacă este determinat de unele dintre semiplanele date (nu neapărat toate semiplanele!). Mai precis, vârfurile sale sunt exact intersecții ale dreptelor suport ale unora dintre semiplane, laturile dreptunghiului sunt incluse în dreptele suport corespunzătoare, iar interiorul dreptunghiului este inclus în fiecare din semiplanele respective (altfel spus, dreptunghiul și interiorul său sunt **exact** intersecția semiplanelor respective).

În figura de mai jos sunt două dreptunghiuri interesante: $`A_{1}A_{2}A_{4}A_{3}`$, determinat de semiplanele $`a,b,c,d`$ și $`A_{1}A_{2}A_{6}A_{5}`$, determinat de semiplanele $`a,b,c,e`$. Dreptunghiul $`A_{3}A_{4}A_{6}A_{5}`$ **nu** este interesant. Chiar dacă vârfurile sale sunt date de intersecțiile semiplanelor $`a,b,d,e`$ și laturile sale sunt incluse în dreptele suport ale acestora, interiorul său **nu** este inclus în intersecția semiplanelor respective.

Se cere să determinați pentru fiecare punct dacă se află în **interiorul** unui dreptunghi **interesant** (iar în cazul afirmativ, să spuneți care este aria minimă a unui dreptunghi interesant care îl conține).

Astfel, în figura de mai sus, sunt considerate punctele $`Q_{1} = (2,0)`$, $`Q_{2} = (1,0)`$, $`Q_{3} = (0,0)`$, $`Q_{4} = (0, - 2.5)`$:

- $`Q_{1}`$ nu este situat în interiorul niciunui dreptunghi interesant.
- $`Q_{2}`$ este pe laturile unor dreptunghi interesante, dar nu este în interiorul niciunuia dintre acestea.
- $`Q_{3}`$ este situat în interiorul dreptunghiurilor interesante $`A_{1}A_{2}A_{4}A_{3}`$ și $`A_{1}A_{2}A_{6}A_{5}`$. Dintre acestea, $`A_{1}A_{2}A_{4}A_{3}`$ are aria minimă, egală cu $`8`$.
- $`Q_{4}`$ este situat în interiorul dreptunghiului interesant $`A_{1}A_{2}A_{6}A_{5}`$, de arie $`10`$.

Recomandarea este să atacați această problemă după ce ați rezolvat-o cu succes pe [cea precedentă](https://cms.fmi.unibuc.ro/problem/l7pb3).

#### Date de intrare

Se va citi de pe primul rând $`n`$, numărul de semiplane care trebuie intersectate, și apoi $`n`$ triplete de numere întregi $`a_{i}b_{i}c_{i}`$, separate prin câte un spațiu, pe linii distincte, reprezentând coeficienții care definesc inecuația semiplanului $`i`$: $`a_{i}x + b_{i}y + c_{i} \leq 0`$. Toate semiplanele citite vor fi fie orizontale, fie verticale (acest lucru nu mai trebuie verificat).

De pe următorul rând se va citi $`m`$, numărul de puncte pentru care trebuie să determinați dacă se află în interiorul vreunui dreptunghi interesant sau nu. Pe următoarele $`m`$ rânduri se vor afla perechi de numere reale $`x_{Q_{j}}y_{Q_{j}}`$, separate printr-un spațiu, reprezentând coordonatele punctului $`Q_{j}(x_{Q_{j}},y_{Q_{j}})`$.

#### Date de ieșire

Pentru fiecare punct $`Q_{j}`$ cu $`j = \overset{―}{1,m}`$, programul va afișa unul dintre următoarele șiruri de caractere:

- `NO`, dacă nu există niciun dreptunghi interesant sau dacă există dreptunghiuri interesante, dar punctul $`Q_{j}`$ **nu** se află **în interiorul** niciunui astfel de dreptunghi.
- `YES`, dacă există cel puțin un dreptunghi interesant care să îl conțină pe $`Q_{j}`$ **în interior**.

În cazul în care răspunsul de pe o linie este `YES`, pe următoarea linie trebuie afișat un număr **real** $`A_{j}`$, reprezentând valoarea minimă a ariilor dreptunghiurilor interesante care îl conțin pe punctul $`Q_{j}`$ **în interior**.

**Aria dreptunghiurilor interesante poate fi un număr real. Aceasta se va afișa cu o precizie de 6 zecimale.**

#### Restricții și precizări

- $`1 \leq n \leq 10000`$
- $`1 \leq m \leq 1000`$
- $`- 10^{6} \leq a_{i},b_{i},c_{i} \leq 10^{6}`$
- $`- 10^{6} \leq x_{Q_{j}},y_{Q_{j}} \leq 10^{6}`$

#### Exemple

##### Exemplul 1

###### Input

Copy

```
3
-1 0 1
1 0 -2
0 1 3
1
1.5 -4
```

###### Output

Copy

```
NO
```

###### Explicație

Cele trei semiplane au inecuațiile $`- x + 1 \leq 0`$, $`x - 2 \leq 0`$, respectiv $`y + 3 \leq 0`$. Inecuațiile pot fi rescrise $`x \geq 1`$, $`x \leq 2`$, $`y \leq - 3`$.

Punctele care întrunesc condiția $`1 \leq x \leq 2`$ sunt cele din fâșia verticală dintre dreptele $`x = 1`$ și $`x = 2`$. Condiția $`y \leq - 3`$ ne obligă să le luăm pe cele care au ordonata mai mică sau egală cu $`- 3`$.

Intersecția oricăror semiplane din cele date este o mulțime nemărginită. Așadar, nu există niciun dreptunghi interesant, deci se va afișa `NO`.

##### Exemplul 2

###### Input

Copy

```
4
-1 0 1
1 0 -2
0 1 3
0 -2 -8
3
0 0
1 -3.5
1.25 -3.5
```

###### Output

Copy

```
NO
NO
YES
1
```

###### Explicație

Cele patru semiplane au inecuațiile $`- x + 1 \leq 0`$, $`x - 2 \leq 0`$, $`y + 3 \leq 0`$, respectiv $`- 2y - 8 \leq 0`$. Inecuațiile pot fi rescrise $`x \geq 1`$, $`x \leq 2`$, $`y \leq - 3`$, $`y \geq - 4`$.

Punctele care întrunesc condiția $`1 \leq x \leq 2`$ sunt cele din fâșia verticală dintre dreptele $`x = 1`$ și $`x = 2`$. Punctele care întrunesc condiția $`- 4 \leq y \leq - 3`$ sunt cele din fâșia orizontală dintre dreptele $`y = - 4`$ și $`y = - 3`$.

Intersecția lor este dreptunghiul determinat de punctele $`A = (1, - 3),B = (1, - 4),C = (2, - 4),D = (2, - 3)`$, acesta este singurul dreptunghi interesant pentru datele de intrare considerate.

- Punctul $`Q_{1}`$ **nu** este situat în interiorul acestui dreptunghi, iar pentru el se va afișa `NO`.
- Punctul $`Q_{2}`$ este situat pe laturile acestui dreptunghi, nu în interiorul lui, deci se va afișa `NO`.
- Punctul $`Q_{3}`$ este conținut în interiorul dreptunghiului, deci se va afișa `YES`, iar pe rândul următor se va afișa aria dreptunghiului, care este $`1`$.

![](https://cms.fmi.unibuc.ro/media/martor/42e33745-e8ae-4e80-ab82-a38c7be08c24.png)

##### Exemplul 3

###### Input

Copy

```
11
-1 0 -1
0 -3 -6
0 2 -6
1 0 -3
0 1 -2
2 0 -10
0 -1 -3
-4 0 0
-1 0 1
0 -1 -1
1 0 -4
1
2 1
```

###### Output

Copy

```
YES
6
```

###### Explicație

Inecuațiile semiplanelor sunt: $`x \geq - 1`$, $`y \geq - 2`$, $`y \leq 3`$, $`x \leq 3`$, $`y \leq 2`$, $`x \leq 5`$, $`y \geq - 3`$, $`x \geq 0`$, $`x \geq 1`$, $`y \geq - 1`$, $`x \leq 4`$.

Există mai multe dreptunghiuri interesante care îl conțin pe $`Q_{1}`$, iar valoarea minimă a ariilor acestora este $`6`$.

# Puncte de intersectie



#### Descriere

Se dă o mulțime de $`n`$ segmente în planul $`\mathbb{R}^{2}`$. Se presupune că fiecare segment al mulțimii este orizontal sau vertical. Vi se cere să determinați numărul total de puncte de intersecție dintre segmentele orizontale și cele verticale.

#### Date de intrare

Se va citi de la tastatură un număr natural $`n`$, reprezentând numărul de segmente. Urmează, pe $`n`$ rânduri distincte, coordonatele extremităților segmentelor. Astfel, al $`i`$ -lea dintre aceste rânduri va conține patru numere întregi $`x_{i,1}y_{i,1}x_{i,2}y_{i,2}`$, separate prin câte un spațiu, reprezentând coordonatele extremităților segmentului $`s_{i}`$ (așadar, segmentul $`s_{i}`$ este determinat de punctele $`P_{i,1} = (x_{i,1},y_{i,1})`$ și $`P_{i,2} = (x_{i,2},y_{i,2})`$).

#### Date de ieșire

Programul va afișa pe ecran numărul total de puncte de intersecție dintre segmentele orizontale și cele verticale.

#### Restricții și precizări

- $`1 \leq n \leq 10^{5}`$.
- $`- 10^{6} \leq x_{i,1} \leq x_{i,2} \leq 10^{6}`$.
- $`- 10^{6} \leq y_{i,1} \leq y_{i,2} \leq 10^{6}`$.
- $`(x_{i,1}y_{i,1}) \neq (x_{i,2}y_{i,2})`$.
- Segmentele au doar puncte de intersecție **interioare**, deci niciunul dintre capetele segmentelor nu este punct de intersecție

#### Exemplu

##### Input

Copy

```
6
4 -4 4 8
2 -1 7 -1
-5 6 0 6
-2 -3 -2 5
2 -5 9 -5
-3 2 6 2
```

##### Output

Copy

```
3
```

##### Explicație

Coordonatele de mai sus corespund următoarei figuri, în care sunt în total trei puncte de intersecție (marcate cu roșu) între segmentele orizontale și cele verticale:

#### Observație

Această problemă poate fi găsită (și rezolvată) și [aici](https://cses.fi/problemset/task/1740).

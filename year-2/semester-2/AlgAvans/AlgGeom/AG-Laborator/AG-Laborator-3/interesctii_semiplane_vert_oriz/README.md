# Intersecții de semiplane orizontale și verticale


#### Descriere

Orice dreaptă din $`\mathbb{R}^{2}`$ împarte planul în două jumătăți, numite semiplane. Fiindcă o dreaptă în plan este definită de o ecuație de forma $`ax + by + c = 0`$ (cu $`a \neq 0`$ sau $`b \neq 0`$), cele două semiplane corespunzătoare acesteia pot fi descrise ca mulțimile de puncte $`(x,y)`$ pentru care $`ax + by + c \geq 0`$, respectiv $`ax + by + c \leq 0`$. Pentru aceste semiplane, dreapta care le determină se numește **dreaptă suport**.

Pentru această problemă, va trebui să determinați natura intersecției a $`n`$ semiplane. Oricare din aceste semiplane este **orizontal** (paralel cu axa $`Ox`$) sau **vertical** (paralel cu axa $`Oy`$).

#### Date de intrare

Se vor citi de la tastatură un număr natural $`n`$, reprezentând numărul de semiplane care trebuie intersectate, și apoi $`n`$ triplete de numere întregi $`a_{i}b_{i}c_{i}`$, separate prin câte un spațiu, reprezentând coeficienții care definesc inecuația semiplanului $`i`$, **inecuație de forma** $`a_{i}x + b_{i}y + c_{i} \leq 0`$.

Toate semiplanele citite vor fi fie orizontale, fie verticale (acest lucru nu mai trebuie verificat).

#### Date de ieșire

Se va afișa pe ecran unul dintre următoarele șiruri de caractere:

- `VOID`, dacă intersecția celor $`n`$ semiplane este **vidă**.
- `BOUNDED`, dacă intersecția celor $`n`$ semiplane este **nevidă** și **mărginită**.
- `UNBOUNDED`, dacă intersecția celor $`n`$ semiplane este **nevidă** și **nemărginită**.

#### Restricții și precizări

- $`1 \leq n \leq 10^{5}`$.
- $`- 10^{7} \leq a_{i},b_{i},c_{i} \leq 10^{7}`$

#### Exemple

##### Exemplul 1

###### Input

Copy

```
3
1 0 -1
-1 0 2
0 1 3
```

###### Output

Copy

```
VOID
```

###### Explicație

Sunt trei semiplane, care au inecuațiile $`x - 1 \leq 0`$, $`- x + 2 \leq 0`$, respectiv $`y + 3 \leq 0`$. Inecuațiile pot fi rescrise $`x \leq 1`$, $`x \geq 2`$, $`y \leq - 3`$.

Deoarece nu există niciun punct în $`\mathbb{R}^{2}`$ care să aibă abscisa mai mică sau egală cu $`1`$ și mai mare sau egală cu $`2`$ în același timp, intersecția este vidă.

##### Exemplul 2

###### Input

Copy

```
4
-1 0 1
1 0 -2
0 1 3
0 -2 -8
```

###### Output

Copy

```
BOUNDED
```

###### Explicație

Sunt patru semiplane, care au inecuațiile $`- x + 1 \leq 0`$, $`x - 2 \leq 0`$, $`y + 3 \leq 0`$, respectiv $`- 2y - 8 \leq 0`$. Inecuațiile pot fi rescrise $`x \geq 1`$, $`x \leq 2`$, $`y \leq - 3`$, $`y \geq - 4`$.

Punctele care întrunesc condiția $`1 \leq x \leq 2`$ sunt cele din fâșia verticală dintre dreptele $`x = 1`$ și $`x = 2`$. Punctele care întrunesc condiția $`- 4 \leq y \leq - 3`$ sunt cele din fâșia orizontală dintre dreptele $`y = - 4`$ și $`y = - 3`$. Intersecția lor este dreptunghiul determinat de punctele $`(1, - 4),(2, - 4),(2, - 3),(1, - 3)`$, deci este o mulțime nevidă și mărginită.

![Semiplanele au intersecția nevidă, mărginită.](https://cms.fmi.unibuc.ro/media/martor/cff08f94-ebb1-4b20-8d36-2bfb403322f7.png)

##### Exemplul 3

###### Input

Copy

```
3
-1 0 1
1 0 -2
0 1 3
```

###### Output

Copy

```
UNBOUNDED
```

###### Explicație

Sunt trei semiplane, care au inecuațiile $`- x + 1 \leq 0`$, $`x - 2 \leq 0`$, respectiv $`y + 3 \leq 0`$. Inecuațiile pot fi rescrise $`x \geq 1`$, $`x \leq 2`$, $`y \leq - 3`$.

Punctele care întrunesc condiția $`1 \leq x \leq 2`$ sunt cele din fâșia verticală dintre dreptele $`x = 1`$ și $`x = 2`$. Condiția $`y \leq - 3`$ ne obligă să le luăm pe cele care au ordonata mai mică sau egală cu $`- 3`$. Prin urmare, intersecția este nevidă și nemărginită.

![Semiplanele au intersecția nevidă, nemărginită.](https://cms.fmi.unibuc.ro/media/martor/5adff468-738b-416c-bc9a-79b7296bd6ce.png)


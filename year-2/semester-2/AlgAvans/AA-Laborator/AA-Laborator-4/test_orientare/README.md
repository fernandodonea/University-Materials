
# Testul de orientare


#### Descriere

Se dau trei puncte în plan, $`P,Q,R`$, de coordonate $`P = (x_{P},y_{P})`$, $`Q = (x_{Q},y_{Q})`$ și $`R = (x_{R},y_{R})`$. Să se stabilească poziția punctului $`R`$ față de dreapta $`PQ`$, folosind testul de orientare descris în [cursul 8](https://drive.google.com/file/d/1ZVmLnqESDYEbMRfNU_Zmwe9xUMpjzQhF/view).

#### Date de intrare

Se va citi de la tastatură $`t`$, reprezentând numărul de teste. Următoarele $`t`$ linii vor descrie fiecare câte un test. Fiecare linie conține șase numere întregi: $`x_{P}`$, $`y_{P}`$, $`x_{Q}`$, $`y_{Q}`$, $`x_{R}`$ și $`y_{R}`$, reprezentând coordonatele punctelor $`P`$, $`Q`$, $`R`$.

#### Date de ieșire

Pentru fiecare test se va afișa, pe câte un rând separat, un mesaj corespunzator pozitiei punctului $`R`$:

- `LEFT` (dacă punctul $`R`$ se află *la stânga* dreptei $`PQ`$)
- `RIGHT` (dacă punctul $`R`$ se află *la dreapta* dreptei $`PQ`$)
- `TOUCH` (dacă punctul $`R`$ se află *pe* dreapta $`PQ`$)

#### Restricții și precizări

- $`1 \leq t \leq 10^{5}`$
- $`- 10^{9} \leq x_{p},y_{p},x_{q},y_{q},x_{r},y_{r} \leq 10^{9}`$

De asemenea, trebuie să aveți în vedere că în mediul de lucru de pe CMS **nu** aveți posibilitatea să importați biblioteci externe (de exemplu, nu puteți importa `numpy` ca să folosiți `numpy.linalg.det`).

#### Exemplu

##### Input

Copy

```
3
1 1 5 3 2 3
1 1 5 3 4 1
1 1 5 3 3 2
```

##### Output

Copy

```
LEFT
RIGHT
TOUCH
```

##### Explicație

Datele de mai sus corespund următoarei situații:

\
[proudly powered by **DMOJ**](https://dmoj.ca/) \|

català (ca) Deutsch (de) Ελληνικά (el) English (en) español (es) français (fr) Hrvatski (hr) Magyar (hu) 日本語 (ja) Қазақ (kk) 한국어 (ko) Português (pt) Română (ro) Русский (ru) srpski (latinica) (sr-latn) Türkçe (tr) Tiếng Việt (vi) 简体中文 (zh-hans) 繁體中文 (zh-hant)
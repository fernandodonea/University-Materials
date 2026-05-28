# Poziția unui punct față de cercul circumscris unui triunghi


#### Descriere

Implementați un algoritm care să determine poziția relativă a unui punct $`P`$ față de cercul circumscris unui triunghi $`\Delta ABC`$. Puteți folosi criteriul numeric descris în [cursul 10](https://drive.google.com/file/d/1hCTkJIUfRL0X1b6R7BncbPzD3i0crp6K/view?usp=sharing).

#### Date de intrare

Programul va citi trei perechi de numere întregi $`x_{A}y_{A}`$, $`x_{B}y_{B}`$ și $`x_{C}y_{C}`$, pe linii distincte, reprezentând coordonatele vârfurilor triunghiului $`\Delta ABC`$, parcurse în sens trigonometric.

Pe următorul rând se află un număr natural $`m`$, reprezentând numărul de puncte ale căror poziții relative trebuie determinate, și apoi $`m`$ perechi de numere întregi separate prin spațiu $`x_{j}y_{j}`$, pe linii distincte, reprezentând coordonatele punctului $`P_{j}(x_{j},y_{j})`$.

#### Date de ieșire

Programul va afișa $`m`$ rânduri, pe fiecare aflându-se una dintre următoarele valori:

- `INSIDE`, dacă punctul se află în interiorul cercului circumscris triunghiului $`\Delta ABC`$;
- `BOUNDARY`, dacă punctul se află pe cercul circumscris triunghiului $`\Delta ABC`$;
- `OUTSIDE`, dacă punctul se află în exteriorul cercului circumscris triunghiului $`\Delta ABC`$.

#### Restricții și precizări

- $`1 \leq m \leq 10^{5}`$
- $`- 10^{9} \leq x,y \leq 10^{9}`$

#### Exemple

##### Input

Copy

```
-2 4
-3 0
0 -2
3
1 2
3 3
6 -1
```

##### Output

Copy

```
INSIDE
BOUNDARY
OUTSIDE
```

##### Explicație

Exemplul de mai sus corespunde următoarei situații:

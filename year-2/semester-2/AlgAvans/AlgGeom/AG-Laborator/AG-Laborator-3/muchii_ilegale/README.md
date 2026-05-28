# Muchii ilegale


#### Descriere

Implementați un algoritm care să verifice dacă o muchie a unei triangulări este legală. Puteți folosi folosi problema [1](https://cms.fmi.unibuc.ro/problem/l7pb1), bazată pe criteriul geometric/numeric descris în [cursul 10](https://drive.google.com/file/d/1hCTkJIUfRL0X1b6R7BncbPzD3i0crp6K/view?usp=sharing).

#### Date de intrare

Programul va citi de la tastatură patru perechi de numere întregi separate prin spațiu $`x_{i}y_{i}`$, pe linii distincte, reprezentând coordonatele vârfului $`P_{i}(x_{i},y_{i})`$ al patrulaterului. Vârfurile sunt date în sens trigonometric, iar patrulaterul este convex.

#### Date de ieșire

Programul va afișa pe ecran două rânduri, pe primul aflându-se șirul de caractere `AC:`, urmat de un spațiu și apoi cuvântul `LEGAL` sau `ILLEGAL`; iar pe al doilea, șirul de caractere `BD:`, urmat de un spațiu și apoi cuvântul `LEGAL` sau `ILLEGAL`.

Primul rând indică dacă muchia $`AC`$ este legală, iar al doilea rând indică dacă muchia $`BD`$ este legală.

#### Restricții și precizări

- $`- 10^{6} \leq x,y \leq 10^{6}`$

#### Exemplu

##### Input

Copy

```
-2 4
-3 0
0 -2
1 2
```

##### Output

Copy

```
AC: ILLEGAL
BD: LEGAL
```

##### Explicație

Coordonatele de mai sus corespund următorului poligon:

Folosind criteriul geometric observăm că:

- Punctul $`D`$ este în interiorul cercului circumscris triunghiului $`\Delta ABC`$, deci muchia $`AC`$ este ilegală.
- Punctul $`A`$ este în exteriorul cercului circumscris triunghiului $`\Delta BCD`$, deci muchia $`BD`$ este legală.


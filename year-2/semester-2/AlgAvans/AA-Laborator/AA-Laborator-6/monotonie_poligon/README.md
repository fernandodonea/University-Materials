# Monotonia unui poligon

#### Descriere

Implementați un algoritm de complexitate de timp liniară care să verifice dacă un poligon \\(P\_1P\_2 \\dots P\_n\\) este monoton în raport cu axa \\(Ox\\), respectiv \\(Oy\\), folosind metoda dreptei de baleiere, descrisă în cursul 9.

#### Date de intrare

Programul va citi de la tastatură un număr natural \\(n\\), reprezentând numărul de vârfuri ale poligonului, și apoi \\(n\\) perechi de numere întregi separate prin spațiu \\(x\_i \\ y\_i\\), pe linii distincte, reprezentând coordonatele vârfului \\(P\_i (x\_i, y\_i)\\) al poligonului.

#### Date de ieșire

Programul va afișa exact **două** rânduri, pe fiecare aflându-se unul dintre șirurile de caractere `YES` sau `NO`.

Primul rând va indica dacă poligonul dat este \\(x\\)-monoton, iar al doilea rând indică dacă este \\(y\\)-monoton.

#### Restricții și precizări

-   \\(3 \\leq n \\leq 1\\,000\\,000\\)
-   \\(-10^9 \\leq x, y \\leq 10^9\\)

#### Exemple

##### Exemplul 1

###### Input

```
8
-3 -1
-1 -4
9 -2
7 1
4 2
2 4
1 8
-2 6
```

###### Output

```
YES
YES
```

###### Explicație

Poligonul dat este atât \\(x\\)-monoton, cât și \\(y\\)-monoton.

Explicație pentru \\(x\\)-monotonie: vârful \\(P\_1\\), situat cel mai la stânga (cu cel mai mic \\(x\\)) este unit cu vârful \\(P\_3\\), situat cel mai la dreapta (cu cel mai mare \\(x\\)) prin două lanțuri: \\(P\_1P\_2P\_3\\), respectiv \\(P\_1P\_8P\_7P\_6P\_5P\_4P\_3\\). În ambele cazuri parcurgerea se efectuează de la stânga la dreapta (coordonata \\(x\\) crește). Se poate observa că intersecția dintre o dreaptă verticală oarecare și poligon este mulțimea vidă sau un punct sau un segment (de fapt, este o mulțime conexă, formată "dintr-o singură bucată").

Explicație pentru \\(y\\)-monotonie: vârful \\(P\_7\\), situat cel mai sus (cu cel mai mare \\(y\\)) este unit cu vârful \\(P\_2\\) situat cel mai jos (cu cel mai mic \\(y\\)) prin două lanțuri: \\(P\_7P\_8P\_1P\_2\\), respectiv \\(P\_7P\_6P\_5P\_4P\_3P\_2\\). În ambele cazuri parcurgerea se efectuează de sus în jos (coordonata \\(y\\) descrește). Se poate observa că intersecția dintre o dreaptă orizontală oarecare și poligon este mulțimea vidă sau un punct sau un segment.

##### Exemplul 2

###### Input

```
7
0 5
2 3
1 -1
6 -2
4 2
8 6
3 9
```

###### Output

```
NO
YES
```

###### Explicație

Poligonul dat nu este \\(x\\)-monoton, dar este \\(y\\)-monoton.

Poligonul nu este \\(x\\)-monoton. Putem observa că pe lanțul \\(P\_1 P\_2 P\_3 P\_4, \\dots\\) coordonata \\(x\\) a punctelor crește, apoi scade și crește din nou. Se poate observa că există drepte verticale (de exemplu dreapta de ecuație \\(x=5\\)) pentru care intersecția cu poligonul este reuniunea a două segmente (o astfel de mulțime nu este conexă, ea are două componente conexe).

Poligonul dat este \\(y\\)-monoton. Vârful \\(P\_7\\), situat cel mai sus (cu cel mai mare \\(y\\)), este unit cu vârful \\(P\_4\\), situat cel mai jos (cu cel mai mic \\(y\\)), prin două lanțuri: \\(P\_7P\_1P\_2P\_3P\_4\\), respectiv \\(P\_7P\_6P\_5P\_4\\). În ambele cazuri parcurgerea se efectuează de sus în jos (adică \\(y\\) descrește). Se poate observa că intersecția dintre o dreaptă orizontală și poligon este mulțimea vidă sau un punct sau un segment.

##### Exemplul 3

###### Input

```
8
9 9
5 5
6 9
4 4
-1 2
7 1
3 2
10 3
```

###### Output

```
NO
NO
```

###### Explicație

Poligonul dat nu este nici \\(x\\)-monoton, nici \\(y\\)-monoton. Pe lanțul \\(P\_5P\_6P\_7P\_8\\) coordonata \\(x\\) crește, apoi descrește, apoi crește din nou, deci poligonul nu este \\(x\\)-monoton. Un argument analog poate fi utilizat pentru a arăta că poligonul nu este \\(y\\)-monoton (găsiți un lanț care "obstrucționează" \\(y\\)-monotonia).
# SD Model-colocviu
## ex 1

Fiind sătul de erorile Windows-ului, Z decide să își instaleze Linux. 
Primele comenzi de terminal pe care acesta le învață sunt  `cd` și `pdw`.

Pentru a se familiariza cu comenzile de terminal acesta decide să rezolve următoarea problemă: Fiind date  comenzi de forma `cdx` sau `pwd`, să se proceseze aceste comenzi și să se afișeze pe ecran rezultatul fiecărei comenzi . 
Se garantează că  poate lua doar valorile  sau numele unui subdirector al directorului curent. Înainte de citirea comenzilor vom presupune că directorul actual este `/`.

### Input Format

Se citesc de la tastatura  comenzi de forma:

`cd ..`Aceasta comandă ne întoarce în directorul parinte al celui actual. Daca ne aflam in  atunci comanda nu are niciun efect.

`cd x` Aceasta comandă ne duce în subdirectorul  al directorului actual. Se garantează că directorul actual are subdirectorul .

`pwd` Aceasta comandă afiseaza directorul în care ne aflăm. Pentru simplitate vom considera că afișează doar numele directorului actual (nu întreaga cale). Dacă efectuăm comanda  când ne aflăm în directorul  atunci vom afișa .

### Constraints



Lungimea șirului  în cadrul comenzii  este maxim 10.

1<=n<=10^5

Rezolvați această problemă în timp  folosind o stivă implementată de voi.

### Output Format

Se afișează pe ecran rezultatul fiecarei comenzi . Fiecare rezultat se afișează pe o linie nouă.

#### Sample Input 0

```
5
cd abc
cd bbb
pwd
cd ..
pwd
```

#### Sample Output 0
```
bbb
abc
```

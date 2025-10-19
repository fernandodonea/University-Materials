# SD Model-colocviu
## ex 2


Se consideră un șir cu  elemente numere întregi și un număr întreg `x`. 
Să se determine cele mai apropiate `k` valori din  față de `x`. 

Un număr  este mai aproape de  decât  dacă:
- | a - x | < | b - x |
- | a - x| = | a - b| si a < b

### Input Format

Se citesc de la tastatură 3 valori , apoi  valori reprezentând valorile șirului .

### Constraints
1<=k<=10^5
1<=n<=10^6
-10^6<=x[i]<=10^6

### Output Format

Se afișează pe ecran, pe o singură linie separate prin spațiu  valori (în orice ordine) reprezentand cele mai apropiate  valori față de .

#### Sample Input 0
```
5 3 2
0 3 4 0 5
```

#### Sample Output 0
```
0 0 3
``` 

---
## Metoda de rezolvare

Folosim un **MAX HEAP** (cea mai proasta valoarea este cea mai mare) cu `k` elemente

Pentru fiecare nod tinem minte distanta fata de x si valoarea sa.
```
n=5
k=3
x=2

0 3 0 4 0 5
```
```
MaxHeap(2,0)
MaxHeap(1,3)
MaxHeap(2,4) ->vf heap
```
pt 0 (2,0) mai bun decat (2,4) ->inlocuim varful

Complexitate **O(n logk)**

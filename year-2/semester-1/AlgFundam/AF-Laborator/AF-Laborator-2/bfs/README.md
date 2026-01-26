# BFS - Parcurgere in latime


Se considera un graf orientat cu N varfuri si M arce.
# Cerinta
Fiind dat un nod S, sa se determine, pentru fiecare nod X, numarul minim de arce ce trebuie parcurse pentru a ajunge din nodul sursa S la nodul X.

# Date de intrare
Fisierul de intrare bfs.in contine pe prima linie 3 numere intregi N M S, cu semnificatia din enunt. Urmatoarele M linii contin cate doua numere x y, cu semnificatia ca exista arc orientat de la x la y.

# Date de iesire
In fisierul de iesire bfs.out se vor afla N numere separate prin spatiu cu semnificatia ca al i-lea numar reprezinta numarul minim de arce ce trebuie parcurse de la nodul S la nodul i.

# Restrictii
2 ≤ N ≤ 100 000
1 ≤ M ≤ 1 000 000
Daca nu se poate ajunge din nodul S la nodul i, atunci numarul corespunzator numarului i va fi -1.
## Exemplu
bfs.in	
```
5 7 2
1 2
2 1
2 2
3 2
2 5
5 3
4 5
```
bfs.out
```
1 0 2 -1 1
```
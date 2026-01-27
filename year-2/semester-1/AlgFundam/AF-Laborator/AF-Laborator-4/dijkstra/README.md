

# Algoritmul lui Dijkstra

[Infoarena](https://www.infoarena.ro/problema/dijkstra)


Se da un graf orientat cu N noduri si M arce.

## Cerinta
Sa se determine lungimea minima a drumului de la nodul 1 la fiecare din nodurile 2, 3, ..., N-1, N si sa se afiseze aceste lungimi. Lungimea unui drum este data de suma lungimilor arcelor care constituie drumul.

## Date de intrare
Fisierul de intrare dijkstra.in contine pe prima linie numerele N si M, separate printr-un spatiu, cu semnificatia din enunt. Urmatoarele M linii contin, fiecare, cate 3 numere naturale separate printr-un spatiu A B C semnificand existenta unui arc de lungime C de la nodul A la nodul B.

## Date de iesire
In fisierul de iesire dijkstra.out veti afisa pe prima linie N-1 numere naturale separate printr-un spatiu. Al i-lea numar va reprezenta lungimea unui drum minim de la nodul 1 la nodul i+1.

## Restrictii
1 ≤ N ≤ 50 000
1 ≤ M ≤ 250 000
Lungimile arcelor sunt numere naturale cel mult egale cu 20 000.
Pot exista arce de lungime 0
Nu exista un arc de la un nod la acelasi nod.
Daca nu exista drum de la nodul 1 la un nod i, se considera ca lungimea minima este 0.
Arcele date in fisierul de intrare nu se repeta.
## Exemplu
dijkstra.in	
```
5 6
1 2 1
1 4 2
4 3 4
2 3 2
4 5 3
3 5 6
```
dijkstra.out
```
1 3 2 5
```





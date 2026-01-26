# Arbore partial de cost minim

Se da un graf conex neorientat G cu N noduri si M muchii, fiecare muchie avand asociat un cost. Se cere sa se determine un subgraf care cuprinde toate nodurile si o parte din muchii, astfel incat subgraful determinat sa aiba structura de arbore si suma costurilor muchiilor care il formeaza sa fie minim posibila. Subgraful cu proprietatile de mai sus se va numi arbore partial de cost minim pentru graful dat.

# Date de intrare
Fisierul de intrare apm.in va contine pe prima linie numerele N si M, separate printr-un spatiu. Pe urmatoarele M linii se vor gasi muchiile grafului sub forma X Y C, cu semnificatia ca exista muchie neorientata intre X si Y de cost C.

# Date de ieşire
Fisierul de iesire apm.out va contine pe prima linie costul arborelui partial de cost minim. Pe a doua linie se va gasi numarul de muchii din arborele partial selectat. Fiecare din urmatoarele linii, pana la sfarsitul fisierului de iesire, va contine cate doua numere naturale, capetele unei muchii ce apartine arborelui solutie. Muchiile pot fi afisate in orice ordine. Daca sunt mai multe solutii corecte se poate afisa oricare.

# Restricţii
1 ≤ N ≤ 200 000
1 ≤ M ≤ 400 000
-1 000 ≤ C ≤ 1 000
Pentru 20% din teste N, M ≤ 20
Pentru inca 20% din teste N ≤ 800 si M ≤ 1 500


# Exemple
apm.in
```
9 14
1 2 10
1 3 -11
2 4 11
2 5 11
5 6 13
3 4 10
4 6 12
4 7 5
3 7 4
3 8 5
8 7 5
8 9 4
9 7 3
6 7 11
```
apm.out
```
37
8
3 1
7 9
7 3
9 8
7 4
2 1
5 2
7 6
```

Exemplu 2

apm.in
```
3 3
1 2 -3
2 3 -4
3 1 -5
```

apm.in
```
-9
2
1 3
3 2
```
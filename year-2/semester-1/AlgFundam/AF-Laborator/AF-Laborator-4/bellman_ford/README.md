# Algoritmul Bellman-Ford

[Infoarena](https://www.infoarena.ro/problema/bellmanford)

Se dă un graf orientat conex cu N noduri şi M muchii cu costuri. Definim un lanţ ca fiind un şir de noduri cu proprietatea că între oricare două consecutive există o muchie. Costul unui lanţ este dat de suma costurilor muchiilor care unesc nodurile ce îl formează. Definim un ciclu ca fiind un lanţ cu proprietatea că primul element al său este egal cu ultimul.

# Cerinţă
Să se determine dacă în graful dat există un ciclu de cost negativ. Dacă nu există, să se determine costul minim al unui lanţ de la nodul 1 la fiecare dintre nodurile 2, 3, ... , N-1, N.

# Date de intrare
Fişierul de intrare bellmanford.in conţine pe prima linie numerele N şi M cu semnificaţia din enunţ. Pe următoarele M linii se vor afla câte 3 numere x, y şi c cu semnificaţia că există o muchie de cost c de la nodul x la nodul y.

# Date de ieşire
În fişierul de ieşire bellmanford.out se va afişa pe prima linie mesajul "Ciclu negativ!" dacă în graf există un astfel de ciclu sau, în caz contrar, N-1 numere separate printr-un spaţiu. Al i-lea număr va reprezenta costul minim al unui lanţ de la nodul 1 la nodul i+1.

# Restricţii
1 ≤ N ≤ 50 000.
1 ≤ M ≤ 250 000.
Costurile muchiilor sunt numere întregi cel mult egale în modul cu 1 000.
# Exemplu
bellmanford.in
```
5 8
1 3 -3
1 5 7
3 2 -2
3 4 7
5 1 4
5 2 3
5 3 4
4 5 3
```

bellmanford.out
```
-5 -3 4 7
```
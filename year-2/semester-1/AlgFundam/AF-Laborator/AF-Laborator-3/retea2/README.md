# Retea2

Damia s-a hotarat sa-si deschida N centrale electrice. In orasul ei sunt M blocuri care trebuie sa primeasca curent. Un bloc primeste curent eletric daca este conectat la alt bloc care primeste curent electric sau daca este conectat la o centrala eletrica. Stiindu-se coordonatele celor N centrale si a celor M blocuri, si stiindu-se faptul ca pentru a conecta doua dintre aceste puncte trebuie platit un cost egal cu distanta euclidiana dintre ele, ajutati-o pe Damia sa determine costul minim pentru a transmite curent eletric catre toate blocurile.

# Date de intrare
Fişierul de intrare retea2.in se gasesc doua numere naturale N si M. Pe ficare dintre urmatoarele N linii se va gasi cate o pereche de numere intregi reprezentand coordonatele in plan ale unei centrale. Pe fiecare dintre urmatoarele M linii se va gasi cate o pereche de numere intregi reprezentand coordonatele unui bloc de locutine.

# Date de ieşire
În fişierul de ieşire retea2.out se va gasi un singur numar real, reprezentand costul minim pentru a transmite curent eletric blocurilor in modul descris in enunt.

# Restricţii
1 ≤ N ≤ 2000
0 ≤ M ≤ 2000
Coordonatele punctelor vor fi mai mici in modul ca 106.
Rezultatul trebuie afisat cu o precizie de 6 zecimale.
Pentru teste in valoare de 50 puncte, N + M ≤ 1000.
Pentru teste in valoare de 20 puncte, N,M ≤ 10.
# Exemplu
retea2.in	
```
2 2
0 0
10 11
10 0
0 10
```
retea2.out
```
20.000000
```
Explicaţie
Ambele blocuri sunt conectate la centrala situata in 0,0.
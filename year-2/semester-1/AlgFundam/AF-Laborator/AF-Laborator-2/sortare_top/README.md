# Sortare topologica

O sortare topologica a varfurilor unui graf orientat aciclic este o operatie de ordonare liniara a varfurilor, astfel incat, daca exista un arc ( i, j ), atunci i apare inaintea lui j in aceasta ordonare.

# Date de intrare
In fisierul de intrare sortaret.in vom avea pe prima linie doua numere intregi N si M. Pe fiecare dintre urmatoarele M linii se vor afla cate doua numere intregi, separate intre ele printr-un spatiu, X si Y, cu semnificatia ca exista arc de la nodul X catre nodul Y.

# Date de iesire
Fisierul de iesire sortaret.out va contine pe o singura linie N numere separate intre ele prin spatii, care reprezinta sortarea topologica a nodurilor grafului dat. Daca exista mai multe solutii se va afisa oricare.

Restrictii
1 ≤ N ≤ 50000
1 ≤ M ≤ 100000
Pot exista mai multe arce intre doua noduri X si Y
Exemplu
sortaret.in	
```
9 8
1 2
1 3
3 4
3 5
5 9
4 6
4 7
4 8
```
sortaret.out
```
1 2 3 4 6 7 8 5 9
```
Indicatii de rezolvare
O scurta prezentare a acestui subiect gasiti aici
Algoritmul de Sortare Topologica il gasiti foarte bine explicat si in cartea Introducere in algoritmi, Thomas Cormen, editura Agora, Cluj-Napoca.
O idee de rezolvare este sa introducem, pe rand, intr-o lista, nodurile care la un moment dat un gradul exterior zero. Odata ce un nod este introdus in lista, vom scoate nodul respectiv din graf si vom considera in continuare graful ramas. O implementare directa are complexitatea O(N2) si se gaseste aici. Daca rafinam aceasta idee, introducand succesiv nodurile intr-o coada, putem obtine complexitatea O(N+M), sursa se gaseste aici.
O alta posibila idee de rezolvare consta intr-o parcurgere in adancime pentru a calcula timpii de terminare pentru fiecare varf v. Pe masura ce fiecare varf este terminat, este inserat in capul unei liste simplu inlantuite. Parcurgerea listei va constitui solutia. Acest algoritm are o complexitate de O(N+M) deoarece cautarea in adancime necesita un timp O(N+M) iar inserarea fiecaruia din cele |N| varfuri in capul liste simplu inlantuite necesita timp O(1). Sursa se gaseste aici.
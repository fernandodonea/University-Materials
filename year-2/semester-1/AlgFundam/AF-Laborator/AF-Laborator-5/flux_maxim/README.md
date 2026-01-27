# Flux maxim

O retea de transport este un graf orientat in care fiecare muchie are asociata o capacitate si o anumita cantitate de flux. Fluxul primit de fiecare muchie trebuie sa fie mai mic sau egal decat capacitatea acesteia. De asemenea, pentru fiecare nod, fluxul care intra in nod trebuie sa fie egal cu cantitatea de flux care iese din nod. Cu alte cuvinte, suma fluxurilor asociate muchiilor care intra intr-un nod trebuie sa fie egala cu suma fluxurilor asociate muchiilor care ies din nod, exceptie facand nodurile speciale S si D, denumite sursa, respectiv, destinatie. Din nodul sursa poate doar iesi flux, in timp ce in nodul destinatie poate doar intra flux. Valoarea fluxului unei astfel retele este egal cu suma fluxului care iese din sursa sau cu suma fluxului care intra in destinatie (cele doua fluxuri sunt egale).

# Cerinta 
Dandu-se o retea de transport, in care initial fluxul pe fiecare muchie este 0, sa se calculeze fluxul maxim care poate fi trimis prin aceasta retea.

# Date de intrare
Fisierul de intrare maxflow.in va contine pe prima linie 2 numere, N si M, reprezentand numarul de noduri si numarul de muchii din retea. Pe fiecare din urmatoarele M linii, se vor afla cate 3 numere naturale, x, y si z, cu semnificatia ca exista o muchie care porneste de la nodul x, ajunge in nodul y si are capacitatea z.

# Date de ieşire
In fisierul de iesire maxflow.out se va afla un singur numar F, reprezentand fluxul maxim ce poate fi trimis prin retea.

# Restricţii
2 ≤ N ≤ 1 000
1 ≤ M ≤ 5 000
Nodul 1 este nodul sursa, iar nodul N este nodul destinatie.
Pentru fiecare muchie, capacitatea va fi un numar natural in intervalul [1, 110 000].
Nu exista nici o muchie x y astfel incat x sa fie egal cu N sau y sa fie egal cu 1.
Intre oricare doua noduri x si y exista maxim un arc, însă arcele x -> y şi y -> x pot exista simultan.
In practica, retelele de flux contin adesea un numar mare de noduri vecine cu destinatia. Testele folosite la evaluarea vitezei algoritmului de flux de la aceasta problema au aceeasi proprietate.
Exemplu
maxflow.in	maxflow.out
4 5
1 2 3
1 3 5
2 4 6
3 4 4
3 2 3
8
Explicaţie
Fluxul maxim care poate fi trimis din sursa catre destinatie este 8 si este trimis astfel:



In figura de mai sus, fiecare muchie are asociate 2 numere reprezentand fluxul si capacitatea asociate muchiei respective.

Indicaţii de rezolvare
Pentru a rezolva aceasta problema putem folosi algoritmul Edmonds-Karp. Acest algoritm introduce insa o notiune noua, anume aceea de graf rezidual. Graful rezidual este graful retelei de transport, in care pentru fiecare muchie introducem si muchia inversa, cu capacitate 0. La fiecare pas trebuie sa gasim in acest graf un drum de la sursa la destinatie, in care fiecare muchie de pe drum sa aiba fluxul asociat pana in acest moment strict mai mic decat capacitatea sa. Putem face acest lucru usor, folosind un algoritm de parcurgere a grafurilor precum BFS sau DFS. Drumul astfel gasit se va numi drum de ameliorare. Dupa acest pas, calculam valoarea cu care putem mari fluxul pe acest drum, aceasta fiind valoarea minima cu care poate fi marit fluxul asociat fiecarei muchii care se afla pe drumul gasit. Odata gasita aceasta valoare, luam fiecare muchie x -> y si marim fluxul pe aceasta muchie cu acea valoare, scazand de asemena tot aceasi valoare pe muchia y -> x. Astfel este posibil ca drumul nostru la un moment dat sa parcurga o muchie inversata, de capacitate 0 si flux negativ, practic decrementand fluxul de pe muchia neinversata. Acest algoritm garanteaza ca in momentul in care nu vom mai gasi niciun drum de la sursa la destinatie in graful rezidual, atunci fluxul trimis prin retea este maxim. Complexitatea teoretica este O(N * M2), insa in practica se comporta mult mai bine. Acest algoritm ar trebui sa obtina in jur de 70 de puncte. O sursa pe aceasta idee se gaseste aici.

Pentru 100 de puncte trebuie facuta o optimizare. Astfel, la fiecare pas construim arborele BFS (excluzand destinatia), si acum un drum de la sursa la destinatie e reprezentat de un drum de la sursa (care este radacina arborelui) la o frunza legata de destinatie printr-o muchie nesaturata. Astfel putem la un pas sa marim fluxul pe un numar maximal de astfel de drumuri, fara a mai reface BFS-ul. Aceasta optimizare reduce destul de mult timpul de executie si obtine 100 de puncte. O sursa care foloseste si aceasta optimizare se gaseste aici.
Pentru mai multe detalii puteti consulta si acest articol.

Exista si algoritmi mai buni pentru a rezolva aceasta problema, nefiind insa necesari la aceasta problema, cum ar fi algoritmul lui Dinic si algoritmul lui Karzanov.

Aplicaţii
Algoritmul de flux maxim este un algoritm foarte important, cu ajutorul lui fiind posibil sa rezolvam multe probleme. Aici se afla o lista de probleme care se rezolva folosind flux maxim:

Critice
Senat
Drumuri2
Two Shortest
Trafic
Paznici
Taramul Nicaieri
Croco
Joc4
Optimal Marks
WorkersOnPlane

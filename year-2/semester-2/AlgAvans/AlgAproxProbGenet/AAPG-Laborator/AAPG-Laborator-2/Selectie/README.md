# Algoritmi genetici - selecție 

#### Descriere

##### Context

Într-un algoritm genetic, după ce am generat o populație de cromozomi care codifică soluții fezabile pentru problema noastră, aplicăm operații ca să evoluăm populația către soluția optimă. Primul pas este să [selectăm](https://en.wikipedia.org/wiki/Selection_(genetic_algorithm)) care indivizi trec în etapele următoare ale algoritmului (e.g. care cromozomi participă la recombinare, care cromozomi vor fi mutați etc.). Putem selecta cromozomii într-un mod complet aleator, dar ar fi bine să luăm în considerare și _fitness-ul_ indivizilor (cât de bună este soluția pe care o reprezintă). O metodă pe care o putem folosi este [selecția proporțională bazată pe fitness](https://en.wikipedia.org/wiki/Fitness_proportionate_selection), cunoscută și ca _metoda ruletei_.

##### Cerință

Vrem să găsim punctul de maxim al unei funcții polinomiale de forma f(x)=a x 2+b x+c (cu a<0).

Presupunem că avem o populație formată din n cromozomi, fiecare identificat după un indice i=0,n−1―. Vom nota valoarea codificată de cromozomul i cu x i∈R și fitness-ul acestuia cu f i=f(x i)>0. Fitness-ul total al populației de cromozomi este F=∑i=0 n−1 f(x i).

Pentru a putea aplica metoda ruletei, trebuie să împărțim intervalul [0,1] în n intervale consecutive [p 0,p 1), [p 1,p 2), …, [p n−1,p n] cu 0=p 0<p 1<⋯<p n−1<p n=1, astfel încât lungimea intervalului [p i,p i+1) să corespundă cu _fitness-ul relativ_ al cromozomului i, adică f(x i)/F.

Obiectivul vostru este să determinați capetele acestor intervale, fiind date valorile fiecărui cromozom (ca numere reale).

#### Date de intrare

Se citesc de la tastatură a, b și c, trei numere întregi care reprezintă coeficienții polinomului a x 2+b x+c. Pe următoarea linie se va citi numărul natural n, dimensiunea populației de cromozomi, iar pe următoarea linie un șir de n numere reale (x 0, x 1, …, x n−1), separate prin câte un spațiu, fiecare reprezentând valoarea (decodificată) a unui cromozom din populației.

#### Date de ieșire

Afișați capetele intervalelor de selecție 0=p 0<p 1<⋯<p n−1<p n=1, care vor fi folosite ulterior pentru selecția cromozomilor prin metoda ruletei.

#### Restricții și precizări

*   −10<a<0
*   −10<b,c<10
*   1≤n≤100
*   Presupunem că f(x i) va fi pozitiv pentru toți cromozomii primiți ca date de intrare. Prin urmare, puteți presupune și că fitness-ul total F va fi un număr real pozitiv.
*   Puteți afișa numerele reale cu oricâte zecimale, dar trebuie să fie corecte cu o precizie de cel puțin 4 zecimale (i.e. eroarea absolută între ce afișați și răspunsul corect să fie cel mult 10−4).

#### Exemplul 1

##### Input

```
-1 4 -1
3
1 1.5 2.5
```

##### Output

```
0.000000
0.266666
0.633333
1.000000
```

##### Explicație

Funcția pe care vrem să o maximizăm este f(x)=−x 2+4 x−1.

Valorile de fitness ale celor trei cromozomi sunt f 0=f(x 0)=2, f 1=f(x 1)=2.75 și f 2=f(x 2)=2.75.

Suma acestor valori este F=2+2.75+2.75=7.5.

Calculând sumele parțiale ale fitness-urilor și împărțindu-le la suma valorilor, obținem capetele intervalelor de selecție:

*   p 0=0/7.5=0
*   p 1=2/7.5≈0.2666
*   p 2=(2+2.75)/7.5≈0.6333
*   p 3=(2+2.75+2.75)/7.5=1

Observați că intervalele [p 1,p 2] și [p 2,p 3] au aceeași lungime, deoarece corespund la doi cromozomi cu același fitness. În schimb, intervalul asociat primului cromozom este mai scurt, acesta având un fitness mai mic.

#### Exemplul 2

##### Input

```
-1 -1 2
2
-1 0
```

##### Output

```
0.0
0.5
1.0
```

##### Explicație

Funcția pe care vrem să o maximizăm este f(x)=−x 2−x+2.

Avem doi indivizi în populație, cu fitness-urile f 0=f(x 0)=2 și f 1=f(x 1)=2.

Suma acestor valori este F=2+2=4.

Calculând sumele parțiale ale fitness-urilor și împărțindu-le la suma valorilor, obținem capetele intervalelor de selecție:

*   p 0=0/4=0
*   p 1=2/4=0.5
*   p 2=(2+2)/4=1

Am obținut două intervale de lungime egală deoarece ambii cromozomi au același fitness (deci reprezintă puncte diferite din domeniu).

#### Exemplul 3

##### Input

```
-3 9 2
4
0 1 1.5 3
```

##### Output

```
0
0.09638
0.48192
0.90361
1
```

##### Explicație

Funcția pe care vrem să o maximizăm este f(x)=−3 x 2+9 x+2.

Avem patru indivizi în populație, cu fitness-urile f 0=f(x 0)=2, f 1=f(x 1)=8, f 2=f(x 2)=8.75 și f 3=f(x 3)=2.

Suma acestor valori este F=2+8+8.75+2=20.75.

Calculând sumele parțiale ale fitness-urilor și împărțindu-le la suma valorilor, obținem capetele intervalelor de selecție:

*   p 0=0/20.75=0
*   p 1=2/20.75≈0.0963
*   p 2=(2+8)/20.75≈0.4819
*   p 3=(2+8+8.75)/20.75≈0.9036
*   p 4=(2+8+8.75+2)/20.75=1
# Acoperire cu intervale

Managerul unui renumit spital din capitală trebuie să programeze turele la camera de gardă și vrea să se asigure că reușește să facă acest lucru cu cât mai puțini medici.

El are un interval de timp  pe care trebuie să-l acopere cu cei  doctori care sunt angajați la spital. Însă doctorii nu sunt dispuși să stea oricând și oricât timp la camera de gardă, așa că fiecare doctor are un interval de timp  în care este dispus să stea de gardă.

Managerul trebuie să aleagă care dintre acești medici vor sta de gardă. Nu este nicio problemă dacă la un anumit moment ajung să fie doi (sau mai mulți) doctori asignați la camera de gardă, dar trebuie ca pe tot parcursul intervalului  să fie cel puțin o persoană acolo.

Îl puteți ajuta pe manager să decidă ce doctori ar trebui să fie programați, în așa fel încât să acopere tot intervalul , iar numărul acestora să fie cât mai mic?

## Date de intrare

Pe prima linie se vor afla două numere întregi a  și  b reprezentând capetele intervalului [a,b] . Pe următoarea linie se va afla un număr natural N, reprezentând numărul de medici angajați la spital (da, e un spital foarte mare). Pe următoarele N linii se află perechi de numere întregi separate prin spațiu a_i,b_i  reprezentând capetele intervalelor , [a_i,b_i].
 

## Date de ieșire

Răspunsul vostru trebuie scris pe două rânduri. Pe primul rând, un număr natural K, numărul de intervale pe care le-ați ales pentru a forma soluția voastră. Pe al doilea rând, veți scrie K numere naturale separate prin spațiu,i_1,i_2,...i_k , reprezentând indicii (porniți de la 1 ) ale intervalelor alese.

Dacă nu există nicio alegere a intervalelor  astfel încât să acoperim întregul interval , afișați doar 0.

### Exemple

Exemplul 1

Input

```
3 8
5
1 4
3 5
4 9
5 7
6 8
```
Output

```
2
1 3
```
Explicație

Luând intervalul [1,4]  și  [4,9] obținem [1,9], care acoperă intervalul [3,8].

### Exemplul 2

Input

```
3 8
3
1 4
4 5
7 9
```
Output

```
0
```
Explicație

Chiar dacă luăm toate intervalele, nu putem acoperi subintervalul [5,7] , deci nu există nicio soluție pentru această instanță a problemei.


Solutie:
- sortam dupa captul din stanga
- algem intervalul cel mai lung??
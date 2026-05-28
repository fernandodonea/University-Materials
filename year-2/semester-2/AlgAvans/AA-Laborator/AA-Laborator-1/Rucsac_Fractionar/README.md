# Problema rucsacului - varianta fracționară

## Descriere

Fiind date  obiecte, fiecare cu o valoare  și cu o greutate , determinați ce obiecte trebuie să punem într-un rucsac în care încape o greutată maximă egală cu unități, astfel încât suma valorilor obiectelor incluse să fie maximă. Pentru fiecare obiect, putem alege să-l punem cu totul în rucsac sau să includem doar o parte din el (un procent din intervalul ). În această situație, obiectul va contribui cu acel procent din valoarea sa completă către suma valorilor din rucsac, analog pentru greutatea totală.

## Date de intrare

Se citesc de la tastatură două numere naturale  și , cu semnificațile din enunț. Pe următoarea linie se vor citi  numere naturale (, , , ), reprezentând valorile obiectelor, iar pe cealaltă încă  numere naturale (, , , ), reprezentând greutățile obiectelor.

## Date de iesire

Se va afișa un număr real, reprezentând valoarea maximă pe care o putem obține punând obiecte în rucsac.

## Restricții și precizări

Răspunsul trebuie să fie corect până la o precizie de cel puțin 2 zecimale.

### Exemplul 1

Input

```
3 5
7 12 15
2 3 5
```
Output
```
19
```
### Explicație

Valoarea maximă se obține punând în rucsac primul și al doilea obiect, care au o valoare combinată egală cu .

### Exemplul 2

Input

```
5 7
10 5 8 3 15
2 5 3 2 3
```

Output

```
30.3333
```
Explicație

Valoarea maximă se obține punând complet primul și ultimul obiect în rucsac, iar apoi punând  din al treilea obiect, pentru o valoare totală egală cu
 

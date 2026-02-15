# 412 Adiacenta
[Pbinfo](https://www.pbinfo.ro/probleme/412/adiacenta)

## Cerinţa
Se dă lista muchiilor unui graf neorientat. Să se afișeze matricea de adiacență a grafului.

## Date de intrare
Fişierul de intrare adiacenta.in conţine pe prima linie numerele n și m, reprezentând numărul de vârfuri ale grafului și numărul de muchii date în continuare. Fiecare dintre următoarele m linii conține câte o pereche de numere i j, cu semnificația că există muchie între i și j.

## Date de ieşire
Fişierul de ieşire adiacenta.out va conţine n linii, pe fiecare linie fiind câte n valori separate prin exact un spațiu, reprezentând matricea de adiacență a grafului dat.

## Restricţii şi precizări
1 ≤ n ≤ 100
1 ≤ i , j ≤ n
muchiile se pot repeta în fișierul de intrare
## Exemplu:
adiacenta.in
```
5 8
1 4 
1 3 
3 5 
4 5 
2 4 
1 2 
4 2 
3 4 
```
adiacenta.out
```
0 1 1 1 0 
1 0 0 1 0 
1 0 0 1 1 
1 1 1 0 1 
0 0 1 1 0 
```
# 414 ListaVecini

[Pbinfo](https://www.pbinfo.ro/probleme/414/listavecini)

## Cerinţa
Se dă lista muchiilor unui graf neorientat. Să se afișeze, pentru fiecare vârf al grafului, lista vecinilor săi.

## Date de intrare
Fişierul de intrare listavecini.in conţine pe prima linie numărul n, reprezentând numărul de vârfuri ale grafului. Fiecare dintre următoarele linii conține câte o pereche de numere i j, cu semnificația că există muchie între i și j.

## Date de ieşire
Fişierul de ieşire listavecini.out va conţine n linii. Fiecare linie i va conține numărul de vecini ai vârfului i urmat de aceștia, în ordine crescătoare.

## Restricţii şi precizări
1 ≤ n ≤ 100
1 ≤ i , j ≤ n
muchiile se pot repeta în fișierul de intrare
## Exemplu:
listavecini.in
```
5
1 4 
1 3 
3 5 
4 5 
2 4 
1 2 
4 2 
3 4 
```
listavecini.out
```
3 2 3 4 
2 1 4 
3 1 4 5 
4 1 2 3 5 
2 3 4 
```
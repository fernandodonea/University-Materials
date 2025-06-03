# Pbinfo #3011 lastk


Se dă un șir a[1], a[2], …, a[n] de numere naturale și un număr natural k.

## Cerința
Să se determine cele mai mari k numere din șir.

## Date de intrare
Programul citește de la tastatură numerele n, k, A, B, C, D. Șirul de numere se va genera după formulele:

a[1] = A
a[i] = (B * a[i-1] + C) % D, pentru i=2..n
Date de ieșire
Programul va afișa pe ecran, ordonate crescător, cele mai mari k numere din șir.

## Restricții și precizări
1 ≤ n ≤ 5.000.000
1 ≤ k ≤ min(100.000, n)
1 ≤ A, B, C, D ≤ 1.000.000.000

## Exemplu:
Intrare
```
10 4 13 23 47 97
```
Ieșire
```
55 56 74 96
```
Explicație
Se obține șirul de numere a = (13, 55, 51, 56, 74, 3, 19, 96, 24, 17). Cele mai mari patru numere sunt 55, 56, 74, 96.
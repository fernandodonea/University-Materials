# PAOJ Laborator 1


### ex 1
Sa se scrie un program java care verifica daca un numar e palindrom.
Un numar e palindrom daca inversul lui este egal cu el insusi.

Exemplu:

- 121 -> palimdrom
- 122 -> nu e palimdrom intrucat inversul lui 122 = 221 si 221 != 122

### ex 2
Sa se verifice daca un numar n are un numar impar de cifra ‘1’ in baza 2.
Exemplu :
n=3  3=11 in baza 2 se va afisa false
n=4 4=100 in baza 2 se va afisa true

### ex 3
Pentru un numar natural n sa se afiseze lungimea celui mai mare subsir de 1 al scrierii lui in baza 2.
Exemplu :
n=102 102=1100110 in baza 2 si se va afisa 2

### ex 4
Pentru un numar natural n sa se afiseze  la consola true daca si numai daca aplicand operatorul && pe toti bitii lui
(transformand numarul in baza 2) se obtine acelasi bit ca aplicand operatorul || pe toti bitii lui. Altfel se va afisa false.
Exemplu :
n=3  3=11  1&&1=1 1||1=1 Se va afisa true intrucat 0==0
n=4 4=100 1&&0&&0=0   1||0||0 = 1 Se va afisa false intruca 1!=0


### ex 5
Scrieti un program java care implementeaza jocul x si 0 in felul urmator :
-Cele 3 linii si 3 coloane ale matricei vor avea urmatoarea codificare

1 2 3
4 5 6
7 8 =9

-programul va astepta de la tastatura o cifra a jucatorului 1 apoi a jucatorului 2. Cifra respectiva reprezinta pozitia din matrice completata cu x, respectiv 0.
-dupa fiecare alegere a unui jucator se va afisa starea matricii. Exemplu daca jucatorul 1 a ales pozitia 5 initial se va afisa
```
_ _ _
_ x _
_ _ _
```
Ulterior daca jucatorul 2 va alege pozitia 3 se va afisa
```
_ _ 0
_ x _
_ _ _
```

-jocul se termina atunci cand avem un castigator[are x, respectiv 0 pe o linie, coloana sau diagonala] ori s-au epuizat toate miscarile pt cei 2 jucatori.


Problema 5 e challenge pt acasa.

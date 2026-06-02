# PAOJ Laborator 2

## ex 1
Pentru o lista de numere naturale sa se afiseze **lungimea celui mai lung subsir crescator**.

Exemplu: 
```
1 2 3 2 1 4 5 6 5 7 8 9 10 
```
Se va afisa 5

## ex 2
Se considera o matrice cu `m` linii si `n` coloane formata doar din 1 si 0.

Sa se afiseze numarul de celule din matrice cu urmatoarele proprietati:
- au valoarea 1
- toti vecinii(sus, jos, stanga, dreapta) au valoarea 0.

Exemplu:
m=3 n=3
```
0 1 0
1 0 0
0 1 1
```
Se va afisa 2.

## ex 3
Se considera un sir de numere intregi. Numerele pot fi pozitive sau negative. 

Sa se afiseze **suma maxima** pe care o poate avea un **subsir**.


Exemplu:
```
1 ,2, -3,   1, 2, 3, -5, 1,2,-4, 1,2  
```
Se va afisa 6

Bonus(optional) : Sa se rezolve problema in O(n)


## ex 4
Implementati o **lista dublu inlantuita** in java:
- Fiecare nod din lista va retine o valoare int
- Avem o metoda statica ce va returna capul listei
- Sa se implementeze metoda addLast ce primeste ca parametru un int si adauga un nod la finalul listei. Metoda returneaza o referinta catre nodul nou creat
- Sa se implementeze metoda addFirst ce primeste ca parametru un int si adauga un nod la inceputul listei. Noul nod va deveni capul listei. Metoda returneaza o referinta catre nodul nou creat
- Sa se implementeze o metoda addAtIndex care adauga la un index in lista un nou nod cu  valoarea primita ca parametru.
- Sa se implementeze o metoda fara parametrii size() ce returneaza dimensiunea listei.
- Sa se implementeze o metoda find care verifica daca o valoare numerica exista in lista.
- Sa se implementeze o metoda remove  care pentru un parametru dat elimina toate nodurile din lista cu aceeasi valoare.
- Sa se implementeze o metoda sort() care va sorta elementele listei in ordine crescatoare. Metoda va returna noul cap al listei.



## ex 5
Pentru lista dublu inlantuita de la 4) creati un constructor de copiere. 
El va returna capul listei copiate.

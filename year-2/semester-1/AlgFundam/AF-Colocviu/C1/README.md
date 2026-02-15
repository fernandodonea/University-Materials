# AF Colocviu - C1

[HackerRank](https://www.hackerrank.com/contests/af2026-v2/challenges/c1-64)

Scor maxim: 20 pct

## Cerinta 

In cadrul laboratorului de retele, ai la dispozitie o infrastructura formata din `n` servere numerotate de la 1 la n. Legaturile de comunicare sunt *unidirectionale*: daca exista o conexiune de la serverul `a` la serverul `b`, atunci mesajele pot fi trimise doar din `a` spre `b`. Astfel, reteaua este modelata ca un graf orientat cu `m` arce.

Administratorul vrea sa identifice **serverele centrale**, adica acele servere `x` care pot primi mesaje de la oricare alt server din retea, indiferent de unde porneste mesajul.
Mai exact, un server `x` este considerat central daca pentru orice server `y` (1 ≤ y ≤n) exista un *drum orientat de la y la x*. 

Sa se determine toate nodurile `x` cu aceasta proprietate si sa se afiseze in ordine crescatoare.


## Input Format

Se citesc de la tastatura:
- de pe prima linie: doua numere intregi n si m
- urmatoarele m linii: cate doua numere intregi a si b, reprezentand un arc orientat de la a la b

## Constraints

- 2 ≤ n ≤ 10^5
- 1 ≤ m ≤ min(n*(n - 1), 2 * 10^5)
- Pentru 25% din teste n, m ≤ 1000

## Output Format

Se vor afisa pe o singura linie toate nodurile x pentru care, pentru orice nod y, exista un drum de la y la x, in ordine crescatoare, separate prin spatiu.



## Exemple

Sample Input 0
```
6 6
4 3
2 4
4 2
5 4
6 2
1 3
```

Sample Output
```
3
```

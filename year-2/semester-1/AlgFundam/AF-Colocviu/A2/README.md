# AF Colocviu - A2

[HackerRank](https://www.hackerrank.com/contests/af2026-v2/challenges/a2-10-1)

Scor Maxim: 35 pct



## Cerinta 

In laboratorul de retelistica al facultatii exista `n` calculatoare, numerotate de la 1 la n.
Intre unele perechi de calculatoare exista deja cabluri, astfel incat se formeaza un *graf neorientat* cu `m` muchii. 

Reteaua nu este (neaparat) complet conectata, iar administratorul vrea sa o faca conexa adaugand cabluri noi. Daca se adauga un cablu intre calculatoarele `a` si `b`, costul este `a + b`. 

Se cere sa se determine **costul total maxim** al cablurilor care trebuie adaugate astfel incat graful sa devina **conex**.

## Input Format
De la tastatura se citesc:
- pe prima linie: doua numere intregi `n` si `m`.
- pe urmatoarele m linii: cate doua numere intregi `a` `b`, reprezentand o muchie neorientata intre nodurile a si b.

## Constraints
- 1 ≤ n ≤ 100000.
- 0 ≤ m < n-1.
- pentru fiecare muchie: 1 ≤ a, b ≤ n si a ‡ b.
- pentru 40 % din teste 1 ≤ n ≤ 1000.

## Output Format
Pe ecran se va afisa un singur numar intreg `S`: costul total maxim necesar pentru a adauga muchii astfel incat graful sa devina conex.

## Exemple

Sample Input 0
```
6 3
1 2
3 4
5 6
```

Sample Output 0
```
18
```

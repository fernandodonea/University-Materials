# AF Colocviu - B2

[HackerRank](https://www.hackerrank.com/contests/af2026-v2/challenges/b2-3-2)

Scor maxim: 35 pct

## Cerinta 

Intr-un oras inteligent exista `N` intersectii numerotate de la 1 la N si `M` strazi bidirectionale.

Fiecare strada leaga doua intersectii `A` si `B` si are un cost `C`. 
Primaria a amplasat `K` statii de interventie, situate in anumite intersectii. Din pacate, dupa o furtuna puternica, nu toate intersectiile sunt accesibile: se cunosc `Q` intersectii eligibile din care este permisa deplasarea catre statii.

 Distanta dintre doua intersectii este definita ca suma minima a costurilor strazilor de pe cel mai scurt drum. O intersectie eligibila este cu atat mai vulnerabila cu cat se afla mai departe de cea mai apropiata statie. Pentru fiecare
intersectie eligibila `x`, notam: `d(x) = min  dist(x, s)`, unde S este multimea statiilor.

Sa se determine intersectia eligibila `x` pentru care `d(x)` este **maxim**. Daca exista mai multe, se alege cea cu indicele cel mai mic. Se vor afisa distanta d(x) si un traseu minim de la x la o statie s € S de cost exact d(x). Afisarea corecta doar a costului fara traseu primeste jumatate din

## Input Format
Se citesc de la tastatura:
- de pe prima linie: trei numere naturale `N`, `M` si `K`
- de pe a doua linie: `K numere` distincte, indicii intersectiilor cu statii
- de pe a treia linie: un numar natural `Q`, numarul intersectiilor eligibile
- de pe a patra linie: `Q numere` distincte, indicii intersectiilor eligibile
- de pe urmatoarele M linii: cate trei numere `A`, `B`, `C`, reprezentand o strada bidirectionala intre A si B de cost C
- Pentru 40\% din teste N ≤ 1000

## Constraints
- 2 ≤ N ≤ 100000
- N-1 ≤ M ≤ min ((N*(N-1)/2) , 500000)
- 1 ≤ K ≤ N 
- 1 ≤ Q ≤ N
- 1≤ C ≤ 1000
- Graful este conex
- Pot exista mai multe strazi directe intre aceeasi pereche de intersectii
- Intersectiile din lista de statii sunt distincte; cele eligibile sunt distincte


## Output Format
Se afiseaza pe ecran:
- pe prima linie: un numar intreg `D`, reprezentand distanta minima D = d(x),
unde x este intersectia eligibila aleasa conform cerintei.
- pe a doua linie: un numar intreg `L` urmat de L numere intregi, reprezentand
un traseu minim: `p_1`, `p_2`, ... , `p_L`, unde `p_1` = x, `p_L` este o statie de interventie, iar costul total al traseului este D.



## Exemple

Sample Input 0
```
10 13 4
2 5 6 8
9
1 2 3 4 5 6 7 8 10
2 1 8
2 4 5
2 7 2
1 4 13
1 6 2
1 7 4
7 5 5
5 8 1
5 10 8
6 3 3
6 9 10
6 8 2
8 9 8
```

Sample Output 0
```
8
2 10 15
```

# Problema rucsacului - varianta discretă

## Descriere

Fiind date  obiecte, fiecare cu o valoare  și cu o greutate , determinați ce obiecte trebuie să punem într-un rucsac în care încape o greutată maximă egală cu unități, astfel încât suma valorilor obiectelor incluse să fie maximă. Pentru fiecare obiect, singurele opțiuni disponibile sunt să îl includem cu totul în rucsac sau să nu îl luăm deloc.

## Date de intrare

Se citesc de la tastatură două numere naturale  și , cu semnificațile din enunț. Pe următoarea linie se vor citi  numere naturale (, , , ), reprezentând valorile obiectelor, iar pe cealaltă încă  numere naturale (, , , ), reprezentând greutățile obiectelor.

## Date de iesire

Se va afișa un număr natural, reprezentând valoarea maximă pe care o putem obține punând obiecte în rucsac.


## Exemplul 1

Input

```
3 7
7 3 5
5 3 4
```
Output

```
8
```


## Exemplul 2

Input

```
5 10
7 15 4 8 9
3 6 1 1 2
```
Output

```
36
```

### Exemplul 3

Input

```
4 15
6 7 8 5
1 2 3 4
```
Output

```
26
```


#  Aflarea obiectelor folosite

`d[j]`= profitul maxim fara a depasi greutatea j

Initializare
```c++
for(int i=1;i<=C;i++)
    d[j]=0


//cazul de baza
//p[0]=-1
d[0]=0

for (int i=1;i<=n;i++)
{

    //aici avem DUPLICATE for(int j=gr[i];j<=C;j++)
    for(int j=C;j>=gr[i];j--)
    {
        d[j]=max(
            d[j],
            val(i)+d[j-gr[i]]
        );

        //pentru a retine obictele folosite
        // p[j]= p[j],daca am ales d[j]
        //       i, daca a, ales d[j-gr[i]]

    }

}

//solutia
sol=d[C]
```

GRESIT!!
Aceasta solutie admite duplicate



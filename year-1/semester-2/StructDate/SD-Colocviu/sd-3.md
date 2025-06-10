# S-3

## Cerinta

O zonă de deal trebuie modernizata prin amplasarea unor stalpi de iluminare, ce contin becuri la varf. Becurile vor fi plasate in forma de matrice, cunoscandu-se inaltimile lor. Becurile sunt identice si lumineaza pe linie si pe coloana maxim `K` patratele adiacente, insa iluminarea nu poate depasi o inaltime strict mai mare. 

Cu alte cuvinte un bec lumineaza in cele patru directii pana la distanta `D=min(K, i)`, unde  `i` este distanta pana la primul bec situat la o **inaltime strict mai mare** decat cea a becului curent.

## Input Format

Programul citeste de la tastatura `N`,`M`,`K`, numarul de linii, respectiv de coloane ale matricei de iluminat și numarul maxim de patratele iluminate de un bec în cele doa directii. Pe urmatoarele N linii se afla cate M numere separate prin cate un spatiu reprezentand inaltimile de amplasare ale becurilor.

## Constraints

5<=N,M<=2000

0<=K<=1999 (K=0 înseamnă că becul luminează doar pătrățica în care se află el).

0<=înălțimile din matrice<=30000

Pentru teste in valoare de  9 puncte se garanteaza ca N,M,K<=50.

Timp de rulare: 2 secunde.

Limita de memorie: 512Mb.

Folosirea STL pentru implementarea structurii de date necesare rezolvarii problemei duce la o penalizare de 25% din punctajul obtinut.

## Output Format

Programul va afisa pe ecran **numarul maxim de patratele** iluminate de un singur bec.

## Sample Input
```
6 5 2
5 1 9 9 0
4 9 8 5 1
3 8 8 8 5
2 7 3 6 6
1 5 8 7 0
5 9 9 1 9
```

## Sample Output
```
8
```

# Cod
```c++
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int n,m,k;
int a[2002][2002];
int distanta(int i, int j)
{
    int s=1;

    //verificam in jos
    int down=i;

    while(a[i][j]>=a[down][j] && (down-i-1)<k)
    {
        down++;
    }
    s+=down-i-1;
    //cout<<"jos:"<<down-i-1<<endl;

    //verifica sus
    int up=i;
    while(a[i][j]>=a[up][j] && (i-up-1)<k)
    {
        up--;
    }
    s+=i-up-1;
    //cout<<"up:"<<i-up-1<<endl;


    //verifica dreapta
    int right=j;
    while(a[i][j]>=a[i][right] && (right-j-1)<k)
    {
        right++;
    }
    s+=right-j-1;
    //cout<<"dreapta"<<right-j-1<<endl;


    int left=j;
    //verifica stanga
    while(a[i][j]>=a[i][left] && (j-left-1)<k)
    {
        left--;
    }
    s+=j-left-1;
    //cout<<"stanga"<<j-left-1;



    return s;
}

int main() 
{
    cin>>n>>m>>k;
    for(int i=0;i<=n+1;i++)
    {
        for(int j=0;j<=m+1;j++)
        {   
            //bordam matricea
            if(i==0 || i==n+1 || j==0 || j==m+1)
            {
                a[i][j]=30001;
            }
            else cin>>a[i][j];
        }
    }

    int maxim=4*k+1;
    int sol=-1;
    for(int i=1;i<=n && sol!=maxim;i++)
    {
        for(int j=1;j<=m && sol!=maxim;j++)
        {
            int d=distanta(i,j);
            if(d>sol)
            {
                sol=d;
            }

        }
    }
    cout<<sol;
    return 0;
}
```
complexitate Worst Case: O(K * N^2)

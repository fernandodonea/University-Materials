# S-2


Se dau `n` numere naturale `d_1,d_2,...,d_n` reprezentand lungimile a `n`  siruri ordinate crescator. Dacă se interclasează sirurule de dimensiuni  `d_i`si `d_j` atunci se efectuează `d_i + d_j` operatii si se obtine un sir de dimensiuni `d_i + d_j`. 

Trebuie interclasate toate cele `n` șiruri. Pentru aceasta sunt necesari exact `n-1` pasi. La fiecare pas se iau două siruri, se interclaseaza si cele două siruri se inlocuiesc cu noul sir. Scopul este să se obtina un singur sir ordonat efectuând un numar minim de operatii. 

De exemplu, dacă `n=5` si sirurile au dimensiunile **`1`**,**`5`**,**`2`** si **`5`** , atunci se poate interclasa mai întâi **`1`** si **`5`** , se fac 6 operatii si raman 3 siruri de lungimi `6`,`2`,`5`. Se interclaseaza apoi **`2`** cu **`5`** cu un cost 7 si raman două siruri: **`6`** și **`7`**. Se interclaseaza aceasta două cu un cost de 13 și a rămas un singur șir. In total s-au efectuat `6+7+13=26` operatii, dar **acesta nu este numarul minim posibil.**


## Input Format

Programul citeste de la tastatura numarul n, iar apoi dimensiunile celor n siruri.

## Constraints

1<=n<=10^5

Cele  numere citite vor fi naturale pozitive și mai mici sau egale 1000.

Pentru 12 puncte se garanteaza ca n<=2000

Timp de rulare: 1 secunda.

Limita de memorie: 512Mb.

Folosirea STL pentru implementarea structurii de date necesare rezolvarii problemei duce la o penalizare de 25% din punctajul obtinut.

## Output Format

Programul va afisa pe ecran numarul minim de operatii.

## Sample Input
```
4
1 5 2 5
```


## Sample Output
```
24
```


# Cod
```c++
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;



int H[100001];
int sz;


int parinte(int i){return i/2;}
int fiu_drept(int i){return 2*i+1;}
int fiu_stang(int i){return 2*i;}
int minim()
{
    return H[1];
}

void urcare(int pos)
{
    while(pos>1 && H[pos]<H[parinte(pos)])
    {
        swap(H[pos],H[parinte(pos)]);
        pos=parinte(pos);
    }
}

void inserare(int x)
{
    sz++;
    H[sz]=x;
    urcare(sz);
}


void coborare(int pos)
{
    while(true)
    {
        //este frunza ne oprim
        if(fiu_stang(pos)>sz)
            break;
        
        //verificam care dintre fii sai este mai mic
        int next_pos=fiu_stang(pos);

        if(fiu_drept(pos)<=sz && H[fiu_drept(pos)]<H[next_pos])
        {
            next_pos=fiu_drept(pos);
        }

        if(H[pos]<H[next_pos])
            break;
        else
        {
            swap(H[pos],H[next_pos]);
            pos=next_pos;
        }
    }
}
void stergeMin()
{
    swap(H[1],H[sz]);
    sz--;
    coborare(1);
}

int main() {
    int n;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        int d;
        cin>>d;
        inserare(d);
    }

    int op=0;

    while(sz>1)
    {
        int d1,d2;
        d1=minim();
        stergeMin();
        d2=minim();
        stergeMin();


        int s=d1+d2;
        op+=s;

        inserare(s);
    }

    cout<<op;
    return 0;
}

```
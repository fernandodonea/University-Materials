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

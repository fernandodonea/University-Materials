#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

//max heap =>ca sa putem stergem maximul 
int H[100001];

int sz;

int parinte(int i){return i/2;}
int left_son(int i){return 2*i;}
int right_son(int i){return 2*i+1;}

int maxim()
{
    return H[1];
}

bool cmp(int a, int b, int x)
{
    int dist_a=abs(a-x);
    int dist_b=abs(b-x);
    if(dist_a>dist_b)
        return true;
    else if(dist_a==dist_b && a>b)
        return true;
    else return false;
}
void urcare(int pos, int x)
{
    while(pos>1 && cmp(H[pos],H[parinte(pos)],x)==true)
    {
        swap(H[pos],H[parinte(pos)]);
        pos=parinte(pos);
    }
}


void inserare(int val, int x)
{
    sz++;
    H[sz]=val;
    urcare(sz,x);
}

void coborare(int pos, int x)
{
    while(true)
    {
        //cazul 1: este frunza
        if(left_son(pos)>sz)
            break;
        
        //cazul 2: are fii
        int next_pos=left_son(pos);
        //selectam fiul mai mic
        if(right_son(pos)<=sz && cmp(H[right_son(pos)],H[next_pos],x)==true)
        {
            next_pos=right_son(pos);
        }

        //verificam daca parintele se afla pe poztia corecta
        if( cmp(H[pos],H[next_pos],x)==false)
        {
            swap(H[pos],H[next_pos]);
            pos=next_pos;
        }
        else break;
    }
}



void stergeMax(int x)
{
    swap(H[sz],H[1]);
    sz--;
    coborare(1,x);
}



int main() {
    int n,k,x;
    cin>>n>>k>>x;
    for(int i=1;i<=n;i++)
    {
        int nr;
        cin>>nr;
        if(sz<k)
        {
            inserare(nr,x);
        }
        else
        {
            if(cmp(H[1],nr,x)==true)
            {
                stergeMax(x);
                inserare(nr,x);
            }
        }
    }
    for(int i=1;i<=k;i++)
    {
        cout<<maxim()<<" ";
        stergeMax(x);
    }
    return 0;
}
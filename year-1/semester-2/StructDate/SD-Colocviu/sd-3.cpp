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

    //pentru fiecare directe, daca depasim minimul adica K ne oprim

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

    //maximul posibil al unui bec este de 4*k+1 
    // (fiecare directie*k + pozitia sa)
    int maxim=4*k+1;
    int sol=-1;
    
    //daca un bec are valoarea maxima posibila, oprim (nu mai are sens sa cautam)
    
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
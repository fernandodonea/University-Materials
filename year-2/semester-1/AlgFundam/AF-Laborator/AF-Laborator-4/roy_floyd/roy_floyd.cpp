#include <iostream>
#include <fstream>
using namespace std;
#include <vector>

ifstream fin("royfloyd.in");
ofstream fout("royfloyd.out");


int n,m;
int d[101][101]; //matricea drumurilor minime

const int INF=1e9;

void citire()
{
    fin>>n;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            fin>>d[i][j];

            if(d[i][j]==0 && i!=j)
                d[i][j]=INF; //daca nu exista drum, punem infinit
        }
    }
}

void royfloyd()
{
    for(int k=1;k<=n;k++)
    {
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n;j++)
            {
                d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
            }
        }
    }
}

void afisare()
{
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            if(d[i][j]==INF)//distanta inca este infinit
                fout<<"0 ";
            else
                fout<<d[i][j]<<" ";
        }
        fout<<"\n";
    }
}
int main()
{
    citire();
    royfloyd();
    afisare();
    return 0;
}




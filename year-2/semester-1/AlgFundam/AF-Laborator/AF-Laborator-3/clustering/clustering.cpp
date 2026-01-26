#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <fstream>
#include <vector>
using namespace std;
ifstream fin("cuvinte.in");


int n; //numarul de cuvinte
int k=3; //numerul de clustere

int tata[101]; //vector de tati
int h[101]; //inaltimea componentelor
struct muchie
{
    int x,y,cost;
};
vector <muchie> E; //lista cu muchiile grafului

vector<string> cuvinte;//lista de cuvinte

vector<vector<int>> Klustere;

int grad_separare;




int Minim(int a, int b, int c)
{
    if(a<=b && a<=c) return a;
    else if(b<=a && b<=c) return b;
    else return c;
}

int Dist_editare(string cuv1,string cuv2)
{
    int n=cuv1.length();
    int m=cuv2.length();
    int a[n+1][m+1];


    //bordarea matricii
    for(int i=0;i<=n;i++)
    {
        a[i][0]=i;
    }
    for(int j=1;j<=m;j++)
    {
        a[0][j]=j;
    }

    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
        {
            int x,y;
            x=i-1;y=j-1;
            if(cuv1[x]==cuv2[y])
            {
                a[i][j]=a[i-1][j-1];
            }
            else{
                a[i][j]=1+Minim(a[i-1][j-1],a[i][j-1],a[i-1][j]);
            }
        }
    }
    return a[n][m];
}


void Citire()
{
    string cuv;
    while(fin>>cuv)
    {
        cuvinte.push_back(cuv);
    }
    n=cuvinte.size();

    //cin>>k;
}

void Init()
{
    //creare muchii pentru graful complet cu cost=dist_editare
    for(int i=0;i<n-1;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            int cost=Dist_editare(cuvinte[i],cuvinte[j]);
            E.push_back({i,j,cost});
        }
    }


    for(int i=0;i<n;i++)
    {
        h[i]=tata[i]=0;
    }
}

void SortareMuchii()
{
    sort(E.begin(),E.end(),
    [](muchie a, muchie b)
    {
        return a.cost < b.cost;
    });

}

int Find(int u)
{
    if(tata[u]==0)
        return u;
    tata[u]=Find(tata[u]);//compreise
    return tata[u];
}

void Union(int u, int v)
{
    int ru=Find(u);
    int rv=Find(v);

    if(h[ru]>h[rv])
    {
        tata[rv]=ru;
    }
    else{
        tata[ru]=rv;
        if(h[ru]==h[rv])
        {
            h[rv]=h[rv]+1;
        }
    }
}



void Kruskal()
{
    int nr_kluester=n;
    for (auto muchie:E)
    {
        int u=muchie.x;
        int v=muchie.y;

        if(Find(u)!=Find(v))
        {
            if(nr_kluester>k)
            {
                Union(u,v);
                nr_kluester--;
            }
            else
            {
                grad_separare=muchie.cost;
                break;
            }
        }
    

    }
}



int main()
{
    Citire();
    Init();
    SortareMuchii();
    Kruskal();

    Klustere.resize(n);
    for(int i=0;i<n;i++)
    {
        Klustere[Find(i)].push_back(i);
    }

    for(auto grup:Klustere)
    {
        if (grup.empty()) continue;
        for(auto nod:grup)
        {
            cout<<cuvinte[nod]<<" ";
        }
        cout<<endl;
    }
    cout<<endl<<endl<<grad_separare;
}
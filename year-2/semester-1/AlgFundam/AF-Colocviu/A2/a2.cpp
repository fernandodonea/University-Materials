/*
!!!!!!!!!!!!!!!!!!!!
    PUNCTAJ: 14/35
    3/9 cazuri
    Status: Abort Called
!!!!!!!!!!!!!!!!!!!!
 */


#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
//ifstream fin("a2.in");

int INF=1e9;
int NMAX=100001;

int n,m;

struct muchie
{
    int x,y,cost;
};


vector <muchie> L;//lista L[x]={nod, muchie}

vector <int> tata;
vector <int> h;



void Citire()
{
    cin>>n>>m;

    int dim=n*(n-1)/2;

    L.resize(dim+1);



    tata.resize(n+1);
    h.resize(n+1);
    for(int i=1;i<=m;i++)
    {
        int x,y;
        cin>>x>>y;
        L.push_back({x,y,INF});
        tata[y]=x;
    }
}



void Init()
{
    for(int i=1;i<n;i++)
    {
        for(int j=i+1;j<=n;j++)
        {
            if(tata[i]!=j)
            {
                int cost=i+j;
                L.push_back({i,j,cost});
                m++;
            }
        }
    }
    for(int i=1;i<=n;i++)
    {
        tata[i]=0;
        h[i]=0;
    }
}

int Reprezentant(int u)
{
    if(tata[u]==0)
        return u;
    tata[u]=Reprezentant(tata[u]);//compresie
    return tata[u];
}

void Reuneste(int u, int v)
{
    int ru=Reprezentant(u);
    int rv=Reprezentant(v);

    if(h[ru]>h[rv])
    {
        tata[rv]=ru;
    }
    else
    {
        tata[ru]=rv;

        if(h[ru]==h[rv])
        {
            h[rv]=h[rv]+1;
        }
    }
}

void SortareMuchii()
{

    sort(L.begin(),L.end(),
    [](muchie a, muchie b)
    {
        return a.cost>b.cost;
    });

}

void Kruskal()
{
    SortareMuchii();
    int cost_apm=0;
    int nr_muchii_sel=0;

    for(auto e:L)
    {
        int u,v,w_u_v;
        u=e.x;
        v=e.y;
        w_u_v=e.cost;

    
        
        if(Reprezentant(u)!=Reprezentant(v))
        {
            Reuneste(u,v);
            nr_muchii_sel+=1;
            if(w_u_v!=INF)
            {
                cost_apm+=w_u_v;
            }
            if(nr_muchii_sel>n-1)
            {
                break;
            }
        }
    }
    cout<<cost_apm;



}

int main()
{
    Citire();
    Init();
    Kruskal();
    return 0;


}
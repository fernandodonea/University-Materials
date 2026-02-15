/*
!!!!!!!!!!!!!!!!!!!!
    PUNCTAJ: 0/35
    neterminat
!!!!!!!!!!!!!!!!!!!!
 */

#include <iostream>
#include <vector>
#include <fstream>
#include <queue>
using namespace std;
ifstream fin("b2.in");


int n,m,k,q;

vector <int> statie;
vector <int> eligibil;

int maxim;


vector<vector <pair<int,int>>> L; //lista de tip L[x]={nod, muchie};


vector <int> d;
vector <int> tata;
vector <int> viz;
vector <int> h;


void Init()
{
    for(int i=1;i<=n;i++)
    {
        d[i]=0;
        tata[i]=0;
        viz[i]=0;
        h[i]=0;

    }
}

void citire()
{
    fin>>n>>m>>k;

    statie.resize(n+1);
    eligibil.resize(n+1);
    d.resize(n+1);
    tata.resize(n+1);
    viz.resize(n+1);
    h.resize(n+1);
    L.resize(n+1);

    //statii
    for(int i=1;i<=k;i++)
    {
        int x;
        fin>>x;
        statie[x]=1;
    }

    //intersectii eligibile
    fin>>q;
    for(int i=1;i<=q;i++)
    {
        int x;
        fin>>x;
        eligibil[x]=1;
    }

    for(int i=1;i<=m;i++)
    {
        int x,y,cost;
        fin>>x>>y>>cost;
        if(eligibil[x]==1 && eligibil[y]==1)
        {
            L[x].push_back({y,cost});
            L[y].push_back({x,cost});
        }
    }


}


void BFS(int s)
{

    int maximmm=-1;

    Init();

    queue <int> C;

    viz[s]=1;
    C.push(s);

    while(!C.empty())
    {
        int nod=C.front();
        cout<<nod<<" ";
        C.pop();

        for(auto vecin:L[nod])
        {
            int x=vecin.first;
            int cost=vecin.second;
            if(viz[x]==0)
            {
                h[x]=h[nod]+1;
                d[x]=d[nod]+cost;
                viz[x]=1;

                C.push(x);
            }
        }
    }
    cout<<endl;
    for(int i=1;i<=n;i++)
    {
        if(d[i]>maximmm)
        {
            maximmm=d[i];
        }
    }
    cout<<maximmm<<endl;
}

int main()
{
    citire();
    for(int i=1;i<=n;i++)
    {
        if(statie[i]==1)
        {
            BFS(i);
        }
        
    }

}
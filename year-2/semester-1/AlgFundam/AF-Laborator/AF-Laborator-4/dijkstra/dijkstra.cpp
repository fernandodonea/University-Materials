#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
using namespace std;

ifstream fin("dijkstra.in");
ofstream fout("dijkstra.out");

 
int n,m;


vector <int> d; //vector de distante minime

vector <vector <pair<int,int> > > L; //lista de adiacenta
vector <int> viz; //vector de vizitati
priority_queue <pair<int,int> > PQ; //priority queue



void citire()
{
    fin>>n>>m;
    
    
    d.resize(n+1);
    L.resize(n+1);
    viz.resize(n+1, 0);
    
    for(int i=1;i<=m;i++)
    {
        int x,y,cost;
        fin>>x>>y>>cost;

        //adaugam in lista
        L[x].push_back({y,cost});
        
    }    
}
void initializare(int sursa)
{
    d[sursa]=0;
    for(int i=1;i<=n;i++)
    {
        if(i != sursa)
            d[i]=1e9; //infinit
    }
}

void dijkstra(int sursa)
{

    PQ.push({-d[sursa],sursa});
    while(!PQ.empty())
    {
        int nod=PQ.top().second;
        PQ.pop();

        if(viz[nod]==1)
            continue;
        
        viz[nod]=1;
        for(auto x:L[nod])
        {
            int vecin=x.first;
            int cost=x.second;
            if(d[vecin]>d[nod]+cost)
            {
                d[vecin]=d[nod]+cost;
                PQ.push({-d[vecin],vecin});
            }
        }
    }
}
void afisare()
{
    for(int i=2;i<=n;i++)
    {
        if(d[i]==1e9)
            fout<<"0 ";
        else
            fout<<d[i]<<" ";
    }
}

int main() 
{
    citire();
    initializare(1);
    dijkstra(1);
    afisare();
    return 0;
}
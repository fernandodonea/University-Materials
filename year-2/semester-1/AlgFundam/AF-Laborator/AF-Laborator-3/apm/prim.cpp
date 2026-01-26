#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <cstdlib>

using namespace std;
ifstream fin("apm.in");
ofstream fout("apm.out");

const int INF=1001;

int n,m;

vector <vector<pair<int, int>>> L; //lista de tip L[x]=({y, cost},...)
priority_queue <pair<int,int>> PQ; //max heap de tip {-d[nod],nod}

vector <int> viz;
vector <int> d;
vector <int> tata;

int cost_apm;

void Citire()
{
    fin>>n>>m;
    if(!fin.is_open() || n == 0)
    {
        cout << "Eroare: Nu s-a putut citi din fisierul apm.in. Verificati calea fisierului." << endl;
        exit(1);
    }
    L.resize(n+1);
    viz.resize(n+1);
    d.resize(n+1);
    tata.resize(n+1);
    for(int i=1;i<=m;i++)
    {
        int x,y,cost;
        fin>>x>>y>>cost;
        L[x].push_back({y,cost});
        L[y].push_back({x,cost});
    }
}
void Init()
{
    for(int i=1;i<=n;i++)
    {
        d[i]=INF;
        viz[i]=0;
    }
}

void Prim(int s)
{
    d[s]=0;
    PQ.push({d[s],s});

    while(!PQ.empty())
    {
        int u=PQ.top().second;
        PQ.pop();

        if(viz[u]==0)
        {

            cost_apm+=d[u];
            viz[u]=1;

            for(auto vecin:L[u])
            {
                int v=vecin.first;
                int cost=vecin.second;
                //relaxam muchii
                if(cost<d[v])
                {
                    d[v]=cost;
                    tata[v]=u;
                    PQ.push({-d[v],v});
                }
            }
        }
    }

}

int main()
{
    Citire();
    Init();
    Prim(1);
    cout<<cost_apm<<endl;
    cout<<n-1<<endl;
    fout<<cost_apm<<endl;
    fout<<n-1<<endl;
    for(int i=2;i<=n;i++)
    {
        cout<<i<<" "<<tata[i]<<endl;
        fout<<i<<" "<<tata[i]<<endl;
    }
}
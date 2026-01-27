#include <fstream>
#include <vector>
#include <queue>
using namespace std;
ifstream fin("bellmanford.in");
ofstream fout("bellmanford.out");

const int INF=1e9;

int n,m;

vector <int> d; // vector de distante minime
vector <int> inq; // vector care retine daca un nod este in coada
vector <int> cnt; // vector de numar de relaxari efectuate pentru fiecare nod

vector <vector<pair<int,int>>> L; // lista de adiacenta: L[x] = {(y,cost)}

queue <int> Q; // coada pentru SPFA

void citire()
{
    fin>>n>>m;
    L.resize(n+1);
    for(int i=1;i<=m;i++)
    {
        int x,y,cost;
        fin>>x>>y>>cost;
        L[x].push_back({y,cost});
    }
}

void initializare(int sursa)
{
    d.resize(n+1,INF);
    inq.resize(n+1,0);
    cnt.resize(n+1,0);

    d[sursa]=0;
    Q.push(sursa);
    inq[sursa]=1;
    cnt[sursa]++;
}

bool bellman_ford(int sursa)
{
    while(!Q.empty())
    {
        int nod=Q.front();
        Q.pop();
        inq[nod]=0;

        // Iteram peste vecinii nodului curent (nu peste TOATE muchiile)
        for(auto muchie : L[nod])
        {
            int vecin = muchie.first;
            int cost = muchie.second;

            if(d[vecin] > d[nod] + cost) // relaxare muchiilor
            {
                d[vecin] = d[nod] + cost;

                if(inq[vecin] == 0)
                {
                    Q.push(vecin);
                    inq[vecin] = 1; // il marcam ca fiind in coada
                    cnt[vecin]++;

                    if(cnt[vecin] > n) // exista ciclu negativ
                    {
                        return true; // returnam true daca exista ciclu negativ
                    }
                }
            }
        }
    }
    return false; // nu exista ciclu negativ
}

void afisare()
{
    for(int i=2;i<=n;i++)
    {
        fout<<d[i]<<" ";
    }
}

int main()
{
    citire();
    initializare(1);
    
    if(bellman_ford(1))
    {
        fout<<"Ciclu negativ!\n";
    }
    else
    {
        afisare();
    }
    
    return 0;
}
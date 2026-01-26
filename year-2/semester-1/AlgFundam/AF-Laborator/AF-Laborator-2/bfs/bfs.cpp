#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

ifstream fin("bfs.in");
ofstream fout("bfs.out");


/*
Fiind dat un nod S, sa se determine, pentru fiecare nod X, 
numarul minim de arce ce trebuie parcurse pentru a ajunge din nodul sursa S la nodul X.
 */

const int NMAX=100001;
const int INFINIT=-1;

int n,m,s;

vector<vector <int>> L;//lista de adiacenta
queue <int> C;//coada pentru bfs

vector <int> d;
vector <int> viz;

void Citire()
{
    fin>>n>>m>>s;
    L.resize(n+1);
    d.resize(n+1);
    viz.resize(n+1);


    for(int i=1;i<=m;i++)
    {
        int x,y;
        fin>>x>>y;
        L[x].push_back(y);
    }
}

void Init()
{
    for(int i=1;i<=n;i++)
    {
        d[i]=INFINIT;
        viz[i]=0;
    }
}

void BFS(int s)
{
    C.push(s);
    viz[s]=1;
    d[s]=0;

    while(!C.empty())
    {
        int u=C.front();
        C.pop();

        for(auto v:L[u])//parcurgem muchiile
        {
            if(viz[v]==0)
            {
                viz[v]=1;
                d[v]=d[u]+1;
                C.push(v);
            }
        }
    }
}

int main()
{
    Citire();
    Init();
    BFS(s);

    for(int i=1;i<=n;i++)
    {
        fout<<d[i]<<" ";
    }

    fin.close();
    fout.close();
    return 0;
}




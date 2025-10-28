#include <fstream>
#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;
ifstream fin("bfs.in");
ofstream fout("bfs.out");


int n,m,s;

vector<int> L[100001];
queue<int> C;
int viz[100001];
int dist[100001];

void citire()
{
    fin>>n>>m>>s;
    for(int i=1;i<=m;i++)
    {
        int x,y;
        fin>>x>>y;
        L[x].push_back(y);
    }
    
}


void bfs()
{
    //initializare distante cu infinit
    for(int i=1;i<=n;i++)
    {
        dist[i]=-1;
    }

    dist[s]=0;
    C.push(s);

    while(!C.empty())
    {
        int nod=C.front();
        C.pop();
        for(auto vecin: L[nod])
        {
            if(dist[vecin]==-1)
            {
                dist[vecin]=dist[nod]+1;
                C.push(vecin);
            }
        }
    }


}

void afisare()
{
    for(int i=1;i<=n;i++)
    {
        fout<<dist[i]<<" ";
    }
}

int main()
{
    citire();
    bfs();
    afisare();
    return 0;

}
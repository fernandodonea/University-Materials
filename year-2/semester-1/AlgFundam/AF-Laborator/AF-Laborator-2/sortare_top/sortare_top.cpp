#include <fstream>
#include <vector>
#include <stack>
using namespace std;
ifstream fin("sortaret.in");
ofstream fout("sortaret.out");


int n,m;

vector <vector<int>> L;
vector <int> viz;
stack <int> S;




void Citire()
{
    fin>>n>>m;
    L.resize(n+1);
    viz.resize(n+1);
    for(int i=1;i<=m;i++)
    {
        int x,y;
        fin>>x>>y;
        L[x].push_back(y);
    }
}


void DFS(int u)
{
    viz[u]=1;
    for(auto v:L[u])
    {
        if(viz[v]==0)
        {
            DFS(v);
        }
    }
    //s-a terminat explorarea
    //adaugam pe stack
    S.push(u);
}

int main()
{
    Citire();
    for(int i=1;i<=n;i++)
    {
        if(viz[i]==0)
        {
            DFS(i);
        }
    }

    while(!S.empty())
    {
        int nod=S.top();
        S.pop();
        fout<<nod<<" ";
    }
    fin.close();
    fout.close();
    return 0;
}

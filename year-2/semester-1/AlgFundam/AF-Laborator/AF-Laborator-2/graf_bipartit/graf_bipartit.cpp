#include <iostream>
#include <fstream>
#include <vector>
#include <queue>

using namespace std;
//ifstream fin("graf_bipartit.in");


int n,m;

vector<vector<int>> L;
vector<int> viz;
bool ok=true;


void Citire()
{
    cin>>n>>m;
    L.resize(n+1);
    viz.resize(n+1);

    for(int i=1;i<=m;i++)
    {
        int a,b;
        cin>>a>>b;
        L[a].push_back(b);
        L[b].push_back(a);
    }

}

void BFS(int s)
{
    queue <int> C;

    viz[s]=1;
    C.push(s);

    while(!C.empty())
    {
        int nod=C.front();
        C.pop();

        for(auto vecin:L[nod])
        {
            if(viz[vecin]==0)
            {
                viz[vecin]=3-viz[nod];
                C.push(vecin);
            }
            else if(viz[vecin]==viz[nod])
            {
                ok=false;
                
            }
        }
    }

}


int main()
{
    Citire();
    for(int i=1;i<=n;i++)
    {
        if(viz[i]==0)
        {
            BFS(i);
        }
    }
    if(ok==false)
    {
        cout<<"IMPOSSIBLE";
    }
    else{
        for(int i=1;i<=n;i++)
            cout<<viz[i]<<" ";
    }

    
    return 0;

}
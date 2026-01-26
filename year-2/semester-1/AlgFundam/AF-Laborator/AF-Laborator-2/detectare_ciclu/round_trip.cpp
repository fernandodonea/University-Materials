#include <iostream>
#include <vector>
using namespace std;

int n,m;

vector<vector<int>> L;//lista muchii
vector <int> viz;
vector <int> tata;
vector <int> ciclu;

bool ok=false;

void Citire()
{
    cin>>n>>m;
    L.resize(n+1);
    viz.resize(n+1);
    tata.resize(n+1);
    for(int i=1;i<=m;i++)
    {
        int x,y;
        cin>>x>>y;
        L[x].push_back(y);
        L[y].push_back(x);//graf neorientat
    }
}

void DFS(int u)
{
    if(ok==true)return;

    viz[u]=1;
    for(auto v:L[u])
    {
        if(ok)return;

        if(viz[v]==0)
        {
            tata[v]=u;
            DFS(v);
        }
        else if(tata[u]!=v)
        {
            
            
                //ciclu detectat
                ok=true;

                ciclu.push_back(v);
                int nod = u;
                while(nod!=v)
                {
                    ciclu.push_back(nod);
                    nod=tata[nod];
                }
                ciclu.push_back(v);
                return;

            
        }
    }
}


int main()
{
    Citire();
    for(int i=1;i<=n && ok!=true;i++)
    {
        if(viz[i]==0)
        {
            DFS(i);
        }
    }
    if(ok==false)
    {
        cout<<"IMPOSSIBLE";

    }
    else
    {
        cout<<ciclu.size()<<endl;
        for(auto nod:ciclu)
        {
            cout<<nod<<" ";

        }
    }

}
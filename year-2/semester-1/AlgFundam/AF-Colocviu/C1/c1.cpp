/*
!!!!!!!!!!!!!!!!!!!!
    PUNCTAJ: 12.5/20
    8/15 cazuri
    Status: Terminated due to timeout
!!!!!!!!!!!!!!!!!!!!
 */

#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
//ifstream fin("c1.in");


int n,m;
vector <vector<int>> L;

vector <int> viz;

void citire()
{
    cin>>n>>m;
    L.resize(n+1);
    viz.resize(n+1);
    for(int i=1;i<=m;i++)
    {
        int x,y;
        cin>>x>>y;
        L[y].push_back(x);//introducem arcul invers;
    }
}
void Init()
{
    for(int i=1;i<=n;i++)
    {
        viz[i]=0;
    }
}

int k;

void DFS(int x)
{
    k++;
    viz[x]=1;
    for(auto y:L[x])
    {
        if(viz[y]==0)
        {
            DFS(y);
        }
    }
}


int main()
{
    citire();
    for(int i=1;i<=n;i++)
    {
        Init();
        k=0;
        DFS(i);
        if(k==n)
        {
            cout<<i<<" ";
        }

    }
    return 0;

}
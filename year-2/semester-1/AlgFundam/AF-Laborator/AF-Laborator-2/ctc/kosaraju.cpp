#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
using namespace std;
ifstream fin("ctc.in");
ofstream fout("ctc.out");


int n,m;

vector <vector <int>> L; //lista de adiacenta in graful G

vector <vector <int>> L_t; //lista de adiacenta in graful G transpus

stack <int> sortTop; //stiva pentru a retine sortarea topologica

vector <int> viz,viz_t;

vector<vector <int>> comp_tare_conexa;
int ctc;


void Citire()
{
    fin>>n>>m;

    L.resize(n+1);
    L_t.resize(n+1);
    viz.resize(n+1);
    viz_t.resize(n+1);
    comp_tare_conexa.resize(n+1);

    for(int i=1;i<=m;i++)
    {
        int x,y;
        fin>>x>>y;
        L[x].push_back(y);
        L_t[y].push_back(x);
    }
}



void DFS(int x)
{
    viz[x]=1;
    for(auto i :L[x])
    {
        if(viz[i]==0)
        {
            DFS(i);
        }
    }
    sortTop.push(x);
}

void DFS_t(int x)
{
    viz_t[x]=1;
    comp_tare_conexa[ctc].push_back(x);//adaugam in ctc

    for(auto i :L_t[x])
    {
        if(viz_t[i]==0)
        {
            DFS_t(i);
        }
    }
}

void AfisareCTC()
{
    fout<<ctc<<endl;
    for(int i=1;i<=ctc;i++)
    {
        for(auto nod:comp_tare_conexa[i])
        {
            fout<<nod<<" ";
        }
        fout<<endl;
    }
}

void Kosaraju()
{
    for(int i=1;i<=n;i++)
    {
        if(viz[i]==0)
        {
            DFS(i);
        }
    }

    while(!sortTop.empty())
    {
        int i=sortTop.top();
        sortTop.pop();
        if(viz_t[i]==0)
        {
            ctc++;
            DFS_t(i);
        }
    }

}

int main()
{
    Citire();
    Kosaraju();
    AfisareCTC();

    fin.close();
    fout.close();

}
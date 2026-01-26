#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
ifstream fin("dfs.in");
ofstream fout("dfs.out");

/*
Sa se determine numarul componentelor conexe ale grafului.
*/

int n,m;

vector <vector <int>> L; //lista de adiacenta a muchiilor


vector <int> culoare;
enum col {
    alb=0,
    gri=1,
    negru=2
};

//vector <int> d;
//vector <int> tata;

int timp;
vector <int> descoperit;
vector <int> finalizat;

void Citire()
{
    fin>>n>>m;
    L.resize(n+1);
    descoperit.resize(n+1);
    finalizat.resize(n+1);
    culoare.resize(n+1);

    for(int i=1;i<=m;i++)
    {
        int x,y;
        fin>>x>>y;
        L[x].push_back(y);
        L[y].push_back(x);//graf neorientat
    }
}

void Init()
{
    for(int i=1;i<=n;i++)
    {
        culoare[i]=alb;
        //tata[i]=0;
        //d[i]=inf;
    }
}

void DFS(int u)
{
    culoare[u]=gri;

    timp++;
    descoperit[u]=timp;

    for(auto v:L[u])
    {
        if(culoare[v]==alb)
        {
            //tata[v]=u;
            //d[v]=d[u]+1;
            DFS(v);
    
        }
    }

    culoare[u]=negru;

    timp++;
    finalizat[u]=timp;
}

int main()
{
    Citire();

    int nr_comp_conexe=0;
    for(int i=1;i<=n;i++)
    {
        if(culoare[i]==alb)
        {
            DFS(i);
            nr_comp_conexe++;
        }
    }
    fout<<nr_comp_conexe;

    fin.close();
    fout.close();
    return 0;
}

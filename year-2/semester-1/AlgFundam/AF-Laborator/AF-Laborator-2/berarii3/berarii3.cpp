#include <iostream>
#include <fstream>
#include <vector>
#include <queue>

using namespace std;
ifstream fin("berarii3.in");
ofstream fout("berarii3.out");

/*
berarii2 DAR

Să se determine, în plus, pentru fiecare intersecție, care
este cea mai apropiată berărie (Reformulare: Se dă o rețea neorientată cu n noduri și o listă
de noduri reprezentând puncte de control pentru rețea. Să se determine pentru fiecare nod
din rețea distanța până la cel mai apropiat punct de control de acesta. )

*/

int n,m,p;

vector <vector <int>> L; //lista muchii
vector <int> viz;

vector <int> d;

int berarie_curenta=0;

void Citire()
{
    fin>>n>>m>>p;
    L.resize(n+1);
    viz.resize(n+1);
    d.resize(n+1);

    for(int i=1;i<=m;i++)
    {
        int x,y;
        fin>>x>>y;
        L[y].push_back(x);//introducem muchiile invers
        //trebuie sa cautam intersectiile din care nu putem ajunge la berarie
        //dfs invers din berarii catre drumuri inaccesibile
    }
}

void DFS(int x)
{
    viz[x]=berarie_curenta;
    for(auto vecin:L[x])
    {
        if(viz[vecin]==0)
        {
            d[vecin]=d[x]+1;
            DFS(vecin);
        }
    }
}

void Berarii()
{

    for(int i=1;i<=p;i++)
    {
        int berarie;
        fin>>berarie;

        berarie_curenta=berarie;

        DFS(berarie);
    }
    
    //intersectiile din care nu putem ajunge la nicio berarie
    int q=0;


    for(int i=1;i<=n;i++)
    {
        fout<<"intersectia "<<i<<"; cea mai apropiata berarie :";
        if(viz[i]==0)
        {
            fout<<-1<<endl;
        }
        else fout<<viz[i]<<endl;
    }
    fout<<q<<endl;

}

int main()
{
    Citire();
    Berarii();
    fin.close();
    fout.close();
}
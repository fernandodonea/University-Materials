
#include <fstream>
#include <vector>
using namespace std;

ifstream fin("ctc.in");
ofstream fout("ctc.out");





int n,m;
vector<int> L[100001],L_t[100001];//L_t graful transpus
int viz[100001],viz2[100001];

int ctc;//componente tare conexe

vector <int> v; //timpul de terminare in dfs -> parcurgem in ordine inversa in graful transpus



void citire()
{
    fin>>n>>m;
    for(int i=1;i<=m;i++)
    {
        int a,b;
        fin>>a>>b;
        L[a].push_back(b);
        L_t[b].push_back(a);
    }
}


void dfs1(int nod)
{
    viz[nod]=1;
    for(auto vecin : L[nod])
    {
        if(viz[vecin]==0)
        {
            dfs1(vecin);
        }
    }
    v.push_back(nod);//ordinea de terminare in dfs
}





void dfs2(int nod)
{
    viz2[nod]=ctc;
    for(auto vecin: L_t[nod])
    {
        if(viz2[vecin]==0)
        {
            dfs2(vecin);
        }
    }
}

int main()
{
    citire();

    for(int i=1;i<=n;i++)
    {
        if(viz[i]==0)
        {
            dfs1(i);
        }
    }

    for(int i=v.size()-1;i>=0;i--)
    {
        int nod=v[i];
        if(viz2[nod]==0)
        {
            ctc++;
            dfs2(nod);
        }
    }

    //nr de componente tare conexe
    fout<<ctc<<"\n";

    // Gruparea nodurilor pe componente pentru o afisare eficienta O(N)
    vector<vector<int>> componente(ctc + 1);
    for(int i = 1; i <= n; i++)
    {
        componente[viz2[i]].push_back(i);
    }

    // Afisarea componentelor
    for(int i = 1; i <= ctc; i++)
    {
        for(int nod : componente[i])
            fout << nod << " ";
        fout<<endl;
    }
    return 0;

}
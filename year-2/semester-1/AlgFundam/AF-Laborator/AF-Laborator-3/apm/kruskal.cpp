#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;
ifstream fin("apm.in");
ofstream fout("apm.out");



int n,m;

struct muchie 
{
    int u,v;
    int cost;
};
vector <muchie> L;
vector <int> tata;
vector <int> h;


vector <muchie> APM;
int cost_apm;



void Citire()
{
    fin>>n>>m;
    L.resize(m+1);
    h.resize(n+1);
    tata.resize(n+1);

    for(int i=1;i<=m;i++)
    {
        int x,y,cost;
        fin>>x>>y>>cost;
        L.push_back({x,y,cost});
    }
}

void Init()
{
    for(int i=1;i<=n;i++)
    {
        tata[i]=h[i]=0;
    }
}

int Reprezentant(int u)
{
    if(tata[u]==0)
        return u;
    tata[u]=Reprezentant(tata[u]);//compresie
    return tata[u];
}

void Reuneste(int u, int v)
{
    int ru=Reprezentant(u);
    int rv=Reprezentant(v);

    if(h[ru]>h[rv])
    {
        tata[rv]=ru;
    }
    else
    {
        tata[ru]=rv;
        if(h[ru]==h[rv])
        {
            h[rv]=h[rv]+1;
        }
    }
}


void SortareMuchii()
{
    sort(L.begin(),L.end(),
    [](muchie a, muchie b)
    {
        return a.cost<b.cost;
    });
}

void Kruskal()
{
    Init();

    SortareMuchii();

    int nr_muchii_sel=0;

    for (auto e:L)
    {

        int rv,ru;
        ru=Reprezentant(e.u);
        rv=Reprezentant(e.v);
        if(ru!=rv)
        {
            APM.push_back(e);
            cost_apm+=e.cost;

            Reuneste(e.u,e.v);

            nr_muchii_sel++;
            if(nr_muchii_sel>n-1)
            {
                break;
            }

        }

    }


}

int main()
{
    Citire();

    Kruskal();
    fout<<cost_apm<<endl;
    fout<<n-1<<endl;
    for(auto e:APM)
    {
        fout<<e.u<<" "<<e.v<<endl;
    }

    
    return 0;
}





#include <fstream>
#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
using namespace std;
ifstream fin("retea2.in");
ofstream fout("retea2.out");


int n,m;
int k=0;

struct coord
{
    int id;
    int x, y;
};


vector <coord> blocuri;
vector <coord> centrale;



vector<vector<pair<int,int>>> L; //L[x]={nod,cost};
priority_queue<pair<int,int>> PQ;//{-d[nod],nod}


vector <int> d;
vector <int> viz;
vector <int> tata;



void Citire()
{
    fin>>n>>m;
    centrale.resize(n+1);
    blocuri.resize(m+1);



    for(int i=1;i<=n;i++)
    {
        int x,y;
        fin>>x>>y;
        k++;
        centrale.push_back({k,x,y});
    }
    for(int i=1;i<=m;i++)
    {
        int x,y;
        fin>>x>>y;
        k++;
        blocuri.push_back({k,x,y});
    }
    L.resize(k+1);
    d.resize(k+1);
    viz.resize(k+1);
    tata.resize(k+1);
}


float dist_euclid(int x1, int y1, int x2, int y2)
{
    return sqrt((x1-x2)^2+(y1-y2)^2);
}

void Init()
{
    //conectam centralele cu blocurile
    for(auto c:centrale)
    {
        for(auto b:blocuri)
        {
            int u=c.id;
            int v=b.id;
            int cost=dist_euclid(c.x,c.y,b.x,b.y);
            cout<<cost<<endl;

            L[u].push_back({v,cost});
            L[v].push_back({u,cost});
        }
    }


    for(auto b1:blocuri)
    {
        for(auto b2:blocuri)
        {
            int u=b1.id;
            int v=b2.id;
            int cost=dist_euclid(b1.x,b1.y,b2.x,b2.y);

            L[u].push_back({v,cost});
            L[v].push_back({u,cost});
        }
    }
}



int main()
{
    Citire();
    Init();
    for(int i=1;i<=k;i++)
    {
        fout<<i<<endl;
        for(auto muchie:L[i])
        {
            fout<<muchie.first<<" "<<muchie.second<<endl;
        }
        fout<<endl<<endl<<endl;
    }

}



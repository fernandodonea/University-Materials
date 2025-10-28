#include <fstream>
#include <vector>
using namespace std;
ifstream fin("dfs.in");
ofstream fout("dfs.out");
int n,m,viz[101];
vector<int> vecini[101]; // Lista de adiacenta
void citire()
{
    int x,y;
    fin>>n>>m;
    for(int i=1;i<=m;i++)
    {
        fin>>x>>y;
        vecini[x].push_back(y); 
        vecini[y].push_back(x); 
    }
}
void dfs(int nod)
{
    viz[nod]=1;
    //parcurgem vecinii
    for(auto vecin :vecini[nod]) // Iteram doar prin vecinii nodului curent
    {
        if(viz[vecin]==0)
        {
            dfs(vecin);
        }
    }
}
int main()
{
    citire();
    int k=0;
    for(int i=1;i<=n;i++)
    {
        if(viz[i]==0)
        {
            dfs(i);
            k++;

        }
    }
    fout<<k;
    return 0;
    
}

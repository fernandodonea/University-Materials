#include <fstream>
#include <vector>
#include <queue>


using namespace std;
ifstream fin("berarii2.in");
ofstream fout("berarii2.out");

const int dim = 1e7 + 1;

int n,m,p;
vector<int> L[dim];
int viz[dim];
queue<int> q;



void citire()
{
    fin>>n>>m>>p;
    for(int i=1;i<=m;i++)
    {
        int x,y;
        fin>>x>>y;
        L[y].push_back(x); //graf orientat
    }
    for(int i=1;i<=p;i++)
    {
        int z;
        fin>>z;
        viz[z] = 1;
        q.push(z);
    }
}




int main()
{
    citire();
    

    while(!q.empty()) {
        //bfs pentru fiecare berarie
        int curr = q.front();
        q.pop();
        for(auto v : L[curr]) {
            if(viz[v] == 0) {
                viz[v] = 1;
                q.push(v);
            }
        }
    }

    int sol = 0;
    for(int i = 1; i <= n; i ++) {
        if(viz[i] == 0)
            sol ++;
    }

    fout << sol << '\n';

    for (int i = 1; i <= n; i ++) {
        if(viz[i] == 0)
            fout << i <<"\n"; 
    }

}
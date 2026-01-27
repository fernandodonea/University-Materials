#include <fstream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
ifstream fin("maxflow.in");
ofstream fout("maxflow.out");

const int NMAX = 1e3; //dimensiune maxima n
int n, m;

int capacitate[NMAX + 1][NMAX + 1]; //matrice de capacitati

int flux[NMAX + 1][NMAX + 1]; //matrice de flux


int vis[NMAX + 1], p[NMAX + 1]; //vector de vizitati



vector<int> G[NMAX + 1]; //graful


void citire()
{
    fin>>n>>m;
    //citim graful
    for(int i=1;i<=m;i++)
    {
        int x,y,c;
        fin>>x>>y>>c;
        capacitate[x][y]=c;
        //capacitate[y][x]=0;

        G[x].push_back(y);
        G[y].push_back(x);
    }
}

int bfs(int s, int d) 
{
    //initializam vectorii de vizitati si parinti
    for(int i = 1; i <= n; i++) 
    {
        vis[i] = 0;
        p[i] = 0;
    }

    
    queue<int> q;
    q.push(s);
    vis[s] = 1;

    while(!q.empty()) 
    {
        int nod = q.front();
        q.pop();
        for(auto vecin : G[nod])  //parcurgem vecinii nodului din coada
        {
            //daca nodul nu este vizitat si capacitatea ramasa 
            if(!vis[vecin] && capacitate[nod][vecin] - flux[nod][vecin] > 0) 
            {
                vis[vecin] = 1;
                p[vecin] = nod;
                q.push(vecin);
            }
        }
    }

    if(!vis[d]) {
        return 0;
    } // nu am ajuns in sursa 


    vector<int> path;
    int x = d;
    while(x != 0) {
        path.push_back(x);
        x = p[x];
    }//iese reversed
    reverse(path.begin(), path.end());


    //calculam fluxul minim pe acest drum
    int flow = 1e9;
    for(int i = 0; i < path.size() - 1; i++) {
        int a = path[i];
        int b = path[i + 1];
        flow = min(flow, capacitate[a][b] - flux[a][b]);
    }
    //actualizam fluxurile pe acest drum
    for(int i = 0; i < path.size() - 1; i++) {
        int a = path[i];
        int b = path[i + 1];
        flux[a][b] += flow;
        flux[b][a] -= flow;
    }
    return flow;

}

int main() 
{
    citire();
    int maxflow = 0;
    while(true) {
        int flow = bfs(1, n);
        if(flow == 0) {
            break;
        }
        maxflow += flow;
    }
    fout << maxflow;
    fin.close();
    fout.close();
}
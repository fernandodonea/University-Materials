#include <queue>
#include<fstream>
using namespace std;

int d[100000],n,m,s,viz[100000];
vector<int> l[100000];

void citire(const char *nume_fisier, int &n, int &m, int &s, vector<int> l[100000]){
     ifstream f(nume_fisier);
     int x,y,i;
     f>>n>>m>>s;
     s--; //daca lucram de la 0 scadem 1 din eticheta fiecaruri varf si adunam 1 la afisarea rezultatului
     for(i=0;i<m;i++){
         f>>x>>y;
         l[x-1].push_back(y-1); //lucram de 0
         //graf orientat, nu adaugam si invers
     }
     f.close();
}

void bfs(int s){
	int x,i;
    queue<int> c; //coada folosita la parcurgere
    c.push(s); //initial se adauga in coada varful de start si se viziteaza
    viz[s]=1;
    
    d[s]=0; //d=vectorul de distante; d[v]=distanta de la s la v; 
    
    while(c.size()>0){
        x=c.front();//se elimina un varf din coada si i se parcurg vecinii
        c.pop();
        for(i=0;i<l[x].size();i++){ //l[x] = lista de adiacenta a lui x (a vecinilor)
			int y=l[x][i];
            if(viz[y]==0){ //daca un vecin este inca nevizitat=nedescoperit=alb
                c.push( y); //se insereaza in coada si se viziteaza
                viz[y]=1;
                d[y]=d[x]+1; //d[y]=distanta de la s la y = distanta de la s la x plus 1 (drumul minim de la s la x + arcul xy)
            }
        }
     }
}
int main(){
    int n,m,s,i;
    citire("bfs.in",n,m,s,l);

    for(i=0;i<n;i++)
        d[i]=-1; //initializam distantele cu o valoare care nu poate fi distanta in final, in enunt se cerea explicit -1

	bfs(s); //apelam parcurgerea din varful de start
    ofstream f("bfs.out");

     for(i=0;i<n;i++) //afisam distantele varfurilor (!varfurile le-am translatat, sunt numerotate de la 1 la n-1)
        f<<d[i]<<" ";
     f.close();
     return 0;
}

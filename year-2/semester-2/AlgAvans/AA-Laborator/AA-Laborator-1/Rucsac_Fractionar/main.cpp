#include <iostream>
#include <vector>
#include <fstream>
using namespace std;
ifstream fin("rucsac.in");

int n,C;
vector <int> v,g;
vector <float> r;


void citire()
{
    //fin>>n>>C;
    cin>>n>>C;
    v.resize(n);
    g.resize(n);
    r.resize(n);
    for(int i=0;i<n;i++)
    {
        //fin>>v[i];
        cin>>v[i];
    }
    for(int i=0;i<n;i++)
    {
        //fin>>g[i];
        cin>>g[i];
    }
    
    for(int i=0;i<n;i++)
    {
        //adaugam raportul valoare/greutate 
        r[i]=(float)v[i]/g[i];
    }

}

//complexitate n log n
void QuickSort(vector <int> &v, vector <int> &g, vector <float> &raport, int st, int dr)
{
    float pivot=raport[(st+dr)/2];
    int i=st;
    int j=dr;
    while(i<=j)
    {
        while(i<=dr && raport[i]<pivot)
            i++;
        while(j>=st && raport[j]>pivot)
            j--;
        if(i<=j)
        {
            swap(raport[i],raport[j]);
            swap(v[i],v[j]);
            swap(g[i],g[j]);
            i++;
            j--;
        }
    }

    if(st<j)
        QuickSort(v,g,raport,st,j);
    if(i<dr)
        QuickSort(v,g,raport,i,dr);
    
}

int main()
{
    citire();
    QuickSort(v,g,r,0,n-1);

    float val_rucsac=0;

    //metoda greedy
    //adaugam obiecte in rucsac iar daca mai este spatiu in rucsac dar nu mai incape urm obiect
    //il adaugam
    for(int i=n-1;i>=0 && C>0;i--)
    {
        if(C>g[i])
        {
            C=C-g[i];
            val_rucsac=val_rucsac+v[i];

        }
        else
        {
            val_rucsac=val_rucsac+(C*r[i]);
            C=0;
        }
    }
    cout<<val_rucsac;


}
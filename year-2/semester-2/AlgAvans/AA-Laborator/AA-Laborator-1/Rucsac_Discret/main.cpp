//problema NP completa

// Programare dinamica

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
ifstream fin("rucsac2.in");

int n,C;
vector<vector <int>> T;
vector<int> v,g;
//T[i][j] = profit maxim dintre primele i obiecte de greutate totala <= 'j'


//folosesc sau nu al i-lea obiect?
// T[i][j] = max { T[i-1][j],
//               val(i-1) + T[i-1][j-gr[i-1]], cu cond j-greutate[i-1]>=0 }

//stim deja
// T[0][j]=T[i][0]=0 

// SOLUTIA
//T[n][C]=solutie


/*
 COMPLEXITATE :
 timp-> O(n*C)
 spatiu-> O(C)
*/

void citire()
{
    //fin>>n>>C;
    cin>>n>>C;
    v.resize(n+1);
    g.resize(n+1);
    for(int i=0;i<n;i++)
    {
        int valoare;
        //fin>>valoare;
        cin>>valoare;
        v[i]=valoare;

    }
    for(int i=0;i<n;i++)
    {
        int greutate;
        //fin>>greutate;
        cin>>greutate;
        g[i]=greutate;
    }
}

void initPD()
{
    T.resize(n+1);
    for(int i=0;i<=n;i++)
    {
        T[i].resize(C+1);
        T[i][0]=0;
    }
    for(int j=0;j<=C;j++)    
    {
        T[0][j]=0;
    }
}
void PD()
{
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=C;j++)
        {
            if(j-g[i-1]>=0)
            {
                T[i][j]=max(T[i-1][j],v[i-1]+T[i-1][j-g[i-1]]);
            }
            else
            {
                T[i][j]=T[i-1][j];
            }
        }
    }
}

//varianta cu spatiu O(C) folosind doi vectori
vector <int> T1,T2;
void PD_2()
{
    T1.resize(C+1); //T1[j] = profit maxim dintre primele i-1 obiecte de greutate totala <= 'j'
    T2.resize(C+1); //T2[j] = profit maxim dintre primele i obiecte de greutate totala <= 'j'
    for(int j=0;j<=C;j++)    
    {
        T1[j]=0;
        T2[j]=0;
    }
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=C;j++)
        {
            if(j-g[i-1]>=0)
            {
                T2[j]=max(T1[j],v[i-1]+T1[j-g[i-1]]);
            }
            else
            {
                T2[j]=T1[j];
            }
        }
        swap(T1,T2);
    }

}

int main()
{
    citire();
    initPD();
    PD();

    cout<<T[n][C];

}
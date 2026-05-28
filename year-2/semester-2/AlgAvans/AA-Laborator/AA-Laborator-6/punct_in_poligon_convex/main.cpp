#include <iostream>

#include <vector>
#include <string>

using namespace std;

#include <fstream>
ifstream fin("input.txt");

string OUTSIDE="OUTSIDE"; //inafara poloigonuliui
string INSIDE="INSIDE"; // in poligon
string BOUNDARY="BOUNDARY"; //punctul pe se afla pe latura a poligonului


struct punct
{
    long long x,y;
};

long long test_orientare(punct A, punct B, punct C)
{
    return (B.x-A.x)*(C.y-A.y) - (B.y-A.y)*(C.x-A.x);
    /*
    <0 = dreapta
    =0 = coliniare
    >0 = stanga 
    */
}



int n,m;
vector<punct> p;
int mini=0; //punctul cu coordonata x cea mai mica

void citirePuncte()
{
    fin>>n;

    vector<punct> cp; //vector copie
    vector <punct> p_rotit;
    cp.resize(n);
    p_rotit.resize(n);

    for(int i=0;i<n;i++)
    {
        fin>>cp[i].x>>cp[i].y;

        if(cp[i].x<cp[mini].x || (cp[i].x==cp[mini].x && cp[i].y<cp[mini].y))
            mini=i;
    }

    //rotim vectorul ca minimul sa fie pe pozitie 1
    int k=mini;
    for(int i=0;i<n;i++)
    {
        p_rotit[i]=cp[k];
        k++;
        k=k%n;
    }

    /*
    TEST CASE 4 ATTEMPT AGHHH
    */

    //eliminam varfurile coliniare din pologin
    p.push_back(p_rotit[0]);
    p.push_back(p_rotit[1]);

    for(int i=2;i<n;i++)
    {
        //cat timp ultimele 2 pct salvate si pct curent sunt coliniare
        while(p.size()>=2 && test_orientare(p[p.size()-2],p[p.size()-1],p_rotit[i])==0)
        {
            p.pop_back(); //eliminima punctul din mijloc
        }
        p.push_back(p_rotit[i]);
    }

    while(p.size()>=3 && test_orientare(p[p.size()-2],p[p.size()-1],p[0])==0)
    {
        p.pop_back();
    }

    n=p.size();
}




//functie care verif daca punctul P se afal pe segmentul [A,B]
bool pe_segment(punct A, punct B, punct P)
{
    if (min(A.x,B.x)<=P.x && P.x<=max(A.x,B.x) &&
        min(A.y,B.y)<=P.y && P.y<=max(A.y,B.y))
        return true;
    else return false;
}

string localizare_punct(punct P)
{
    //verificam daca punctul X este fix p[0]
    if (P.x==p[0].x && P.y==p[0].y)
        return BOUNDARY;

    //verificam daca X se afla intre unghiul p[1],p[0],p[n-1]
    long long u1,u2;
    u1=test_orientare(p[0],p[1],P); //daca e in stanga segmentului p[0],p[1]=>afara
    u2=test_orientare(p[0],p[n-1],P);//daca e in dreapta segementului p[1],p[n-1]=>afara

    if (u1<0 || u2>0)
        return OUTSIDE;

    

    //verificam daca P se afla pe segmentele [p[0],p[1]] sau [p[0],p[n-1]]
    if (u1==0)
    {
        if (pe_segment(p[0],p[1],P)==true)
            return BOUNDARY;
        // else return OUTSIDE; 
        /*
            test case 4: varfurile polignoului pot fi coliniare
            de exemplu, varful P e coliniar cu p[0] si p[1], dar se afla intre p[1] si p[2]
        */
    }

    if (u2==0)
    {
        if(pe_segment(p[0],p[n-1],P))
            return BOUNDARY;
        // else return OUTSIDE;
    }

    //cautarea binara pentru a gasi triunghiul
    int st=1, dr=n-1;
    while(dr-st>1) //cat timp cel putin un element intre st si dr
    {
        int m=(st+dr)/2;
        if (test_orientare(p[0],p[m],P) >=0)
            st=m;
        else
            dr=m;
    }


    long long i=st;

    long long latura=test_orientare(p[i],p[i+1],P);
    if (latura>0)
        return INSIDE;
    else if (latura==0)
        return  BOUNDARY; 
    
    return OUTSIDE;

}


void queries()
{
    fin>>m;
    for(int i=0;i<m;i++)
    {
        punct P;
        fin>>P.x>>P.y;
        cout<<localizare_punct(P)<<'\n';
    }
}

int main()
{
    citirePuncte();
    queries();

    return 0;
}
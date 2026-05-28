


/*
hint: paritatea nr de intersectii
nr par te intersectii: exterior 
nr impar: interior

intersectie printr-un varf: cumva intersecteaza 2 laturi 


intersecteaza o latura: +1
interesctie de punct cu V sau ^ : + 0 (trece tangential)
intersectie de punct cu < sau >: +1 (aici inteapa varufl)
intersectez de a lungul unei laturi: nu numar deloc

- fie testez toate cazurile
- fie modific raza (mut punctul un putin mai jos)

testul de orientare: daca predecesorul si succesorul sunt de parti diferite ale razei: 

*/

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
    float x,y;
};



int n,m;
vector<punct> p;
int mini=0; //punctul cu coordonata x cea mai mica

void citirePuncte()
{
    fin>>n;
    p.resize(n);
    for(int i=0;i<n;i++)
    {
        fin>>p[i].x>>p[i].y;
    }

}




//functie care verif daca punctul P se afal pe segmentul [A,B]
bool pe_segment(punct A, punct B, punct P)
{
    if (min(A.x,B.x)<=P.x && P.x<=max(A.x,B.x) &&
        min(A.y,B.y)<=P.y && P.y<=max(A.y,B.y))
        return true;
    else return false;
}

float test_orientare(punct A, punct B, punct C)
{
    return (B.x-A.x)*(C.y-A.y) - (B.y-A.y)*(C.x-A.x);
    /*
    <0 = dreapta
    =0 = coliniare
    >0 = stanga 
    */
}
int semn(float x)
{
    if(x==0)
        return 0;
    else if(x>0)
        return 1;
    else 
        return -1;


}


bool se_intersecteaza(punct A, punct B, punct C, punct D)
{
    float test_c,test_d;
    test_c=test_orientare(A,B,C);
    test_d=test_orientare(A,B,D);


    float test_a, test_b;
    test_a=test_orientare(C,D,A);
    test_b=test_orientare(C,D,B);

    //AB si CD drepte se intersecteaza daca:
    // A si B se afla de parti diferite ale lui CD (adica au semn diferit)
    // C si D se afla de parti diferite ale lui AB
    if(semn(test_a)!=semn(test_b) && semn(test_c)!=semn(test_d))
        return true;
    else return false;


}

string localizare_punct(punct Q)
{

    //cazul 1: verificam daca Q este este pe o muchie a poligonului
    for(int i=0;i<n;++i)
    {
        punct A=p[i];
        punct B=p[(i+1)%n];

        if(test_orientare(A,B,Q)==0 && pe_segment(A,B,Q)==true)
            return BOUNDARY;
    }

    //generam punctul M
    punct M;
    M.x=Q.x;
    M.y=Q.y;

    for(int i=0;i<n;i++)
    {
        M.x=max(M.x, p[i].x);
        M.y=max(M.y, p[i].y);
    }
    //ne asiguram ca M se afla in afara poligonului
    M.x+=1;
    M.y+=1;


    //ajustam M ca segmentul MQ sa nu intersecteze niciun varf al poligonului
    bool ok=false;
    while(ok==false)
    {
        ok=true;

        for(int i=0;i<n;++i)
        {
            if(test_orientare(M,Q,p[i])==0)
            {
                M.y+=1; //daca atinge un varf, mutam Y putin mai sus
                ok=false;
                break;
            }
        }
    }

    int intersectii=0;
    for(int i=0;i<n;++i)
    {
        punct A=p[i];
        punct B=p[(i+1)%n];

        if(se_intersecteaza(A,B,M,Q))
            intersectii+=1;

    }

    if(intersectii%2==0)
        return OUTSIDE;
    else return INSIDE;
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
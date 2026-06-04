#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
// ifstream cin("input.txt");

const int ORIZ=1;
const int VERT=2;
const int NONE=0;



struct punct{
    long long x,y;
};

struct dreapta
{
    punct P,Q;
};




int clasificareDreapta(dreapta dr)
{
    if(dr.P.x == dr.Q.x)//dreapta verticala
        return VERT;
    if(dr.P.y==dr.Q.y)//dreapta orizontala
        return ORIZ;
    return NONE;
    
}

bool intersectieDreapte(dreapta dr_o, dreapta dr_v)
{

    //aflam capetele stanga dreapta pt orizontal
    //jos sus pentru vertical
    long long minX_o = min(dr_o.P.x, dr_o.Q.x);
    long long maxX_o = max(dr_o.P.x, dr_o.Q.x);
    long long minY_v = min(dr_v.P.y, dr_v.Q.y);
    long long maxY_v = max(dr_v.P.y, dr_v.Q.y);

    if (dr_v.P.x > minX_o && dr_v.P.x < maxX_o &&
        dr_o.P.y > minY_v && dr_o.P.y < maxY_v) {
        return true;
    }
    return false;
}


int n;
vector<dreapta> drepteVerticale;
vector<dreapta> drepteOrizontale;


void citire()
{
    cin>>n;
    for(int i=0;i<n;i++)
    {
        dreapta dr;
        cin>>dr.P.x>>dr.P.y;
        cin>>dr.Q.x>>dr.Q.y;
        if(clasificareDreapta(dr)==ORIZ)
            drepteOrizontale.push_back(dr);
        else if(clasificareDreapta(dr)==VERT)
            drepteVerticale.push_back(dr);

    }
    
   
}

int numaraIntersectii()
{
    int ct=0;
    for(dreapta o: drepteOrizontale)
    {
        for(dreapta v: drepteVerticale)
        {
            if(intersectieDreapte(o,v)==true)
            {
                ct+=1;

            }
        }
    }
    return ct;
}

int main()
{
    citire();
    cout<<numaraIntersectii();
}

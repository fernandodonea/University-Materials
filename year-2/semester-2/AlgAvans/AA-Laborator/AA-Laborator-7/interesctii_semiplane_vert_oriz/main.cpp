#include <iostream>
using namespace std;

// #include <fstream>
// ifstream cin("void.txt");
// ifstream cin("bounded.txt");
// ifstream cin("unbounded.txt");

#include <algorithm>




int n;
int INF=10000000;

float maxi(float a, float b)
{
    if(a>b)
        return a;
    return b;
}
float mini(float a, float b)
{
    if(a<b)
        return a;
    else return b;
}

//initializam coordonatale planului
int min_x=-INF, min_y=-INF;
int max_x=INF, max_y=INF;

int main()
{
    cin>>n;
    for(int i=0;i<n;i++)
    {
        float a, b, c;
        cin>>a>>b>>c;

        //cazul vertical
        if(a!=0)
        {
            //a*x+c<=0
            //a*x<=-c
            //x<=-c/a
            float limita=-c/a; //cordonata lui x
            if(a>0)
            {
                max_x=mini(max_x, limita);
            }
            else //se schimba senusl ineg
            {
                min_x=maxi(min_x, limita);
            }
        }
        else //cazul orizontal
        {
            //b*y+c<=0
            float limita=-c/b; //cordonata lui y
            if(b>0)
            {
                //y<=-b/c
                max_y=mini(max_y,limita);
            }
            else
            {
                //y>=-b/c
                min_y=maxi(min_y, limita);
            }
        } 

    }

    //cazul 1: void 
    if (min_x>max_x  || min_y>max_y) //daca limitele sunt inadmisibile
        cout<<"VOID";
    else if(min_x>-INF && max_x<INF && min_y>-INF && max_y<INF) //daca vreo limita a plaunui a ramas incinit
        cout<<"BOUNDED";
    else cout<<"UNBOUNDED";

    return 0;


}
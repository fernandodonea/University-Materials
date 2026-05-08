#include <iostream>
// #include <fstream>
using namespace std;
//ifstream cin("roby.in");
//ofstream cout("roby.out");

struct punct
{
    long long x,y;

};


long long orientare(punct A, punct B, punct C)
{
    //dreapta a,b
    //orientarea punctului
    
    /*
    | 1  1  1  |
    |xa  xb xc |
    |ya  yb yc |

    */
    long long delta=(B.x-A.x)*(C.y-A.y) - (B.y-A.y)*(C.x-A.x);
    return delta;
}


int main()
{
    int n;
    cin>>n;

    int st=0,dr=0,ct=0;

    punct start, A, B;
    cin>>A.x>>A.y;
    cin>>B.x>>B.y;
    start=A;

    
    for(int i=3;i<=n;i++)
    {
        punct C;
        cin>>C.x>>C.y;
        if(orientare(A,B,C)<0)
            dr++;
        else if(orientare(A,B,C)>0)
            st++;
        else ct++;

        A=B;
        B=C;
    }

    //dupa ce am terminat toate punctele tre sa ne intoarcem in origine
    if(orientare(A,B,start)<0)
        dr++;
    else if(orientare(A,B,start)>0)
        st++;
    else ct++;

    cout<<st<<" "<<dr<<" "<<ct;


    
    return 0;
}
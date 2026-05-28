#include <iostream>

using namespace std;

// #include <fstream>
// ifstream cin("input.txt");


/*
    test case 3: imi da overflow??
 */

struct punct
{
    long long x,y;
};


punct A,B,C;//coordonate triunghji


void citireTriunghi()
{
    cin>>A.x>>A.y;
    cin>>B.x>>B.y;
    cin>>C.x>>C.y;
}




__int128_t getDeterminantGrad3(__int128_t a1, __int128_t a2, __int128_t a3, __int128_t b1, __int128_t b2, __int128_t b3, __int128_t c1, __int128_t c2, __int128_t c3)
{
/*
a1 a2 a3
b1 b2 b3
c1 c2 c3
*/


    __int128_t delta=0;
    delta+=a1*b2*c3;//diag principala
    delta+=a2*b3*c1;
    delta+=b1*c2*a3;

    delta-=a3*b2*c1;//diag secundara
    delta-=c2*b3*a1;
    delta-=b1*a2*c3;

    return delta;
}

__int128_t criteriuNumeric(punct A, punct B, punct C, punct D)
{
    __int128_t delta1=A.x * getDeterminantGrad3(B.y, B.x*B.x+B.y*B.y, 1,
                                                  C.y, C.x*C.x+C.y*C.y, 1,
                                                  D.y, D.x*D.x+D.y*D.y, 1);
                                                  
    
    __int128_t delta2=B.x * getDeterminantGrad3(A.y, A.x*A.x+A.y*A.y, 1,
                                                  C.y, C.x*C.x+C.y*C.y, 1,
                                                  D.y, D.x*D.x+D.y*D.y, 1);
                                                  
   
    __int128_t delta3=C.x * getDeterminantGrad3(A.y, A.x*A.x + A.y*A.y, 1,
                                                  B.y, B.x*B.x+B.y*B.y, 1,
                                                  D.y, D.x*D.x+D.y*D.y, 1);
                                                  
    
    __int128_t delta4=D.x * getDeterminantGrad3(A.y, A.x*A.x+A.y*A.y, 1,
                                                  B.y, B.x*B.x+B.y*B.y, 1,
                                                  C.y, C.x*C.x+C.y*C.y, 1);

    __int128_t delta=delta1-delta2+delta3-delta4;
    return delta;
}


void queries()
{
    int m;
    cin>>m;
    for(int i=0;i<m;i++)
    {
        punct P;
        cin>>P.x>>P.y;
        __int128_t delta=criteriuNumeric(A,B,C,P);

        if(delta==0)
            cout<<"BOUNDARY"<<'\n';
        else if(delta<0)
            cout<<"OUTSIDE"<<"\n";
        else cout<<"INSIDE"<<"\n";
    }
}




int main()
{
    citireTriunghi();
    queries();
    return 0;
}
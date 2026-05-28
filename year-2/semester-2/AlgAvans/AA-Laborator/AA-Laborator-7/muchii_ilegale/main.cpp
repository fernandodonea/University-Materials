#include <iostream>
// #include <fstream>
using namespace std;

// ifstream cin("input.txt");


struct punct
{
    long long x,y;
};


punct A,B,C,D;//coordonate triunghji


void citirePatrulater()
{
    cin>>A.x>>A.y;
    cin>>B.x>>B.y;
    cin>>C.x>>C.y;
    cin>>D.x>>D.y;
}




int getDeterminantGrad3(int a1, int a2, int a3, int b1, int b2, int b3, int c1, int c2, int c3)
{
/*
a1 a2 a3
b1 b2 b3
c1 c2 c3
*/


    int delta=0;
    delta+=a1*b2*c3;//diag principala
    delta+=a2*b3*c1;
    delta+=b1*c2*a3;

    delta-=a3*b2*c1;//diag secundara
    delta-=c2*b3*a1;
    delta-=b1*a2*c3;

    return delta;
}

int criteriuNumeric(punct A, punct B, punct C, punct D)
{
    int delta1=A.x * getDeterminantGrad3(B.y, B.x*B.x+B.y*B.y, 1,
                                                  C.y, C.x*C.x+C.y*C.y, 1,
                                                  D.y, D.x*D.x+D.y*D.y, 1);
                                                  
    
    int delta2=B.x * getDeterminantGrad3(A.y, A.x*A.x+A.y*A.y, 1,
                                                  C.y, C.x*C.x+C.y*C.y, 1,
                                                  D.y, D.x*D.x+D.y*D.y, 1);
                                                  
   
    int delta3=C.x * getDeterminantGrad3(A.y, A.x*A.x + A.y*A.y, 1,
                                                  B.y, B.x*B.x+B.y*B.y, 1,
                                                  D.y, D.x*D.x+D.y*D.y, 1);
                                                  
    
    int delta4=D.x * getDeterminantGrad3(A.y, A.x*A.x+A.y*A.y, 1,
                                                  B.y, B.x*B.x+B.y*B.y, 1,
                                                  C.y, C.x*C.x+C.y*C.y, 1);

    int delta=delta1-delta2+delta3-delta4;
    return delta;
}


void testareDiagonale()
{
    int detAC=criteriuNumeric(A,B,C,D);

    //punctul D este in interiorul cercului circumscris triunghiului A,B,C
    if(detAC>0)
    {
        cout<<"AC: ILLEGAL"<<"\n";
    }
    else{
        cout<<"AC: LEGAL"<<"\n";
    }

    int detBD=criteriuNumeric(B,C,D,A);
    if(detBD>0)
    {
        cout<<"BD: ILLEGAL"<<"\n";
    }
    else{
        cout<<"BD: LEGAL"<<"\n";
    }
}




int main()
{
    citirePatrulater();
    testareDiagonale();
    return 0;
}
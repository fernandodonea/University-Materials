#include <iostream>
#include <fstream>
using namespace std;
// ifstream fin("orientare.in");

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

    for(int i=0;i<n;i++)
    {
        punct P,Q,R;
        cin>>P.x>>P.y;
        cin>>Q.x>>Q.y;
        cin>>R.x>>R.y;

        if(orientare(P,Q,R)<0)
            cout<<"RIGHT"<<endl;
        else if(orientare(P,Q,R)>0)
            cout<<"LEFT"<<endl;
        else cout<<"TOUCH"<<endl;
    }
    
    return 0;
}
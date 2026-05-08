#include <iostream>
// #include <fstream>
#include <stack>
#include <vector>

using namespace std;

// ifstream fin("triunghi.in");
// ifstream fin("stea.in");
// ifstream fin("patrat.in");




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

int n;
int mini;//indexul punctului cel mai din stanga jos
vector<punct> p;


void citire()
{
    cin>>n;
    p.resize(n);
    vector<punct> cp(n);
    for(int i=0;i<n;i++)
    {
        cin>>cp[i].x>>cp[i].y;
        
        //cautam punctul cel mai din stanga
        if(cp[i].x<cp[mini].x || ((cp[i].y==cp[mini].y && cp[i].x<cp[mini].x)))
        {
            mini=i;
        }
    }

    //reindexam vectorul ca sa pastram sensu
    int k=mini;
    for(int i=0;i<n;i++)
    {
        p[i]=cp[k];
        k++;
        k=k%n;
    }
    p.push_back(p[0]);//aduagm vf din stanga din nou pt a inchide poligonu
}


void GrahamScan()
{
    vector<punct> s;//simulam o stiva
    s.push_back(p[0]);
    s.push_back(p[1]);
    for(int i=2;i<=n;i++)
    {

        //cat timp avem macar 2 pct si noul punct face viraj la dreaptw
        while(s.size()>=2 && orientare(s[s.size()-2],s.back(),p[i])<=0)
        {
            s.pop_back();
        }
        s.push_back(p[i]);
    }

    s.pop_back();//scoatem primu elemnt


    cout<<s.size()<<endl;
    for(int i=0;i<s.size();i++)
    {
        cout<<s[i].x<<" "<<s[i].y<<endl;
    }

}

int main()
{
    citire();
    GrahamScan();

}
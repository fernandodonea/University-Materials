#include <iostream>
// #include <fstream>
using namespace std;
// ifstream cin("AplusB.in");
// ofstream cout("AplusB.out");
int main()
{
    int n;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        int a,b;
        cin>>a>>b;
        cout<<a+b<<endl;
    }
    return 0;
    
}
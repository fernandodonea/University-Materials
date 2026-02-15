#include <iostream>
using namespace std;
vector <int> L[101];
int main()
{
    int n,a[101][101],m;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        cin>>m;
        for(int j=1;j<=m;j++)
        {
            int x;
            cin>>x;
            a[i][x]=1;
        }
    }
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            cout<<a[i][j]<<" ";
        }
        cout<<"\n";
    }
    return 0;
    
}
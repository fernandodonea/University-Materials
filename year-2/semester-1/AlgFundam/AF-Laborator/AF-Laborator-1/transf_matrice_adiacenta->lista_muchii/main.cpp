#include <iostream>
using namespace std;
vector <int> L[101];
int main()
{
    int n,a[101][101];
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            cin>>a[i][j];
        }
    }
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=i;j++)
        {
            if(a[i][j]==1)
            {
                cout<<j<<" "<<i<<endl;
            }

        }
    }
    
}
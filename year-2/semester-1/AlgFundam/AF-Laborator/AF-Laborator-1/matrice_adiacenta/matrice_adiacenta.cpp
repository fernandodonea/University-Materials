//
// Created by Fernando-Emanuel Donea on 14.10.2025.
//
#include <iostream>
using namespace std;
int main()
{
    int n,m,a[101][101];
    cin>>n>>m;
    for (int i=1;i<=m;i++)
    {
        int x,y;
        cin>>x>>y;
        a[x][y]=a[y][x]=1;
    }
    for (int i=1;i<=n;i++)
    {
        for (int j=1;j<=m;j++)
            cout<<a[i][j]<<" ";
        cout<<endl;
    }

}
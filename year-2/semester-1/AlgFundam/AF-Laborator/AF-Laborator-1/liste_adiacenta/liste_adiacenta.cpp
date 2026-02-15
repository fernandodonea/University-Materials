//
// Created by Fernando-Emanuel Donea on 14.10.2025.
//
//
//  #414_ListaVecini.cpp
//  AF-Laborator-1
//
//  Created by Fernando-Emanuel Donea on 14.10.2025.
//

#include <fstream>
#include <algorithm>
using namespace std; 
ifstream fin("listavecini.in");
ofstream fout("listavecini.out");
vector<vector<int>> L;
int main()
{
    int n,x,y;
    fin>>n;
    L.resize(n+1);
    while(fin>>x>>y)
    {
        L[x].push_back(y);
        L[y].push_back(x);

    }
    for(int i=1;i<=n;i++)
    {
        //necesar pentru unique
        sort(L[i].begin(),L[i].end());

        L[i].erase(unique(L[i].begin(),L[i].end()),L[i].end());
        int w=L[i].size();
        fout<<w<<" ";
        for(int j=0;j<w;j++)
        {
            fout<<L[i][j]<<" ";
        }
        fout<<'\n';
        // 1 1 2 2 2 3
        // 1 2 3 | 2 2 1
    }

    return 0;
}

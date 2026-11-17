//
// Created by Fernando-Emanuel Donea on 08.04.2026.
//

#include "../include/Helper.h"

std::string fromIntToBinary(int x, int n)
{
    std::string s;
    s.resize(n);

    int ct=n-1;
    for (int i=0;i<n;i++) {
        s[i]='0';
    }
    while (x!=0)
    {
        int c=x%2;
        x=x/2;
        if (c==1)
            s[ct]='1';
        ct--;
    }
    return s;
}

int fromBinaryToInt(std::string s)
{
    int x=0,putere=0;
    for (int i=s.size()-1;i>=0;i--)
    {
        if (s[i]=='1')
            x=x+pow(2,putere);
        putere++;
    }
    return x;
}


double functieGradulDoi(double a, double b, double c, double x)
{
    return a*(x*x)+b*x+c;
}

double getNumarRandomReal(double a, double b)
{
    static thread_local std::mt19937 rng(std::random_device{}());
    std::uniform_real_distribution <double> dist(a,b);

    return dist(rng);
}

int getNumarRandomIntreg(int a, int b) {
    static thread_local std::mt19937 rng(std::random_device{}());
    std::uniform_int_distribution <int> dist(a,b);

    return dist(rng);
}

int cautareBinara(int st, int dr, double x, std::vector<double> v)
{
    while (st<dr)
    {
        int m=(st+dr)/2;
        if (x<v[m])
            dr=m;
        else
            st=m+1;
    }
    return st-1;
}


std::string incrucisareString(std::string s1, std::string s2, int r)
{
    int n=s1.size();
    std::string aux;
    for (int i=0;i<r;i++)
        aux+=s1[i];
    for (int i=r;i<n;i++)
        aux+=s2[i];
    return aux;

}


void bigBreak(std::ostream& out)
{
    out<<"------------------------------------------------------"<<std::endl;
    out<<"------------------------------------------------------"<<std::endl;
}
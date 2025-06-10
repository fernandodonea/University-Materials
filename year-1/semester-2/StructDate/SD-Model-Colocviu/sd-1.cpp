#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


struct stiva
{
    stiva *next;
    string nume;
};



void push(stiva* &st, std::string val)
{
    stiva *t=new stiva;
    t->nume=val;

    if (st==NULL)
    {
        t->next=NULL;
        st=t;
    }
    else
    {
        t->next=st;
        st=t;
    }
}


void pop(stiva* &st)
{
    st=st->next;
}



//returneaza varful stivei
string top(stiva *st)
{
    return st->nume;
}

bool empty(stiva *st)
{
    return st==NULL;
}

int main() {

    stiva *st=NULL;
    int n;
    cin>>n;
    for (int i=1;i<=n;i++)
    {
        string op;
        cin>>op;
        if (op=="cd")
        {
            string s;
            cin>>s;
            if (s=="..")
            {
                if (empty(st)==false)
                    pop(st);
            }
            else
            {
                push(st,s);
            }
        }
        else if (op=="pwd")
        {
            if (empty(st)==true)
            {
                cout<<"/"<<"\n";
            }
            else
            {
                cout<<top(st);
            }
        }
    }
    return 0;
}

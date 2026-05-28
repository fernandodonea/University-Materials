#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
// ifstream fin("codificare2.in");


int a,b; //intervalul [a,b]
int p; //precizia
int m; //numarul de teste

int l; //numarul de cromozomi
float d; //descretizare

int numarCromozomi()
{
    return ceil(log2((b-a)*pow(10,p)));
}
float descretizare()
{
    return (b-a)/(pow(2,l));
}


string fromIntToBinary(int x)
{
    string b;
    b.resize(l);
    for(int i=0;i<l;i++)
    {
        b[i]='0';
    }

    int ct=l-1;
    while(x!=0)
    {
        int rest=x%2;
        x=x/2;

        if(rest==1)
        {
            b[ct]='1';
        }
        ct--;
    }

    return b;

}
int fromBinaryToInt(string b)
{
    int x=0;
    int power=0;
    for(int i=l-1;i>=0;i--)
    {
        if(b[i]=='1')
        {
            x=x+pow(2,power);
        }
        power+=1;
    }
    return x;
}



void TO(float x)
{
    int index =(int)((x-a)/d);
    cout<<fromIntToBinary(index)<<endl;
}


void FROM(string b)
{
    int index=fromBinaryToInt(b);
    cout<<a+index*d<<endl;
}



void citire()
{
    // fin>>a>>b;
    // fin>>p;
    // fin>>m;

    cin>>a>>b;
    cin>>p;
    cin>>m;

}

int main()
{
    citire();

    l=numarCromozomi();
    d=descretizare();

    for(int i=1;i<=m;i++)
    {
        string instruction;
        //fin>>instruction;
        cin>>instruction;
        if(instruction=="TO")
        {
            float x;
            //fin>>x;
            cin>>x;
            TO(x);
        }
        else
        {
            string b;
            // fin>>b;
            cin>>b;
            FROM(b);
        }
    }
    return 0;
}



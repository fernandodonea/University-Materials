#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
ifstream fin("input.txt");


struct punct
{
    long long x,y;
};

int n;
vector<punct> p;


int st,dr,sus,jos;


void citire()
{

    fin>>n;
    for(int i=0;i<n;i++)
    {
        punct a;
        fin>>a.x>>a.y;
        p.push_back(a);  

        //aflam extemitatile
        if(p[i].x < p[st].x)st=i;
        if(p[dr].x<p[i].x)dr=i;
        
        if(p[sus].y<p[i].y)sus=i;
        if(p[jos].y>p[i].y)jos=i;
    }
    
}


bool monotonie_OX()
{

    //lantul de la minim la maxim
    int curent=st;
    while(curent!=dr)
    {
        int urmator=(curent+1)%n;

        if(p[curent].x>p[urmator].x)
            return false;//a scazut inante sa ajunga la maxim deci nu e monton  

        curent=urmator;
    }

    curent=dr;
    while(curent!=st)
    {
        int urmator=(curent+1)%n;

        if(p[curent].x < p[urmator].x)
            return false;//a crescaut inante sa ajunga la minim deci nu e monton  

        curent=urmator;

    }

    return  true;

}

bool monotonie_OY()
{

    //lantul de la minim la maxim
    int curent=jos;
    while(curent!=sus)
    {
        int urmator=(curent+1)%n;

        if(p[curent].y>p[urmator].y)
            return false;//a scazut inante sa ajunga la maxim deci nu e monton  

        curent=urmator;
    }

    curent=sus;
    while(curent!=jos)
    {
        int urmator=(curent+1)%n;

        if(p[curent].y < p[urmator].y)
            return false;//a crescaut inante sa ajunga la minim deci nu e monton  

        curent=urmator;

    }
    return  true;

}

int main()
{
    citire();

    if(monotonie_OX()==true)
        cout<<"YES"<<endl;
    else cout<<"NO"<<endl;

    if(monotonie_OY()==true)
        cout<<"YES"<<endl;
    else cout<<"NO";


    return 0;

}


#include <iostream>
using namespace std;

#include <fstream>
// ifstream cin("input3.txt");


#include <algorithm>
#include <iomanip>
#include <vector>


double maxi(double a, double b)
{
    if(a>b)
        return a;
    return b;
}
double mini(double a, double b)
{
    if(a<b)
        return a;
    else return b;
}


int n;
int INF=10000000;



//initializam coordonatale planului
vector<double> st; 
vector<double> dr;
vector<double> sus;
vector<double> jos;


void citireDrepte()
{
    cin>>n;
    for(int i=0;i<n;i++)
    {
        double a, b, c;
        cin>>a>>b>>c;

        //cazul vertical
        if(a!=0)
        {
            //a*x+c<=0  <=>   x<=-c/a

            double limita=-c/a;
            if(a>0) //perete dreapta
            {
                dr.push_back(limita);
            }
            else //se schimba senusl ineg
            {
                st.push_back(limita);
            }
        }
        else //cazul orizontal
        {
            double limita=-c/b;
            if(b>0)
            {
                sus.push_back(limita);
            }
            else
            {
                jos.push_back(limita);
            }
        } 

    }

}

bool dreptunghih_valid(double b_st, double b_dr, double b_sus, double b_jos)
{
    if(b_st>-INF && b_dr<INF && b_sus<INF && b_jos>-INF)
        return true;
    else return false;
}

void queries()
{
    int m;
    cin>>m;
    for(int i=0;i<m;i++)
    {
        double Qx, Qy;
        cin>>Qx>>Qy;


        double b_st=-INF,b_dr=INF,b_sus=INF,b_jos=-INF;
        //parcurgem toate dreptele si incercam sa construim un dreptunghi interesant

        for(auto val:st)
        {
            if(val<Qx) // trebuie sa fie in stanga punctului
            {
                b_st=maxi(b_st, val); //cea mai apropiata de punct
            }
        }
        for(auto val:dr)
        {
            if(val>Qx)
            {
                b_dr=mini(b_dr, val);
            }
        }
        for(auto val:sus)
        {
            if(val>Qy)
            {
                b_sus=mini(b_sus, val);
            }
        }
        for(auto val:jos)
        {
            if(val<Qy)
            {
                b_jos=maxi(b_jos, val);
            }
        }


        if(dreptunghih_valid(b_st, b_dr, b_sus, b_jos))
        {
            cout<<"YES"<<endl;
            double arie=(b_dr -b_st)*(b_sus-b_jos);
            cout<<fixed<<setprecision(6)<<arie<<endl;
        }
        else
        {
            cout<<"NO"<<endl;
        }   
    }
}

int main()
{
    citireDrepte();
    queries();

    return 0;


}
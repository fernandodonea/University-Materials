#include <fstream>
#include <iostream>
using namespace std;
ifstream fin("interclasari.in");
ofstream fout("interclasari.out");


int H[20000001];
int sz;

int parinte(int i)
{
    return i/2;
}
int fiu_stang(int i)
{
    return 2*i;
}
int fiu_drept(int i)
{
    return 2*i+1;
}

int minim()
{
    return H[1];
}


void urcare(int pos)
{
    while(pos>1 && H[pos]<H[parinte(pos)])
    {
        swap(H[pos],H[parinte(pos)]);
        pos=parinte(pos);
    }
}
void inserare(int x)
{
    sz++;
    H[sz]=x;
    urcare(sz);
}


void coborare(int pos)
{
    while(true)
    {
        //verificam daca e frunza
        if(fiu_stang(pos)>sz)
            break;
        
        //verificam care dintre fii este mai mic
        int next_pos=fiu_stang(pos);
        if(fiu_drept(pos)<=sz && H[fiu_drept(pos)]<H[next_pos])
        {
            next_pos=fiu_drept(pos);
        }

        if(H[pos]>H[next_pos])
        {
            swap(H[pos],H[next_pos]);
            pos=next_pos;
        }
        else break;
    }
}
void stergeMin()
{
    swap(H[1],H[sz]);
    sz--;
    coborare(1);
}

int main()
{
    int k;
    fin>>k;

    int n=0;
    //parcurgem echipele
    for(int i=1;i<=k;i++)
    {
        int m;
        fin>>m;
        n+=m;

        for(int i=1;i<=m;i++)
        {
            int poza;
            fin>>poza;
            inserare(poza);
        }
    }
    fout<<n<<endl;
    for(int i=1;i<=n;i++)
    {
        fout<<minim()<<" ";
        stergeMin();
    }
}
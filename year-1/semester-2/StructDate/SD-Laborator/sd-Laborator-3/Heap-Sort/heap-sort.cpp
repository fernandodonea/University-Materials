#include <iostream>
using namespace std;

int H[1000];
int sz=0;

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


void urcare(int pos)
{
    while(pos>=1 && H[pos]<H[parinte(pos)])
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

int minim()
{
    return H[1];
}

void coborare(int pos)
{
    while(true)
    {
        //verificam daca e frunza
        if(fiu_stang(pos)>sz)
            break;
        
        //trebuie sa dam swap cu fiul cel mai mic
        //nodul poate avea 2 fii (sigur are stang)

        int next_pos=fiu_stang(pos);
        if(fiu_drept(pos)<=sz && H[fiu_drept(pos)]<H[next_pos])
            next_pos=fiu_drept(pos);

        if(H[pos]>H[next_pos])
        {
            swap(H[pos],H[next_pos]);
            pos=next_pos;
        }
        else
        {
            break;
        }
    }
}

void stergeMin()
{
    swap(H[1],H[sz]);
    sz--;
    coborare(1);
}

void HeapSort(int n,int v[])
{
    sz=0;
    for(int i=1;i<=n;i++)
    {
        inserare(v[i]);
    }
    for(int i=1;i<=n;i++)
    {
        cout<<minim()<<" ";
        stergeMin();
    }
}

int main()
{
    int n;
    cout<<"n=";cin>>n;
    int v[n+2];
    for(int i=1;i<=n;i++)
    {
        cin>>v[i];
    }
    HeapSort(n,v);

}
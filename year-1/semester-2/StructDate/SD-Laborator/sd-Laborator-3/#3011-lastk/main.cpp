#include <iostream>
using namespace std;


int H[1000001];
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

        //verificam care fiu este mai mic
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


int main()
{
    int n,k;
    cin>>n>>k;

    int A,B,C,D;
    cin>>A>>B>>C>>D;

    inserare(A);

    int prev=A;
    for(int i=2;i<=n;i++)
    {
        long long x=(B*prev+C)%D;
        
        if(i<=k)
        {
            inserare(x);
        }
        else
        {
            if(x>minim())
            {
                stergeMin();
                inserare(x);
            }
        }

        prev=x;
    }
    for(int i=1;i<=k;i++)
    {
        cout<<minim()<<" ";
        stergeMin();
    }


}
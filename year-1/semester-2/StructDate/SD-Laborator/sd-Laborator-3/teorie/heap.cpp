#include <iostream>
using namespace std;

int Heap[1000];
int sz=0;

int parinte(int i)
{
    return i/2;
}
int left_son(int i)
{
    return 2*i;
}
int right_son(int i)
{
    return 2*i+1;
}


void urcare(int pos)
{
    while(pos>1 && Heap[pos]<Heap[parinte(pos)])
    {
        swap(Heap[pos],Heap[parinte(pos)]);
        pos=parinte(pos);
    }
}
void inserare(int x)
{
    sz++;
    Heap[sz]=x;
    urcare(sz);
}

int minim()
{
    return Heap[1];
}

void coborare(int pos)
{
    while(true)
    {
        //verificam daca nodul este frunza
        if(left_son(pos)>sz)
            break;
        
        //interschimbam nodul cu cel mai mic dintre fii sai

        //nodul poate avea un fiu sau doi fii (sigur are fiu stang)
        int next_pos=left_son(pos);

        if(right_son(pos)<=sz && Heap[right_son(pos)]<Heap[next_pos])
            next_pos=right_son(pos);
        
        //verificam daca se afla pe pozitia corecta
        if(Heap[pos]>Heap[next_pos])
        {
            swap(Heap[pos],Heap[next_pos]);
            pos=next_pos;
        }
        else{
            break;
        }
    }
}
void sterge_min()
{
    swap(Heap[1],Heap[sz]);
    sz--;
    coborare(1);
}




int main()
{
    cin>>sz;
    for(int i=1;i<=sz;i++)
    {
        cin>>Heap[i];
    }
    for(int i=sz/2;i>=1;i--)
    {
        coborare(i);
    }
    for(int i=1;i<=sz;i++)
    {
        cout<<Heap[i]<<" ";
    }
        return 0;
}
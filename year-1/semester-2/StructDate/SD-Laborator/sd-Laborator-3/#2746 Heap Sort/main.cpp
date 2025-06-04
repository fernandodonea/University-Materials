#include <fstream>
using namespace std;
ifstream fin("heap_sort.in");
ofstream fout("heap_sort.out");

int H[1000001];
int sz;

int parent(int pos)
{
    return pos/2;
}

int left_son(int pos)
{
    return 2*pos;
}

int right_son(int pos)
{
    return 2*pos+1;
}

void urcare(int pos)
{
    while(pos>1 && H[pos]<H[parent(pos)])
    {
        swap(H[pos],H[parent(pos)]);
        pos=parent(pos);
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
        //verificam daca nodul este frunza
        if(left_son(pos)>sz){
            break;
        }

        //nodul poate avea un fiu sau 2 fii (sigur are fiu stang)
        int next_pos=left_son(pos);
        if(right_son(pos)<=sz && H[right_son(pos)]<H[next_pos])
        {
            next_pos=right_son(pos);
        }
        if(H[pos]>H[next_pos])
        {
            swap(H[pos],H[next_pos]);
            pos=next_pos;
        }
        else{
            break;
        }
    }
}

void sterge_min()
{
    swap(H[1],H[sz]);
    sz--;
    coborare(1);
}

int main()
{
    fin>>sz;
    for(int i=1;i<=sz;i++)
    {
        fin>>H[i];
    }
    for(int i=sz/2;i>=1;i--)
    {
        coborare(i);
    }
    while(sz>0)
    {
        fout<<minim()<<" ";
        sterge_min();
    }

}
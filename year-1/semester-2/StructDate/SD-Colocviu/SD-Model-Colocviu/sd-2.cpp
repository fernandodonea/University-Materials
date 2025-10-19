#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


struct Node
{
    int dist,val;
};
Node heap[100001];
int sz=0;



int parent(int x)
{
    return x/2;
}
int left_son(int x)
{
    return 2*x;
}
int right_son(int x)
{
    return 2*x+1;
}




/*
 functie de comporare
 returneaza true daca n1 este mai mare decat n2
 */
bool cmp(Node n1, Node n2)
{
    if (n1.dist>n2.dist)
        return true;
    else if (n1.dist==n2.dist && n1.val >n2.val)
        return true;
    return false;
}


void heapUp(int pos)
{
    while (pos>1)
    {
        if (cmp(heap[pos],heap[parent(pos)]))
        {
            swap(heap[pos],heap[parent(pos)]); //schimbam valorile in hep
            pos=parent(pos); //modificam pozitia
        }
        else break;
    }
}

void heapDown(int pos)
{
    while (true)
    {
        //am ajuns intr-o frunza a heap-ului
        if (left_son(pos)>sz)
            break;


        //vedem care este fiul mai amre
        int next_pos=left_son(pos);
        if (right_son(pos)<=sz && cmp(heap[right_son(pos)],heap[next_pos]))
            next_pos=right_son(pos);

        if (cmp(heap[pos],heap[next_pos]))
            break;
        else
        {
            swap(heap[pos],heap[next_pos]);
            pos=next_pos;
        }
    }
}


void inserare(Node nd)
{
    sz++;
    heap[sz]=nd;
    heapUp(sz);
}

void stergeRadacina()
{
    swap(heap[1],heap[sz]);
    sz--;
    heapDown(1);
}



int main() {
    int n,k,x;
    cin>>n>>k>>x;

    for (int i=1;i<=n;i++)
    {
        int val;
        cin>>val;

        Node nd={abs(x-val),val};
        if (sz<k)
        {
            inserare(nd);
        }
        else
        {
            if (cmp(nd,heap[1])==false)
            {
                stergeRadacina();
                inserare(nd);
            }
        }
    }

    //afisare heap (nu conteaza ordinea)
    for (int i=1;i<=k;i++)
        cout<<heap[i].val<<" ";

    return 0;
}
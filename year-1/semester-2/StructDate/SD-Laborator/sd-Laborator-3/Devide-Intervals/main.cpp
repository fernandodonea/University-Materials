#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:


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
int minGroups(vector<vector<int>>& intervals) {
    // Sortam intervalele după început
    sort(intervals.begin(), intervals.end());
    sz = 0; // resetăm heap-ul

    for (auto& interval : intervals) {
        // Dacă există un grup care se termină înainte de intervalul curent, 
        // îl reutilizăm
        if (sz > 0 && minim() < interval[0]) {
            stergeMin();
        }
        // Adaugă capătul intervalului curent în heap (ca grup nou sau actualizat)
        inserare(interval[1]);
    }
    return sz; // numărul minim de grupuri
}



};
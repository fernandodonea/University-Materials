#include <iostream>
using namespace std;

struct node{
    int info;
    node *next;
};


void adaugareFinal(node* &head, node *&last, int x)
{  
    node *p=new node;
    p->info=x;
    p->next=NULL;

    //verificam daca lista este goala
    if (head==NULL)
    {
        head=p;
        last=p;
    }
    else
    {
        last->next=p;
        last=p;
    }
}//complexitate O(1)


//nu este nevoie de referinta intrucat nu modificam lista
void parcurgere(node *head)
{
    while(head!=NULL)
    {
        cout<<head->info<<" ";
        head=head->next;
    }
    cout<<endl;
}


void adaugareInceput(node* &head, node *&last, int x)
{
    node *p=new node;
    p->info=x;
    p->next=NULL;
    if(head==NULL)
    {
        head=p;
        last=p;
    }
    else
    {
        p->next=head;
        head=p;
    }
}//complexitate O(1)


void adaugarePozitie(node* &head, node *&last, int x, int poz)
{
    node *p=new node;
    p->info=x;
    p->next=NULL;

    //presupunem ca poz este un numar valid diferit de 1 si de n
    node *t=head;
    for(int i=1;i<poz;i++)
    {
        t=t->next;
    }

    p->next=t->next;
    t->next=p;

}//complexitate O(poz)


void stergereInceput(node* &head)
{
    node *p=head;
    head=head->next;
    delete p;
}

void stergereFinal(node* &head, node *&last)
{
    node *p=head;
    while(p->next->next!=NULL)
    {
        p=p->next;//parcurgem pana la penultimul element
    }

    //eliberam zona din memorie
    node *t=p->next;
    delete t;

    p->next=NULL;
    last=p;
}

void stergerePozitie(node* &head, int poz)
{
    node *p=head;
    for(int i=1;i<poz-1;i++)
    {
        p=p->next;//parcurgem pana la elementul anterior celui pe care vrem sa il stergem
    }

    node *q=p->next->next;

    //eliberare memorie
    node *t=p->next;
    delete t;

    p->next=q;
}
int main()
{
    node *head=NULL;
    node *last=NULL;
    for(int i=1;i<=10;i++)
    {
        adaugareInceput(head,last,i);
    }

    adaugarePozitie(head,last,6969,3);
    parcurgere(head);
    stergereInceput(head);
    parcurgere(head);
    stergerePozitie(head,3);
    parcurgere(head);
    return 0;
}


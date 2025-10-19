#include <iostream>
using namespace std;

struct Node
{
    Node *next;
    int info;
};

void parcurgere(Node *head)
{
    Node *i=head;
    while(i!=NULL)
    {
        cout<<i->info<<" ";
        i=i->next;
    }
    cout<<endl;
}


void adaugareInceput(Node* &head, Node* last, int val)
{
    Node* p=new Node;
    p->info=val;
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
}


void adaugareFinal(Node* &head, Node* &last, int val)
{

    Node* p=new Node;
    p->info=val;
    p->next=NULL;

    //verificam daca lista este vid
    if(head==NULL)
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





void adaugarePos(Node *head, Node*last, int pos, int val)
{
    Node *p=new Node;
    p->info=val;
    p->next=NULL;


    //presupunem ca pos este un numar diferit de 1 si de n
    Node *t=head;
    for(int i=2;i<=pos-1;i++)
    {
        t=t->next;
    }

    p->next=t->next;
    t->next=p;

}//complexitate O(pos)


int cautare(Node* head, int val)
{
    Node *p=head;
    int i=0;
    while(p->next!=NULL)
    {
        i++;
        if(p->info==val)
        {
            return i;
        }
        p=p->next;
    }
    return -1;
}



void stergereInceput(Node* &head)
{
    Node *p=head;
    head=head->next;
    delete p;
}



void stergereFinal(Node* &head, Node* &last)
{
    Node *p=head;
    //parcurgem pana la penultimul element
    while(p->next!=last)
    {
        p=p->next;
    }

    //elibera zona de memorie
    Node *t=p->next;
    delete t;

    p->next=NULL;
    last=NULL;
}



void stergerePos(Node* &head, Node* &last, int pos)
{
    Node *p=head;
    for(int i=2;i<=pos-1;i++)
    {
        p=p->next;//parcurgem pana la elementul anterior celui pe care vrem sa il stergem
    }

    //salvam nodul de dupa cel dorit
    Node *q=p->next->next;

    //nodul pe care vrem sa il stegem
    Node *temp=p->next;
    delete temp;

    p->next=q;
}

void stergeAparitie(Node *head, int val)
{
    Node *p=head;
    while(p->next->info!=val)
    {
        p=p->next;
    }

    Node *q=p->next->next;

    Node *temp=p->next;
    delete temp;

    p->next=q;

}

int main()
{
    Node *head=NULL;
    Node *last=NULL;

    int n;
    cout<<"n=";cin>>n;
    for(int i=1;i<=n;i++)
    {
        int x;
        cin>>x;
        adaugareFinal(head,last,x);
    }

    cout<<"Adaugam pe pozitia 4 valoarea 0"<<endl;
    adaugarePos(head,last,4,0);
    parcurgere(head);

    cout<<"Stergem primul element"<<endl;
    stergereInceput(head);
    parcurgere(head);


    cout<<"Stergem ultimul element"<<endl;
    stergereFinal(head,last);
    parcurgere(head);

    cout<<"stergem elementul de pe pozitia 3"<<endl;
    stergerePos(head,last,3);
    parcurgere(head);

    cout<<"stergem prima aparitie a elementului cu valoarea 40"<<endl;
    stergeAparitie(head,40);
    parcurgere(head);

    cout<<"cauatam elementul cu valoarea 100"<<endl;
    cout<<cautare(head,100)<<endl;
    return 0;
}

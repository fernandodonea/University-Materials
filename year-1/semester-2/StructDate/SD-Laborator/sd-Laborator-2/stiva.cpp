#include <iostream>
using namespace std;

struct node{
    int info;
    node *next;
};

void push(node* &head, int x)
{
    node *p=new node;
    p->info=x;
    p->next=NULL;
    if(head==NULL)
        head=p;
    else
    {
        p->next=head;
        head=p;
    }
}

void pop(node* &head)
{
    node* p=head;
    head=p->next;
    delete p;

}


int main()
{
    cout << "Hello, World!" << endl;
    return 0;
}
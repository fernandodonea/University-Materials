#include <iostream>
using namespace std;

struct Node
{
    int info;
    Node* next;
};

void push(Node* &head, int x)
{
    Node *p=new Node;
    p->info=x;
    p->next=NULL;

    if(head==NULL)
    {
        head=p;
    }
    else
    {
        p->next=head;
        head=p;
    }
}

void pop(Node* &head)
{
    Node *temp=head;
    head=head->next;
    delete temp;
}

bool isEmpty(Node* head)
{
    if(head==NULL)
        return true;
    else return false;
}

int main()
{
    Node* stiva=NULL;

    push(stiva,6);
    push(stiva,2);
    push(stiva,3);
    while(isEmpty(stiva)==false)
    {
        cout<<stiva->info;
        pop(stiva);
    }
    return 0;
}
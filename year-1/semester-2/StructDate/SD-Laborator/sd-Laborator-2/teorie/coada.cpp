#include<iostream>
using namespace std;
struct Node
{
    int info;
    Node *next;
};

void push(Node* &head, Node* &last, int x)
{
    Node *p=new Node;
    p->info=x;
    p->next=NULL;
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
}
void pop(Node* &head, Node* &last)
{
    Node *temp=head;
    head=head->next;
    delete temp;
}

bool isEmpty(Node *head)
{
    if(head==NULL)
        return true;
    else return false;
}
int main()
{
    Node* head=NULL;
    Node* last=NULL;

    push(head,last,6);
    push(head,last,2);
    push(head,last,3);
    while(isEmpty(head)==false)
    {
        cout<<head->info;
        pop(head,last);
    }
    return 0;

}
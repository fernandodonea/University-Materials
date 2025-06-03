/*
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
*/


#include <iostream>
using namespace std;

struct node{
    char info;
    node *next;
};

void push(node* &head, char x)
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

bool isEmpty(node* head)
{
    if(head==NULL)
        return true;
    return false;
}


int main()
{
    cout << "Hello, World!" << endl;
    return 0;
}


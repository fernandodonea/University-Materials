#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


struct node
{
    string info;
    node* next;
};

void push(node* &head, string val)
{

    node* p=new node;
    p->info=val;
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
string top(node * head)
{
    return head->info;
}

void pop(node* &head)
{
    if(head!=NULL)
    {
        //daca suntem in root nu dam pop
        if(top(head)!="/")
        {
            node *temp=head;
            head=head->next;
            delete temp;
        }
    }
}


int main() 
{
    node* head=NULL;
    //by default ne aflam in root
    push(head,"/");
    int n;

    cin>>n;
    for(int i=1;i<=n;i++)
    {
        string opt;
        cin>>opt;
        if(opt=="cd")
        {
            string director;
            cin>>director;
            if(director=="..")
                pop(head);
            else
            {
                push(head,director);
            }
        }
        else if(opt=="pwd")
        {
            cout<<top(head)<<endl;
        }
    }

    return 0;
}

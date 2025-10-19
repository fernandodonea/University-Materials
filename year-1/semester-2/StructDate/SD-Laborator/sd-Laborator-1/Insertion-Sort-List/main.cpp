#include <iostream>
using namespace std;

 struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
 };




//solutia propriu zisa
ListNode* insertionSortList(ListNode* head)
{

    ListNode* sort=NULL;

    while(head!=NULL)
    {
        ListNode* p=new ListNode;
        p->val=head->val;
        p->next=NULL;

        //lista initiala este vida
        if(sort==NULL)
        {
            sort=p;
        }
        else
        {
            //daca nodul curent este mai mic decat primul adaugam la inceput
            if(p->val<sort->val)
            {
                p->next=sort;
                sort=p;
            }
            //altfel incepem sa parcurgem lista
            else
            {
                ListNode *i=sort;
                while(i!=NULL && i->next!=NULL)
                {
                    if(i->next->val <p->val)
                        i=i->next;
                    else break;
                }
                
                p->next=i->next;
                i->next=p;
            }
        }
        head=head->next;
    }
    return sort;
    

 }






//functii pentru testare 
void adaugare(ListNode* &head, int x)
{
    ListNode* p=new ListNode;
    p->val=x;
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
void parcurgere(ListNode* head)
{
    ListNode* p=head;
    while(p!=NULL)
    {
        cout<<p->val<<" ";
        p=p->next;
    }
    cout<<endl;
}


int main()
{
    ListNode* head=NULL;

    adaugare(head,3);
    adaugare(head,1);
    adaugare(head,2);
    adaugare(head,4);

    insertionSortList(head);


}
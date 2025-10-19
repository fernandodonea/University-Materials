#include <iostream>
using namespace std;


struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
};

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




ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) 
{
     ListNode* sum=NULL;
     ListNode* last=NULL;

     int carry=0;
     

     while(l1!=NULL && l2!=NULL)
     {
          ListNode *p=new ListNode;
          p->val=0;
          p->next=NULL;

          p->val=(l1->val+l2->val+carry)%10;
          carry=(l1->val+l2->val+carry)/10;

          if(sum==NULL)
          {
               sum=p;
               last=p;
          }
          else
          {
               last->next=p;
               last=p;
          }

          l1=l1->next;
          l2=l2->next;
     
     }
     //l1 are mai multe cifre
     while(l1!=NULL)
     {
          ListNode *p=new ListNode;
          p->val=0;
          p->next=NULL;

          p->val=(l1->val+carry)%10;
          carry=(l1->val+carry)/10;

          if(sum==NULL){
               sum=p;
               last=p;
          }
          else{
               last->next=p;
               last=p;
          }
          l1=l1->next;
     }
     //l2 are mai multe cifre
     while(l2!=NULL)
     {
          ListNode *p=new ListNode;
          p->val=0;
          p->next=NULL;

          p->val=(l2->val+carry)%10;
          carry=(l2->val+carry)/10;

          if(sum==NULL){
               sum=p;
               last=p;
          }
          else{
               last->next=p;
               last=p;
          }
          l2=l2->next;
     }
     if(carry>0)
     {
          ListNode *p=new ListNode;
          p->val=carry;
          p->next=NULL;

          if(sum==NULL){
               sum=p;
               last=p;
          }
          else{
               last->next=p;
               last=p;
          }
     }
     return sum;
        
     
}





int main()
{
    ListNode* l1=NULL;

    adaugare(l1,0);


     parcurgere(l1);


     ListNode* l2=NULL;

    adaugare(l2,0);


    parcurgere(l2);
    
    addTwoNumbers(l1,l2);

    


}

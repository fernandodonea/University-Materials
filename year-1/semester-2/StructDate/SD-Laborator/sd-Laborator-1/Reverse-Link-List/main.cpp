#include <iostream>
using namespace std;


struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    void adaugaInceput(ListNode* &head, int x)
    {
        ListNode *p=new ListNode;
        p->next=NULL;
        p->val=x;

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
    ListNode* reverseList(ListNode* head) {
        ListNode* rez=NULL;

        while(head!=NULL)
        {
            adaugaInceput(rez,head->val);
            head=head->next;
        }

        return rez;
        
    }
};
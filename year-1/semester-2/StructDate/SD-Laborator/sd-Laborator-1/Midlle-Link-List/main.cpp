#include <iostream>
using namespace std;

struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
};



/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */


class Solution {
public:
    ListNode* middleNode(ListNode* head) {

        int n=0;
        ListNode* p=head;
        while(p!=NULL)
        {
            n++;
            p=p->next;
        }

        int target=n/2+1;
        int ct=0;
        p=head;
        while(p!=NULL)
        {
            ct++;
            if(ct==target)
                return p;
            else p=p->next;
        }
        return NULL;
        



        
    }
};
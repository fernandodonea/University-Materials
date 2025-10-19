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
    ListNode* deleteMiddle(ListNode* head) {
        ListNode* p=head;
        int n=0;
        while(p!=nullptr)
        {
            ++n;
            p=p->next;
        }
        int target=n/2;
        if(n==1)
            return nullptr;

        p=head;
        int ct=0;
        while(p!=nullptr)
        {
            //am ajuns inaintea nodului din mijloc
            if(ct==target-1)
            {
                //nodul din mijloc
                ListNode* temp=p->next;
                p->next=p->next->next;
                delete temp;
                break;
            }
            p=p->next;
            ct++;
        }
        return head;

        
        
    }
};

int main()
{
    return 0;
}
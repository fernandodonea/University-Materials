
[link](https://leetcode.com/problems/range-sum-of-bst/description/)

# Range Sum of BST

## cerinta
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

##Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

# #Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
 

## Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.

# solutie 1

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void inordine(TreeNode* root, int low, int high, int &s)
    {
        if(root!=NULL)
        {
            inordine(root->left,low,high,s);
            if(root->val>=low && root->val<=high)
                s+=root->val;
            inordine(root->right,low,high,s);
        }
    }
    int rangeSumBST(TreeNode* root, int low, int high) {
        int s=0;
        inordine(root,low,high,s);
        return s;
       
    }
};
```

# soltutie 2
fara functii auxiliare
```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) 
    {
        if(root==NULL)return 0;
        else
        {
            if(root->val>=low && root->val<=high)
                return root->val+rangeSumBST(root->left,low,high)+rangeSumBST(root->right,low,high);
            else
                return rangeSumBST(root->left,low,high)+rangeSumBST(root->right,low,high);
        }

        
    }
};
```
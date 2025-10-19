[link leetcode](https://leetcode.com/problems/binary-tree-preorder-traversal/description/)

# Binary Tree Preorder Traversal

## cerinta

Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

## Example 1:

Input: root = [1,null,2,3]

Output: [1,2,3]





## Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [1,2,4,5,6,7,3,8,9]



## Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]

 

## Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?


# solutie
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
    void preordine(TreeNode* root, vector<int> &rez)
    {
        if(root!=NULL)
        {
            rez.push_back(root->val);
            preordine(root->left,rez);
            preordine(root->right,rez);
        }
    }
    vector<int> preorderTraversal(TreeNode* root) 
    {
        vector<int> rez;
        preordine(root,rez);
        return rez;
    
    }
};
```
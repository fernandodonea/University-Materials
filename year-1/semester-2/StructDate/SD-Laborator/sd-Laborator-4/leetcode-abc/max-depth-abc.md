[link leetcode](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)

# Maximum Depth of Binary Tree

## cerinta
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

## Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

## Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

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
    void parcurgere(TreeNode* root, int h, int &sol)
    {
        if(root!=NULL)
        {
            sol=max(sol,h);
            parcurgere(root->right,h+1,sol);
            parcurgere(root->left,h+1,sol);

        }
    }
    int maxDepth(TreeNode* root) {
        int sol=0;
        parcurgere(root,1,sol);
        return sol;
        
    }
};
```
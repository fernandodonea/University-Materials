[link leetcode](https://leetcode.com/problems/insert-into-a-binary-search-tree/description/)

# Insert into a Binary Search Tree

## cerinta
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 

## Example 1:


Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

## Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
## Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
 

## Constraints:

The number of nodes in the tree will be in the range [0, 104].
-108 <= Node.val <= 108
All the values Node.val are unique.
-108 <= val <= 108
It's guaranteed that val does not exist in the original BST.

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
    void inserare(TreeNode* &root, int val)
    {
        if(root==NULL)
        {
            root=new TreeNode;
            root->val=val;
            root->right=NULL;
            root->left=NULL;
        }
        else
        {
            if(val<root->val)
                inserare(root->left,val);
            else inserare(root->right,val);
        }

    }
    TreeNode* insertIntoBST(TreeNode* root, int val) 
    {
        inserare(root,val);
        return root;

        
    }
};
```
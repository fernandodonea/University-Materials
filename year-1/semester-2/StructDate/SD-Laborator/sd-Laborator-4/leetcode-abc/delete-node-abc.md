[link leetcode](https://leetcode.com/problems/delete-node-in-a-bst/description/)

# Delete Node in a BST

## cerinta
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

## Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

## Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
 

## Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
 

Follow up: Could you solve it with time complexity O(height of tree)?

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
    TreeNode *succesor(TreeNode* root)
    {
        //mergem o data in dreapta iar apoi maxim stanga

        root=root->right;
        while(root->left!=NULL)
        {
            root=root->left;
        }

        return root;
    }
    void sterge(TreeNode* &root, int key)
    {
        if(root!=NULL)
        {
            if(root->val==key)
            {
                //cazul 1 este frunza
                if(root->right==NULL && root->left==NULL)
                {
                    root=NULL;
                }
                else
                {
                    //cazul 2: are unul dintre fii
                    //are fiu drept
                    if(root->right!=NULL && root->left==NULL)
                    {
                        TreeNode* temp=root->right;
                        delete root;
                        root=temp;
                    }
                    //are fiu stanga
                    else if(root->right==NULL && root->left!=NULL)
                    {
                        TreeNode* temp=root->left;
                        delete root;
                        root=temp;
                    }
                    //are ambii fii
                    else
                    {
                        TreeNode* s=succesor(root);
                        swap(root->val,s->val);
                        sterge(root->right,s->val);
                    }
                }

            }
            else if(key<root->val)
                sterge(root->left,key);
            else sterge(root->right,key);
        }
    }
    TreeNode* deleteNode(TreeNode* root, int key) 
    {
        sterge(root,key);
        return root;
        
    }
};
```
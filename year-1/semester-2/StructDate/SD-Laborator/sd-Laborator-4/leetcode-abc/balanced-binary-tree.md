[link leetcode](https://leetcode.com/problems/balanced-binary-tree/description/)


# arbore binar balansat
un arbore binar este balansat daca pentru fiecare nod, adancimea subarborelui stang si adancimea subarborelui drept difera cu cel mult 1.

# Balanced Binary Tree

## cerinta 
Given a binary tree, determine if it is height-balanced.

 

## Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
# Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
# Example 3:

Input: root = []
Output: true
 

# Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

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
    int adancime(TreeNode* root)
    {
        if(root==NULL)
        {
            return 0;
        }
        else
        {
            return 1+max(adancime(root->left),adancime(root->right));
        }
    }
    bool isBalanced(TreeNode* root)
    {
        if(root==NULL)
            return true;
        else
        {
            int st=adancime(root->left);
            int dr=adancime(root->right);
            cout<<root->val<<":"<<st<<" "<<dr<<endl;
            if(abs(st-dr)<=1)
            {
                return isBalanced(root->left) && isBalanced(root->right);
            }
            else 
            {
                return false;
            }
        }
    }

};
```
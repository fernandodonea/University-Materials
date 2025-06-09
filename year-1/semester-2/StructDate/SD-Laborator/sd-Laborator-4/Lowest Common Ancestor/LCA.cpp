#include <iostream>
using namespace std;
struct ABC
{
    int info;
    ABC* left;
    ABC* right;
};
ABC* LCA(ABC* root, int n1, int n2)
{
    if (root == nullptr)
        return nullptr;

    if (root->info == n1 || root->info == n2)
        return root;

    ABC* left_lca = LCA(root->left, n1, n2);
    ABC* right_lca = LCA(root->right, n1, n2);

    if (left_lca && right_lca)
        return root;

    return (left_lca != nullptr) ? left_lca : right_lca;
}

int main()
{

}
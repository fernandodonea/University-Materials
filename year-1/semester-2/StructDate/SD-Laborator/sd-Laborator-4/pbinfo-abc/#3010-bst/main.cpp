#include <iostream>
#include <fstream>
using namespace std;
ifstream fin("bst.in");
ofstream fout("bst.out");


struct ABC
{
    int info;
    ABC* left;
    ABC* right;
};

void inserare(ABC* &root, int x)
{
    if(root==NULL)
    {
        root=new ABC;
        root->info=x;
        root->left=NULL;
        root->right=NULL;
    }
    else
    {
        if(x<root->info)
            inserare(root->left,x);
        else inserare(root->right,x);
    }
}

void inordine(ABC* root)
{
    if(root!=NULL)
    {
        inordine(root->left);
        fout<<root->info<<" ";
        inordine(root->right);
    }
}
int main()
{
    ABC* root=NULL;
    int n;
    fin>>n;
    for(int i=1;i<=n;i++)
    {
        int x;
        fin>>x;
        inserare(root,x);
    }
    inordine(root);

}





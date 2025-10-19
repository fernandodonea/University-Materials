#include <iostream>
using namespace std;




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
        cout<<root->info<<" ";
        inordine(root->right);
    }
}


bool cautare(ABC* root, int x)
{
    if(root!=NULL)
    {
        if(root->info==x)
            return true;
        else
        {
            if(x<root->info)
            {
                return cautare(root->left,x);
            }
            else return cautare(root->right,x);
        }
    }
    else return false;
}


ABC *succesor(ABC* root)
{
    //mergem o data in dreapta iar apoi maxim stanga

    root=root->right;
    while(root->left!=NULL)
    {
        root=root->left;
    }

    return root;
}

void stergere(ABC* &root, int x)
{
    if(root!=NULL)
    {
        if(root->info==x)
        {
            //cazul 1: nodul este frunza
            if(root->left==NULL && root->right==NULL)
            {
                root=NULL;
            }
            else
            {
                //cazul 2 are doi fii

                //are doar fiu stang
                if(root->left!=NULL && root->right==NULL)
                {
                    ABC* temp=root->left;
                    delete root;
                    root=temp;
                }
                //are doar fiu drept
                else if(root->right!=NULL && root->left==NULL)
                {
                    ABC* temp=root->right;
                    delete root;
                    root=temp;
                }
                //are ambii fii
                else
                {
                    ABC* s=succesor(root);
                    swap(root->info,s->info);
                    stergere(root->right, s->info);
                }

            }

        }
        else if(x<root->info)
            stergere(root->left,x);
        else stergere(root->right,x);
    }
}





int main()
{
    ABC* root=NULL;
    inserare(root,4);
    inserare(root,3);
    inserare(root,23);
    inserare(root,1);
    inserare(root,100);
    inordine(root);
    cout<<cautare(root,7)<<endl;
    cout<<cautare(root,23)<<endl;
    stergere(root,23);
    inordine(root);

}

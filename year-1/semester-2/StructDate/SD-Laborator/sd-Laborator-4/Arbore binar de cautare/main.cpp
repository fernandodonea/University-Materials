#include <iostream>
using namespace std;

struct ABC
{
    int info;
    ABC* left;
    ABC* right;
};

void inserare(ABC* &root, int val)
{
    if(root==NULL)
    {
        root=new ABC;

        root->info=val;
        root->left=NULL;
        root->right=NULL;
    }
    else
    {
        if(val<root->info)
        {
            inserare(root->left,val);
        }
        else
        {
            inserare(root->right,val);
        }
    }
}

//nu modificam nimic deci nu trimitem referinte
void inordine(ABC *root)
{
    if(root!=NULL)
    {
        inordine(root->left);
        cout<<root->info<<" ";
        inordine(root->right);
    }
}

bool cautare(ABC *root,int val)
{
    if(root!=NULL)
    {
        if(root->info==val) return true;
        else
        {
            if(val < root->info)
                return cautare(root->left,val);
            else
                return cautare(root->right,val);
        }
    }
    else return false;
}
ABC *succesor(ABC* root)
{
    //succesor = cel mai mic nod mai mare decat rood
    //mergem o singura data in dreapta iar apoi maxim stanga


    root=root->right;
    while(root->left!=NULL)
    {
        root=root->left;
    }
    return root;
}

void stergere(ABC* &root, int val)
{
    if(root!=NULL)
    {
        if(root->info==val)
        {
            //nodul este frunza
            if(root->left==NULL && root->right==NULL){
                root=NULL;
            }
            else
            {
                //nodul are un singur fiu
                if(root->right!=NULL && root->left==NULL)//are doar fiu drept
                {
                    ABC *temp=root->right;
                    delete root;
                    root=temp;
                }
                else if (root->left!=NULL && root->right==NULL)//are doar fiu stang
                {
                    ABC *temp=root->left;
                    delete root;
                    root=temp;
                }
                else //are ambii fii
                {
                    ABC *s=succesor(root);
                    swap(root->info, s->info);
                    stergere(root->right,s->info);
                }
            }
        }
        else if(val<root->info)
            stergere(root->left,val);
        else 
            stergere(root->right,val);
    }
   
}

int main()
{
    ABC* root = NULL;

    inserare(root,3);
    inserare(root,7);
    inserare(root,4);
    inserare(root,2);
    inserare(root,10);


    stergere(root,3);

    inordine(root);


    return 0;
}
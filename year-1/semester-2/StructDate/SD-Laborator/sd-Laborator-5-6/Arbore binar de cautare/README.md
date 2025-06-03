# Laborator 5-6
21 mai 2025

## Arbori binari de cautare
## Strucura
```c++
struct ABC
{
    int info;
    ABC* left;
    ABC* right;
};
```


### Inserari
inseram 5
```
               (5)              <-root
               /   \
           (NULL) (NULL)
```
inseram 7
```
               (5)               <-root
               /   \
           (NULL) (7)            <-nod
                  / \
                (NULL) (NULL) 
```
inseram 6
```
               (5)                  <-root
               /   \
           (NULL) (7)
                  / \
                (6) (NULL)      <-nod
                / \
              (NULL) (NULL) 
```
inseram 4
```
                  (5)                  <-root
               /       \
nod->      (4)           (7)
           / \           / \
        (NULL)(NULL)  (6) (NULL)    
```

```c++
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
```
## Afisare
Pt ordine crescatoare, parcurgem arborele in inordine (coboram in stanga)
```c++
void inordine(ABC *root)
{
    if(root!=NULL)
    {
        inordine(root->left);
        cout<<root->info<<" ";
        inordine(root->right);
    }
}
```
## Cautare
```c++
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
```


### Probleme leetcode
```https://leetcode.com/problems/range-sum-of-bst/```
```https://leetcode.com/problems/maximum-depth-of-binary-tree/```

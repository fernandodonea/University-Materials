[[sd_Curs-4.pdf#page=7|Referinta Curs]]

# Definitie

**Arbore binar de căuatre** = un arbore binar în care fiecare nod este 
- mai mare decât toate nodurile din subarborele stâng 
- mai mic decât toate nodurile din subarborele drept

# Declarare

```c++
struct ABC
{
	int info;
	ABC* left;
	ABC* right;
}
```


# Operații

## Cautare

[[sd_Curs-4.pdf#page=8|Exemplu cautare ABC]]

complexitate: 
- **O(n)** worst case
- **O(log n)**

Pornim din rădăcina și începm să comparăm cu valoarea căutată `x`:
	- dacă `x` este mai mic decât valoare nodului, coborâm în subarborele stâng
	- altfel, coborâm în subarborele drept

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

---
## Inserari

[[sd_Curs-4.pdf#page=9|Exemplu insertie ABC]]

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
---
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
---

## Succesor
[[sd_Curs-4.pdf#page=10|Succesor]]
#### *def:* 
cel mai mic număr mai mare decât `x`

#### Algoritm:
1. Dacă x are fiu drept, atunci succesorul va fi minimul din subarborele drept
2. Dacă nu are fiu drept, urcăm în arbore până când dăm de un nod `y` care ar fiu stâng care este fiu stâng al altui nod, fie el `z`.
atunci succesor(x)=z

#### Cod
```c++
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
```

--- 
## Stergere

[[sd_Curs-4.pdf#page=11|Exemplu stegere]]

```c++
  

void stergere(ABC* &root, int val)
{
	if(root!=NULL)
	{
		if(root->info==val)
		{
			//nodul este frunza
			if(root->left==NULL && root->right==NULL)
			{
				root=NULL;
			}
			else
			{
				//caz 1: nodul are un singur fiu
				//are doar fiu drept
				if(root->right!=NULL && root->left==NULL)
				{
					ABC *temp=root->right;
					delete root;
					root=temp;
				}
				//are doar fiu stang
				else if (root->left!=NULL && root->right==NULL)
				{
					ABC *temp=root->left;
					delete root;
					root=temp;
				}
				else //caz 2: are ambii fii
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
```

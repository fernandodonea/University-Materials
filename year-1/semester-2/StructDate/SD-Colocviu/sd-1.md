# S-1

## Cerinta 

Se da un arbore binar de cautare cu  valori distincte. Sa se determine diferenta maxima intre doua noduri din arbore. Se cere să implementați funcția test_case (a se vedea scheletul de program), ce primește un pointer catre radacina arborelui si returneaza diferenta maxima intre doua noduri din arbore.

ATENȚIE! Modificarea codului înaintea liniei // MODIFY START va face ca submisia voastră să fie respinsă.

[Schelet cod](https://drive.google.com/file/d/1Td5dNkcN6OHwTWWX7C6n6pE4mvWkpEYB/view?usp=sharing)

## Input Format

Inputul este citit automat de scheletul de cod dat.

## Constraints

1<=n<=1000

Valoarea maxima dintr-un nod este cel mult 10^5

Timp de rulare: 1 secunda.

Limita de memorie: 512Mb.

## Output Format

Nu trebuie afișat nimic la STDOUT

## Sample Input
```
5
12 13 1 17 15
``` 
## Sample Output
```
16
```

# cod
```c++
#include <iostream>

using namespace std;

struct ABC {
    int info;
    ABC* left;
    ABC* right;
};

void inserare(ABC* &root, int val) {
    if(root == NULL) {
        root = new ABC;
        root -> info = val;
        root -> left = NULL;
        root -> right = NULL;
    } else {
        if(val < root -> info) {
            inserare(root -> left, val);
        } else {
            inserare(root -> right, val);
        }
    }
}

int test_case(ABC* root);

int main() {
    int n;
    cin >> n;
    ABC* root = NULL;
    for(int i = 1; i <= n; i++) {
        int x;
        cin >> x;
        inserare(root, x);
    }
    int sol = test_case(root);
    cout << sol;
    return 0;
}

// MODIFY START

int test_case(ABC* root) {
    
    int maxim, minim;
    maxim=-1;
    minim=100001;
    
    ABC* p=root;
    while(p->left!=NULL)
    {
        p=p->left;
    }
    minim=p->info;
    
    ABC* q=root;
    while(q->right!=NULL)
    {
        q=q->right;
    }
    maxim=q->info;
    
    
    if(root==NULL)
        return 0;
    else return maxim-minim;
}
```
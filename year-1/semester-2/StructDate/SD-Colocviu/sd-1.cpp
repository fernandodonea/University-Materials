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



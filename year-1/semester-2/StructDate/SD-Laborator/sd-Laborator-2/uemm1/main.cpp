#include <iostream>
using namespace std;

struct Node {
    int index; // stocăm indexul în loc de valoare
    Node* next;
};

void push(Node* &head, int x) {
    Node* p = new Node;
    p->index = x;
    p->next = head;
    head = p;
}

void pop(Node* &head) {
    if (head != NULL) 
    {
        Node* temp = head;
        head = head->next;
        delete temp;
    }
}

bool isEmpty(Node* head) 
{
    return head == NULL;
}

int top(Node* head) 
{
    if (head != NULL) return head->index;
    return -1;
}

int main() {
    int n;
    cin >> n;
    int v[n], sol[n];

    for (int i = 0; i < n; ++i)
        cin >> v[i];

    Node* stiva = NULL;

    for (int i = n - 1; i >= 0; --i) {
        while (isEmpty(stiva)==false && v[top(stiva)] <= v[i]) 
        {
            pop(stiva);
        }

        if (isEmpty(stiva))
            sol[i] = -1;
        else
            sol[i] = v[top(stiva)];

        push(stiva, i);
    }

    for (int i = 0; i < n; ++i)
        cout << sol[i] << " ";

    return 0;
}

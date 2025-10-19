"""
Aranjamente de m din multimea {1,2,..,n}
1 2 3
2 3 1
3 2 1
1. Reprez solutiei
x=x_0,.., x_{m-1}
2) Fiecare element x_k poate lua valorile
x_k - 1,2..., n
3) Conditiile finale
elementele sa fie distincte x_i!=x_j
4) Conditiile de continuare la pasul k (!!) - cand ii dam valoare lui x_k
x_k!=x_0,...,x_{k-1}
"""
def continuare(k,x):
    for i in range(k): #x[k]in x[:k] x.index(x[k],0,k)...
        if x[i]==x[k]:
            return False
    return True

def back(k,x,n,m):
    if k == m: #daca am completat toate pozitiile si incerc sa completez x_m -> avem solutie
        #testam conditiile finale - doar in cazul in care cond de continuare nu au fost suficiente
        print(*x)
        #daca x retine indici din A(!!!de la 1 la n)
        for i in range(m):
            print(A[x[i]-1],end=" ")
        print()
    else:
        #luam la rand valorile posibile pentru x_k
        for i in range(1,n+1): #for i in A, daca x contine direct elemente din A
            x[k]=i
            if continuare(k,x):
                back(k+1,x,n,m)
def aranjamente(m,n):
    x=[0]*m
    back(0,x,n,m)
A=["s1","s2","s3","s4"]
aranjamente(3,4)

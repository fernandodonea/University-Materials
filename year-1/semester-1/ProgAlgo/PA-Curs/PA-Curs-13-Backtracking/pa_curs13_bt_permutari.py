"""
Permutarile multimii {1,2,..,n}
1. Reprez solutiei
x=x_0,.., x_{n-1}
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

def back(k,x,n):
    if k == n: #daca am completat toate pozitiile si incerc sa completez x_n -> avem solutie
        #testam conditiile finale - doar in cazul in care cond de continuare nu au fost suficiente
        print(*x)
    else:
        #luam la rand valorile posibile pentru x_k
        for i in range(1,n+1):
            x[k]=i
            if continuare(k,x):
                back(k+1,x,n)
def permutari(n):
    x=[0]*n
    back(0,x,n)
permutari(3)

def permutari_nerecursiv(n):
    x=[0]*n
    k=0
    while k>=0: #cand k devine -1 => stop
        if k==n:
            print(*x,sep=",")
            k-=1
        else: #dam lui x[k] urmatarea valoare posibila, daca mai sunt valori
            if x[k]<n:
                x[k]=x[k]+1
                if continuare(k,x):
                    k+=1
            else:
                x[k]=0
                k-=1
permutari_nerecursiv(3)


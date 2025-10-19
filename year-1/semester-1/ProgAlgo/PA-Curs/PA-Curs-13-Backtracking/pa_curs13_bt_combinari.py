"""
Combinari  de m din multimea {1,2,..,n}
1 2 3 = 2 3 1 = 3 2 1 -> o generam doar pe cea ord crescator
1. Reprez solutiei
x=x_0,.., x_{m-1}
2) Fiecare element x_k poate lua valorile
x_k - 1,2..., n
3) Conditiile finale
elementele sa fie distincte x_i!=x_j +Crescator
4) Conditiile de continuare la pasul k (!!) - cand ii dam valoare lui x_k
x_k>x[k-1] (Deci x_k este diferit de x_0,..,x_{k-1}
"""
def continuare(k,x):
     return k==0 or x[k]>x[k-1]

def back(k,x,n,m):
    if k == m: #daca am completat toate pozitiile si incerc sa completez x_m -> avem solutie
        #testam conditiile finale - doar in cazul in care cond de continuare nu au fost suficiente
        print(*x)


    else:
        #luam la rand valorile posibile pentru x_k
        for i in range(1 if k==0 else x[k-1]+1,n+1):
        #for i in range(1,n+1):
            x[k]=i
            #if continuare(k,x):
            back(k+1,x,n,m)
def combinari(m,n):
    x=[0]*m
    back(0,x,n,m)

combinari(3,4)

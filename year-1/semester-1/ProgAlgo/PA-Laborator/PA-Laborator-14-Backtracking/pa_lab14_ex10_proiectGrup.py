'''

Un grup format din n persoane (notate P1,P2,...,Pn ) dorește să se organizeze în
echipe pentru un proiect. Fiecare echipă trebuie să aibă un număr impar de membri, iar
ordinea în care persoanele sunt selectate nu contează. Se cere să se genereze toate
combinațiile posibile de echipe care respectă regula de mai sus, și să fie afișate în ordine
lexicografică după persoanele din echipă.


intrare
5

{P1}, {P2}, {P3}, {P4}, {P5}, {P1, P2, P3}, {P1, P2,
P4}, {P1, P2, P5}, {P1, P3, P4}, {P1, P3, P5}, {P1,
P4, P5},{P2, P3, P4}, {P2, P3, P5}, {P2, P4, P5}, {P3,
P4, P5}, {P1, P2, P3, P4, P5}



ne gandim combinari
'''


n=int(input('n='))
x=[0]*(n+1)


def afis(p):
    print("{", end="")
    for i in range(1,p+1):
        print(f'P{x[i]}',end=" ")

    print("}", end="")

    print()

def solutie(k):
    return k==p

def ok(k):
    for i in range(1,k):
        if x[i]==x[k]:
            return False
    if x[k]<x[k-1]:
        return False
    return True



def bkt(k):
    for i in range(1,n+1):
        x[k]=i
        if ok(k):
            if solutie(k):
                afis(p)
            else:
                bkt(k+1)
for p in range(1,n+1,2):
    x=[0]*(n+1)
    bkt(1)



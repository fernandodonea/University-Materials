'''
Se dau n mulțimi (elementele fiecărei mulțimi se dau pe o linie, separate prin
spațiu). Să se afișeze elementele produsului cartezian al celor n mulțimi
Exemplu, pentru fișierul de intrare


1 4
2 6
10 11 12


se va afișa
1 2 10
1 2 11
1 2 12
1 6 10
1 6 11
1 6 12
4 2 10
4 2 11
4 2 12
4 6 10
4 6 11
4 6 12


{1,4} x {2,6} x {10,11,12}
 0 1     0 1     0   1  2
0 0 1
0 0 1
0 0 2



'''

n=int(input())
multimi=[]

for _ in range(n):
    multime=[int(x) for x in input().split()]
    multimi.append(multime)
print(multimi)


x=[0]*n

def solutie(k):
    return k==(n-1)

def afis():
    for i in range(n):
        print(multimi[i][x[i]],end=" ")
    print()


def bkt(k):
    for i in range(len(multimi[k])):
        x[k]=i
        if solutie(k):
            afis()
        else:
            bkt(k+1)
bkt(0)
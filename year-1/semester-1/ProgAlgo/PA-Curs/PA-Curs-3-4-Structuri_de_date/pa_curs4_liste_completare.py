#COPIERE
#copiere
l=[7,8]
l1=l #nume pentru aceeasi lista
l1[0]=9
print(l1,l)
l1=l.copy()
l1[0]=11
print(l1,l)
m=[[1,2],[4,5]]
m1=m.copy() #copiere superficiala -doar de referinta
m1[0][0]=13
print(m1)
print(m)
import copy
m2=copy.deepcopy(m)
m[0][0]=100
print(m)
print(m2)

#EXP - citrea unei matrice cu elementele de pe o linie date
#separate cu spatiu; dimenisiunile matricei - date separate
# cu spatiu pe olinie
"""
2 3
1 4 6
3 67 10
"""
#Matrice -lista de liste
#un element al listei - o linie
n,m=[int(x) for x in input("dati dimensiunile ").split()]
"""
a=[]
for i in range(n):
    linie=[int(x) for x in input().split()]
    a.append(linie)
"""
#citirea matrice - cu comprehension
a=[[int(x) for x in input().split()] for i in range(n)]

print(a)
for linie in a:
    for x in linie:
        print(x, end=" ")
    print()
#stil c++
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()
#inint cu 0 -in alt fisier






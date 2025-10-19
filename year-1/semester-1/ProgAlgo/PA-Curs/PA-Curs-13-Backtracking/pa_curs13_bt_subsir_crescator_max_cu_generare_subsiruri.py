#v=[5,3,7,8,6,10]
v=[8,3,1,4,6,5,11]
n=len(v)
lung=[1]*n
succ=[-1]*n #[None]*n



lung[n-1]=1 #stim direct
#ord de calcul - de la ultimul catre primul
for i in range(n-2,-1,-1):
    lmax=0
    for j in range(i+1,n):
        if v[i]<v[j] and lung[j]>lmax:
            lmax=lung[j]
            succ[i]=j
    lung[i]=1+lmax

print(*lung)
print(*succ)

pmax=0
for i in range(n):
    if lung[i]>lung[pmax]:
        pmax=i
print("lungimea maxima ",lung[pmax])

p=pmax
for i in range(lung[pmax]):
    print(v[p],end=" ")
    p=succ[p]

#numaram cate subisruri optime exista
print(lung)

nr=[0]*n
nr[n-1]=1
for i in range(n-2,-1,-1):
    for j in range(i+1,n):
        if v[i]<v[j] and lung[j]==lung[i]-1:
            nr[i]+=nr[j]
    if nr[i]==0:
        nr[i]=1
print(nr)
nr_optim=0
for i in range(n):
    if lung[i]==lung[pmax]:
        nr_optim+=nr[i]
print(nr_optim)

"""
Toate subsirurile crescatoare de lungime maxima
1) repr sol:
x=(x0,..., x_{lung-1}) - indicii elementelor din subsir
2)
x0 - tb lung[x0]=lmax
x1: x0<x1 (dupa x0), v[x0]<v[x1] (subsir crescator) si lung[x1]=lung[x0]-1
analog pt xk
"""
lmax=lung[pmax]
def back(k):
    if k==lmax:
        for i in x:
            print(v[i],end=" ")
        print()
    else:
        for j in range(x[k-1]+1,n): #toate pozitiile de dupa x[k-1]
            x[k]=j
            if v[x[k-1]]<v[x[k]] and lung[x[k]]==lung[x[k-1]]-1:
                back(k+1)
#pentru primul element - dam valori separat
x=[0]*lmax
for i in range(len(v)):
    if lung[i]==lmax:
        x[0]=i
        back(1)


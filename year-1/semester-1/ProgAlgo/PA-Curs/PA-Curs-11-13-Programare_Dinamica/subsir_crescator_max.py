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



S=12
S=19
v=[1,6,7]
inf=S+1
nr=[inf]*(S+1) #daca nu se poate descompune -> inf =S+1
nr[0]=0
desc=[inf]*(S+1)
for s in range(1,S+1):
    if s in v:
        nr[s]=1
        desc[s]=s
    else:
        nrmin=inf
        for moneda in v:
            if moneda<=s and nr[s-moneda]<nrmin:
                nrmin=nr[s-moneda]
                desc[s]=moneda
        if nrmin<inf:
            nr[s]=1+nrmin
print(nr)
print(desc)
if nr[S]==inf:
    print("nu se poate plati suma")
else:
    s=S
    while s!=0:
        print(desc[s],end=" ")
        s=s-desc[s]

def descompune(s):

    if nr[s] is not None:
        return nr[s]
    if s==0:
        nr[0]=0
        return 0
    nrmin = inf
    for moneda in v:
        if moneda <= s and  descompune(s - moneda)< nrmin: #ar fi mers memorat descompune(s - moneda) in variabia
            nrmin = descompune(s - moneda)
    if nrmin<inf:
        nr[s]=1+nrmin
    else:
        nr[s]=inf
    return nr[s]

S=19
nr=[None]*(S+1)
print()
print(descompune(S))





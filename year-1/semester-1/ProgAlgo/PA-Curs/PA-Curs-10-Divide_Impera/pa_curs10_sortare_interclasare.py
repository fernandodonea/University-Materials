def interclasare(v,p,m,u): #v[p...m] se interclaseaza cu v[m+1...u]
    b=[0]*(u-p+1)
    i=p
    j=m+1
    k=0
    while i<=m and j<=u:
        if v[i]>v[j]:
            b[k]=v[j]
            j+=1
            k += 1
        else:
            b[k] = v[i]
            i += 1
            k += 1

    while i <= m:
        b[k] = v[i]
        i += 1
        k += 1
    while j<=u:
        b[k] = v[j]
        j += 1
        k+=1
    v[p:u+1]=b #for i in range(len(b)): v[i+p]=b[i]

def sort_inter(v,p,u): #supb- data prin indicii p si u, nu v[p:u+1]
    if p>=u:  #rezolvam direct
        return
    else:
        m=(p+u)//2
        sort_inter(v,p,m)
        sort_inter(v,m+1,u)
        interclasare(v,p,m,u)
def sortare_interclasare(v):
    sort_inter(v,0,len(v)-1)
v=[5,1,6,3,1,9,11,-4]
sortare_interclasare(v)
print(v)
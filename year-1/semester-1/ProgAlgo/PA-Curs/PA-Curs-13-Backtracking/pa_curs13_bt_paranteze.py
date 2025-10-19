def catalan(n):
    cat=[0]*(n+1)
    cat[0]=cat[1]=1
    cat[2]=2
    for j in range(3,n+1):
        for i in range(0,j):
            cat[j]+=cat[i]*cat[j-1-i]
    return cat[n]

def back(k,dif):
    global nr
    if k==2*n:
        print("".join(x))
        nr+=1
    else:
        #luam la rand valorile pentru x[k]:
        x[k]='('
        dif=dif+1
        if dif<=2*n-k:
            back(k+1,dif)
        dif-=1
        x[k]=')'
        dif-=1
        if dif>=0:
            back(k + 1, dif)
        dif+=1
n=4
x=[None for i in range(2*n)]
nr=0
back(0,0)
print(nr)
print(catalan(n))
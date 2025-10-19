"""
n=5
1+1+1+1+1
1+1+1+2
..
2+3 (= 3+2)
5
x=(x1,...,xp) (lungime variabila
cond continuare suma<=n
valori pt xk: 1...n  -+ crescator nestrict (pentru unicitate)

"""
def back(k,s,x,n):
    if s==n:
        print(*x[:k],sep="+")
    else:
        for i in range(1 if k==0 else x[k-1],n+1):
            x[k]=i
            s+=i
            if s<=n:
                back(k+1,s,x,n)
            s-=i
def partitie(n):
    x=[0]*n
    back(0,0,x,n)
partitie(6)

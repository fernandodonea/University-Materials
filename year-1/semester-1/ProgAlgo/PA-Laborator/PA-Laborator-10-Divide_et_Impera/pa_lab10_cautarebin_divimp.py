v=[2,11,15,22,36,43,57]
def cautarebinara(l,st,dr,x):
    if st>dr:
        return -1
    mij=(st+dr)//2
    if l[mij]==x:
        return mij
    if l[mij]<x:
        return cautarebinara(l,mij+1,dr,x)
    return cautarebinara(l,st,mij-1,x)

print(cautarebinara(v,0,len(v)-1,15))

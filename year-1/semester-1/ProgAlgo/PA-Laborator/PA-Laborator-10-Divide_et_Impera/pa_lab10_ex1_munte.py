'''
Se dă un vector a=(a1,…an) de tip munte (există un indice i astfel încât a1<a2<…<ai > ai+1>…>an;
ai se numește vârful muntelui). Propuneți un algoritm O(log n) care determină vârful muntelui (în
calculul complexității algoritmului nu se consideră și citirea vectorului).
'''

n=5
v=[4,8,10,11,5]
def gaseste_varf(l,st,dr):
    if st==dr:
        return l[st]
    mij=(st+dr)//2
    if l[mij]>l[mij+1] and l[mij]>l[mij-1]:
        return l[mij]
    if l[mij]<l[mij+1]:
        return gaseste_varf(l,mij+1,dr)
    return gaseste_varf(l,st,mij-1)

print(gaseste_varf(v,0,n-1))
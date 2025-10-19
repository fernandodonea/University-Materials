"""
Scrieți o funcție nr_aparitii cu complexitate O(log(n)) care primește ca parametru o listă de numere
întregi ordonată crescător și un număr x și returnează numărul de apariții ale unei valori x în listă.
De exemplu, nr_aparitii( [1, 1, 2, 2, 2, 2, 6, 9, 9, 20], 2) va returna 4
"""

v=[int(x) for x in input().split()]
x=int(input("x="))
def gasestePrimul(l,x):
    st=0
    dr=len(l)-1
    p=-1
    while st<=dr:
        mij=(st+dr)//2
        if l[mij]==x:
            p=mij
            dr=mij-1
        else:
            if l[mij]<x:
                st=mij+1
            else:
                dr=mij-1
    return p

def gasesteUltimul(l,x):
    st=0
    dr=len(l)-1
    p=-1
    while st<=dr:
        mij=(st+dr)//2
        if l[mij]==x:
            p=mij
            st=mij+1
        else:
            if x>l[mij]:
                st=mij+1
            else:
                dr=mij-1
    return p
a=gasestePrimul(v,x)
b=gasesteUltimul(v,x)

if a==-1 or b==-1:
    print("NU se afla in sir")
else:
    print(b-a+1)
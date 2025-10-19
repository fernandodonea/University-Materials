'''
2N*2N pe care se scriu numerele naturale de la 1 si 2N*2N prin vizitarea recursivă a celor patru
cadrane ale tablei în ordinea indicată și în figura alăturată: dreapta-sus, stânga-jos,
stânga-sus, dreapta-jos. De exemplu, daca N=2, tabla este completată astfel:
11 9 3 1
10 12 2 4
7 5 15 13
6 8 14 16

'''

x=int(input("n="))
def f(a,n,l,c,nr):
    if n==0:
        a[l][c]=nr
        return
    e=2**n//2
    #zona 1
    f(a,n-1,l,c+e,nr)
    #zona 2
    f(a,n-1,l+e,c,nr+e**2)
    #zona 3
    f(a,n-1,l,c,nr+2*e**2)
    #zona 4
    f(a,n-1,l+e,c+e,nr+3*e**2)
N=2
a=[[0]*2**N for _ in range(2**N)]
f(a,N,0,0,1)
for x in a:
    for y in x:
        print(y,end=" ")
    print()


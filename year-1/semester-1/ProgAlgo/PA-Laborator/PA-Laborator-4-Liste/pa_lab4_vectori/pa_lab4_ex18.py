'''
Ciurul lui Eratostene. Se dă un număr natural n. Să se creeze o listă cu numerele
prime mai mici sau egale cu n.
'''

def prim(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,n//2,2):
        if n%i==0:
            return False
    return True
n=int(input("n="))
l=[x for x in range(1,n+1) if prim(x)==True]
print(l)

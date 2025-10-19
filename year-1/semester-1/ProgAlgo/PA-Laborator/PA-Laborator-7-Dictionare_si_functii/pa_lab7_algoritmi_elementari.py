def salut():
    print("Buna dimineata")

def nrcif(a):
    if a<10:
        return 1
    else:
        return nrcif(a//10)+1


def ogl(a,o=0):
    if a==0:
        return o
    else:
        return ogl(a//10,o*10+a%10)
def cmmdc(a,b):
    if a==b:
        return a
    else:
        if a>b:
            return cmmdc(a-b,b)
        else:
            return cmmdc(a,b-a)
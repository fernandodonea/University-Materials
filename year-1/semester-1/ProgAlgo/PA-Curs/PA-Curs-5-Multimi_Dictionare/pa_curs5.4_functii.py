"""
FUNCTII

"""

def f(x,y): #antet, x,y- param formali
    if x>y:
        return x-y, x*y #putem returna mai multe valori => tuplu
    else:
        return y-x, x*y
    #daca nu returneaza explicit val, implicit returneaza None

def afis(x,y):
    print(x,y)

t=f(3,4)
print(t,type(t))
a,b= f(3,4)
print(a,b)
x=afis(a,b)
print(x) #None

v=[5,1,6]
ls=sorted(v)
print(ls)
ls=v.sort()
print(ls)
v=v.sort() #!!!NU - v devine None
print(v)

#transmiterea parametrilor - prin atribuire
# (param formal= parm actual (param formal - vairabila locala)
def modifica(x):
    x=x+1
    print(x)
    print(locals())
a=8
modifica(a)
print(a)
"""
x=8
modifica(x)
print(x)
"""

def modificare_lista(ls):
    ls.append(6)
v=[7,8]
modificare_lista(v)
print(v)
def creare(v):
    v=[0]*10
v=[]
creare(v)
print(v)
#dupa exec fct se vad doar modificarile facute asupra
# valorii unui param mutabil ("deja alocat")

a=[[2],[4,5],[10,7,3],[1,5,2,1],[8,4,5,6,7,11]]
a=[[2],[4,5],[10,7,3],[1,5,2,1]]

#varianta recursiva
def suma(i,j):
    global nr #numarul de apeluri recursive<=2*nr de elemente
    nr=nr+1
    if s[i][j] is not None: #daca este deja rezolvata-returnam valoarea, nu mai apelam recursiv
        return s[i][j]
    if i==n-1:
        s[i][j]=a[i][j]
        return a[i][j]
    s[i][j]=a[i][j]+max(suma(i+1,j), suma(i+1,j+1))
    return s[i][j]
    #return a[i][j]+max(suma(i+1,j), suma(i+1,j+1))-: exponential

def suma_nerec():
    s = [[None for j in range(i + 1)] for i in range(n)]
    #s[n-1][:]=a[n-1]
    for j in range(n):
        s[n-1][j]=a[n-1][j]
    for i in range(n-2, -1,-1):
        for j in range(i+1):
            s[i][j]=a[i][j]+max(s[i+1][j],s[i+1][j+1])
    print(s[0][0])
    print(s)

nr=0
n=len(a)
s=[[None for j in range(i+1)] for i in range(n)]
print(suma(0,0))
print(s)
print(nr,"apeluri")
suma_nerec()

def traseu(i,j):
    if i==n-1:
        print(i,j)
    else:
        print(i,j)
        if s[i][j]==a[i][j]+s[i+1][j]: #if s[i+1][j]>s[i+1][j+1]
            traseu(i+1,j)
        else:
            traseu(i+1,j+1)


traseu(0,0)

#Observatii:
#1. Putem afisa traseul si nerecursiv
#2. Putem folosi tot matricea a pentru a caclula suma, in loc de s


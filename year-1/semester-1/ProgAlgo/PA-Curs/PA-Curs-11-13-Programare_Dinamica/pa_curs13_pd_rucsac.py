f=open("rucsac.in")
g=[int(x) for x in f.readline().split()]
c=[int(x) for x in f.readline().split()]
G=int(f.readline())
f.close()
n=len(g)
g.insert(0,0) #obiectul 1 va fi pe pozitia 1
c.insert(0,0)
s=[[0 for i in range(G+1)] for j in range(n+1)]
#prima linie si prima coloana raman 0 (corespun 0 obiecte/greutate 0
for i in range(1,n+1):
    for gr in range(1, G+1):
        if g[i]>gr:
            s[i][gr]=s[i-1][gr] #nu putem lua obiectul i, are greutate prea amre
        else:
            s[i][gr] =max(s[i-1][gr], s[i-1][gr-g[i]]+c[i])
print(*s,sep="\n")
print(s[n][G])

#determinarea solutiei - de la coltul de jos inapoi
print("obiectele")
i=n
gr=G
while i>0 and gr >0:
    if s[i][gr]!=s[i-1][gr]: #luam obiectul i
        print(i)
        gr-=g[i]
        i-=1
    else:
        i-=1
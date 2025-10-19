"""
clasa list- vector (array)
elminarea rimului elelemnt -> O(n)

"""
ls=[1,"abc",[3,4]] #imbricate, pot fi neomogene
m=[[2,3],[5,6]]
#lista vida
ls=[]
ls=list()
#list(iterabil)->lista (cu fiecare element din iterabil)
ls=list(range(6))
print(ls)
ls=list("un cuvant") #sir elemnt=o litera
print(ls) #lista de litere

#Se pot initializa cu comprehensiune (list comprehension)
#Exc - o lista cu primele n patrate perfecte
n=5
ls=[]
for i in range(1,n+1):
    ls.append(i*i) #append - adauga un element la finalul listei
print(ls)

#ls=[expresie for element in iterabil]
ls1=[i*i for i in range(1,n+1)]
print(ls1)

##sa se creeze un vector cu n elemente egale cu 0
v=[0]*n
v[0]=1
print(v)
v=[]
for i in range(n):
    v.append(0)
v=[0 for i in range(n)]
v[0]=3
print(v)
#se se citeasca un vector de numere intregi cu elementele date pe o linie
#9 0 23 4 7
v=input().split()
print(v)
"""
for x in v:
    x=int(x) #nu se modifica v
print(v)
"""
for i in range(len(v)):
    v[i]=int(v[i])
print(v)

v=[int(x) for x in input().split() ]
print(v)

#citim 2 numere pe aceeasi linie
m,n=[int(x) for x in input("dati doua numere ").split() ]
print(m+n)

#Comprehensiune conditionata:
#[expresie for elem in iterabil if conditie]
#Exp: sa se creeze o lista cu elementele pozitive ale unei liste date
ls=[4,5,-1,7,3,-8,9]
ls_pozitiv=[]
for x in ls:
    if x>0:
        ls_pozitiv.append(x)
print(ls_pozitiv)
ls_pozitiv=[x for x in ls if x>0]
print(ls_pozitiv)

#exc: se dau doua liste reprezentand multimi
#sa se creeze o noua lista cu intersectia celor doua multimi
a=[3,1,5,7]
b=[1,7,2,9,11]
c=[x for x in a if x in b]
print(c)

##se da un cuvant, sa se stearga vocalele din cuvant => un nou cuvant
s="programarea"
ls=[lit for lit in s if lit.lower() not in "aeiou"]
print(ls)
s_consoane="".join(ls)
print(s_consoane)
"""
    for x in "aeiou"
        s=s.replace(x,"")
"""

#in comprehensiune expresie poate contine si operatorul if... else (?:)
#exp: Data o lista, sa se creeze o noua lista in care elementele negative
#din lista initiala sunt inlocuite cu 0
ls=[8,1,-5,7,-2,-3]
ls2=[x if x>0 else 0 for x in ls]
print(ls2)

#for in for
ls_perechi=[(x,y) for x in range(1,7) for y in range(1,7) if x%2==0 and y%2==0]
print(ls_perechi)

#EXp - cifrul lui Cezar pt k=1 si litere mici
s="abz" #=>bca
s_cezar="".join([chr(ord(lit)+1) if lit<'z' else 'a' for lit in s])
print(s_cezar)
"""
lit="c"
if lit<'z':
    lit=chr(ord(lit)+1)
else:
    lit='a'
"""

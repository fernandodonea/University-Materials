"""
Exp -> se citeste un sir de cifre
sa se afiseze frecventa fiecarei cifre in sir
"""
"""
v=[int(x) for x in input("dati sirul ").split()]
fr=[0]*10
for x in v:
    fr[x]+=1
for i in range(10):
    if fr[i]!=0:
        print(i,fr[i])
"""
"""
Exp -> se citeste o propozitie cu cuv separate prin spatiu 
sa se afiseze frecventa fiecarui cucvant din propozitie
un exemplu un alt exemplu
un 2
alt 1
exemplu 2
"""
#struct de date indexate dupa alt tip de cheie


d={} #frecv - alta structura - dictionar
p="un exemplu un alt exemplu"
for cuv in p.split():
    if cuv in d:
        d[cuv]+=1
    else:
        d[cuv]=1
for cuv in d:
    #if d[cuv]!=0: - nu este necesar
    print(cuv,d[cuv])
"""
Solutie de o(n^2) un de n=nr de cuvinte"""
l=p.split()
l_dist=set(l)
print(l_dist)
#l1=[(l[i],l.count(l[i])) for i in range(len(l)) if l.count(l[i])>0] - se repeta cuv
l1=[(cuv,l.count(cuv)) for cuv in l_dist ]
print(l1)
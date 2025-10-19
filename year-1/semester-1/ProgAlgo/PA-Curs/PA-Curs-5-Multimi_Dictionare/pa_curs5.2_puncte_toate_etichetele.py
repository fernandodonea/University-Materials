"""
Se dau informatii de despre puncte in plan
x y eticheta
(in fisierul puncte.in)
a) Sa se memoreze punctele cu etichete intr-un dictionar
b) se citesc coordonatele unui punct, sa se afiseze eticheta acestuia
c) se citesc coordonatele unui punct, sa se stearga informatiile asociate lui
"""
#a)var 3- se pastreaza ca eticheta toate etichetele
# (cea mai recenta)
f=open("puncte.in") #pt citire - implicit
d={}
for linie in f: #f este colectie de linii
    x,y,eticheta=linie.split(maxsplit=2)
    x=int(x)
    y=int(y)
    eticheta=eticheta.strip("\n")  #elimina \n de la capetele sirului pana gaseste alt caracter
    #p=[x,y] #TypeError: unhashable type: 'list'
    p=(x,y)

    if p not in d: #doar pt var 2
        d[p]=[eticheta] #!!!lista cu o eticheta
    else:
        d[p].append(eticheta)
    """
    if p not in d: #doar pt var 2
        d[p]=[] #!!!lista 
    d[p].append(eticheta)
    """
f.close()
print(d)
#b)
#p=(int(x) for x in input().split()) #nu este tuplu
a,b=(int(x) for x in input().split())
t=(a,b)
if t in d: #cauta t in cheile lui d
    print(d[t])
else:
    print("nu exista punctul ",t)
#alternativ, fara if- puteam folosi get
print(d.get(t,"nu exista"))


#stergere
if t in d:
    del d[t]
print(f"am sters {d.pop(t," nimic ")}")

#var 2 la citire - sa pastreze prima eticheta (alte etichete ale aceluiasi punct- ignora)

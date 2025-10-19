#cautarea
s="programarea"
print("a" in s)
print(s.count("a"))
print(s.count("a",6)) #numara incepand de la pozitia 5
print(s.count("a",6,10)) #numara incepand de la pozitia 5

#pozitii
p=s.index("a")
print(f"prima pozitie {p}")
p=s.index("a",p+1)
print(f"a doua pozitie {p}")

try:
    p=s.index("b") #eroare daca elementul nu este gasit
    print(f"prima pozitie {p}")
except ValueError:
    pass
print("ok")
#exc: sa se afiseze toate pozitiile pe care apare "a" in s
p=s.index("a")
try:
    while True:
        print(p)
        p=s.index("a",p+1)
except:
    pass

#doar pt siruri -find - returneaza -1 daca elementul nu este gasit
p=s.find("a")
while p!=-1:
    print(p)
    p=s.find("a",p+1)

#rfind, rindex - cauta de la dr la stg (ultima aparite) - doar pt siruri
p=s.rfind("a")
print(f"ultima pozitie {p}")

#concatenari => obiect nou
s=s[:3]+" "+s[5:]
print(s)
n=7
s="a"*n
print(s)
v=[0]*n
print(v)

#sorted -> returneaza lista
v=[9,4,6,7]
v_sortat=sorted(v)
print(v_sortat,v)
s="mare"
s_sortat=sorted(s)
print(s_sortat)
#---- siruri caractere - unificari/separari
#separator.join(ecventa de cuvinte)
ls=["programarea", "algoritmilor", "seria", "14"]
s=" ".join(ls)
print(ls)
print(s)
s="_".join(ls)
print(s)
cuv="".join(s_sortat)
print(cuv)

#sir.split(separator) -> lista de cuvinte
#daca nu se specifica separator - caractere albe
s="programrea algoritmilor    seria 14"
ls=s.split()
print(" ".join(ls))
print(ls)
ls=s.split(" ")
print(ls)
print(" ".join(ls))

#
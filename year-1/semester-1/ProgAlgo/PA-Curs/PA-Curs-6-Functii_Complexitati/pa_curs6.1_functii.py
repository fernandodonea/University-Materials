"""
Tipuri de paramterii
"""

"""
1. Param obligatorii - trebuie sa primeasca valaore la apel
Se pot da
-prin pozitie (in ordinea in care sunt in antet 
-prin nume (nume_param_formal=)
- combinat - dar primii se dau cei prin pozitii
"""
def f(x,y,z):
    print(x,y,z)
f(3,4,5)
f(z=7,x=9,y=8) #prin nume-in orice ordine
f(3,z=89,y=2)

"""
2. Param cu valoare implcita - atribuita in antet
Daca la apel nu ii coresp o valoare, este folosita cea implicita
la final in antet
"""
def f(x,y,z=9):
    print(x,y,z)
f(7,8) #pentru z se foloseste valoare implicita

"""
3. Functii cu numar variabil de parametrii:
- in antet unul dintre parametri este prefixat de *
*parametru 
"""

def f(*numere):
    print(numere, type(numere))
    l=list(numere)
    print(l, type(l))
f(1,2)
f(1,2,3)
f(1,2,3,4)

#!!!parametrii de dupa cel cu * trebuie dati prin nume

#exemplu - suma numerelor primite ca param, dintr-un interval dat
def suma(*numere, lim_inf,lim_sup):
    s=0
    for nr in numere:
        if lim_inf<=nr<=lim_sup:
            s+=nr
    s=sum(nr for nr in numere if lim_inf<=nr<=lim_sup)
    return s

s=suma(100,45,79,105, lim_inf=50, lim_sup=100) #cei de dupa- prin nume
print(s)

#parametrii de dupa * pot avea si valoare implicita
def suma(*numere, lim_inf=0,lim_sup=100):
    s = sum(nr for nr in numere if lim_inf <= nr <= lim_sup)
    return s
s=suma(100,45,79,105, lim_sup=50) #lim_inf- s-a cons valoarea default
print(s)

#putem transmite ca parametrii si functii
#exp: suma generica suma(f(x) pentru numerele x primite ca param
#si funtia f primita ca param
def suma(*numere, f=int):
    s=0
    for nr in numere:
        s+=f(nr)
    return s
def finvers(x):
    return 1/x
import math
r=suma(9,16,100, f=math.sqrt)
print(r)
r=suma(9,16,100, f=finvers)
print(r)
r=suma(9,16,100) #lipseste f la apel -implicit int
print(r)

#map(f,lista) -> f aplicat elementelor listei
ls=["70",8,"90"]
#v=[int(x) for x in ls]

v=map(int,ls) #aplica functia fiecarui element
v=list(v)
print(v)
"""
filter(criteriu,lista) -> 
doar elementele din lista care verifica criteriul
unde criteriu - functie care returneaza True/False
"""
#Exp:
ls=[8,12,7,9,10]
#lista cu elementele pare
lsp=[x for x in ls if x%2==0]
def f(x):
    return x%2==0
lsp=list(filter(f,ls))
print(lsp)

#sortari
ls=["cuv","un","altul","doi","cinci","ab"]
#sort lista de cuvinte crescator dupa lungime si in caz de egalitate
#crescator lexicografic
#OBS: sortarea din python este stabila =
#doua elemente egale dupa sortare pastreaza ordinea din sirul initial

#Avem 2 criterii de sortare 1)llung, 2)lexicogr:
#var1- folosim sort de 2 ori, pentru criteriile in ordine inversa:
#sortam lexicografic !!sortare stabila
ls.sort()
#sortam dupa lungime
ls.sort(key=len) #keycheia de sortare key(v[i])
print(ls)

#var 2
ls=["cuv","un","altul","doi","cinci","ab"]
def f(x): #elementele se compara dupa f(v[i])
    #returnam un tuplu, fiecare element din tuplu corespunde unui criteriu
    #primul elemnt din ltuplu - primul criteriu)
    return len(x),x

ls.sort(key=f)
print(ls)

#functii fara nume
ls=["cuv","un","altul","doi","cinci","ab"]
ls.sort(key= lambda x:(len(x),x)) #lambda x : cheie asociata lui x)
print(ls)



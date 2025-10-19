#dict -dictionar
"""
memoreaza perechi cheie:valoare ai cautarea dupa cheie O(1) mediu
(si stergerea cheii (impreuna cu valoarea asociata)
"""
#Creare
d={"un":2,"cuvant":1}
print(d,type(d))
d={} #!!!dictionar vid, nu set vid
#Obs: cheia - imutabila + cu hash
#valoarea poate fi de orice tip
#pot fi chei in dict /elemente in set: str, tuple, frozenset
#nu pot fi chei: list, set

#se poate crea dict/set cu comprehensiune
s="abcdab"
d={lit:0 for lit in s}
print(d)
d={lit:s.count(lit) for lit in s} #ineficient -o(n2) - v curs trecut
print(d)
#si set se poate crea cu comprehensiune (completare la set)
#sa se determine multima cuvintelor cu cel putin k litere dintr-o propozite:
prop="aceasta este o propozitie aceasta"
k=5
s={w for w in prop.split() if len(w)>=k}
print(s)

#accesarea unui element din dictionar - dupa cheie
#d[cheie]- returneaza valoarea asociata cheii/KeyError daca nu exista cheia in dictionar
d={"un":2,"cuvant":1}
print(d["un"])
#d.get(cheie,valoare_default)- daca nu gaseste cheia
# returneaza valoare_default
print(d.get("trei","nu exista"))

#ACTUALIZARE
#d[cheie]=valoare -> daca nu exista cheie in dict,se adauga cheie:valoare,
#daca exista cheie - se modifica valoarea asociata
d={"un":2,"cuvant":1}
d["un"]=5
d["unu"]=1
print(d)

#d.setdefault(cheie,valoare) - adauga daca nu exista in dictionar cheie
#perechea cheie:valoare

#stergerea unei cheii (a perechii cheie:valoare
#del d[cheie]
#d.pop(cheie,valoare_default)
#d.clear()





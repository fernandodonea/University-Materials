#Alte tipuri de colectii in Python
"""
Multmi, dictionare - sunt mmem cu tabele de dispersie
(tabele"de frcventa" indexate"" dupa chei care au asociate o valoare numerica (hash code)
Hash code depinde de valoarea obiectui => cheile pot fi doar de tipuri imutabile
(Care nu isi pot schimba valoarea))
"""
#cheie -> hash -> index in tabel
#t[index] - informatii despre toate cheile care au acelasi index
"""
ob cu aceeasi valoare => acelasi hash
ob cu valori difertite - poate avea acelasi hash (coliziuni)
Obs: Cautarea si stergrea in astfel de struct O(1) mediu (!!coliziuni)
"""

#MULTIMI
"""
Colectii de ob cu valori diferite
Nu sunt indexate de la 0 !!!!
elemntele din multime - tb sa fie imutabile+ sa aiba hash code
"""
s={6,1,3,1}
print(s) #ordine ain s- nu este garantata a fi cea de la adaugare/creare}
cuv="alfabet"
#multimea literelor din cuv
s=set(cuv)
print(s)
#s={[3,4],[5,6]} #unhashable type: 'list'
print(hash(cuv))

#operatii , incluziune
#op relationali - testeaza incluziunea < (stict inclus), <=
s1={3,1,5}
s2={1,5}
print(s2<s1) #s2 est inclus in s1 => adev
#op cu multimi - si operatori si metode
# (care modifica ob/returneaza rezultatul)
"""
reuniune:
operatorul |
metoda care returneaza mult obtinuta dupa reuniune: union
metoda care modifica ob: update
intersectie: & , intersection, intersection_update
"""
s1={4,5,6}
s2={6,7}
s3={5,11}
r=s1|s2|s3 #se pot inlantui
print(r)
r=s1.union(s2,s3,[7,34,78]) #metode- param pot sa fie si de alt tip decat set
print(r)
r.intersection_update({5,6,11,110}) #modifica r
print(r)
#multimea vida
#s={}#nu- dictionar
s=set()
#len, sorted,min, max
#NU s[i]

s={{1,3},{2,4,5}}
#set se poate modifica - add, remove, discard de un element
#->nu exista set de set-uri
#exista tipul de date frozenset
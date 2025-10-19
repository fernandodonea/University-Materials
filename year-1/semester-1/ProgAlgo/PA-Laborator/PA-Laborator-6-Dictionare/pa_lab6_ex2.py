#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 18:42:12 2025

@author: fernandodonea
"""

'''
În fișierul "elevi.in" sunt memorate informații despre elevii unei clase; astfel, pe o
linie a fișierului se dau următoarele informații despre un elev: cnp, nume (fără spații),
prenume (fără spații), lista de note, de exemplu:
2501910000034 Ionescu Ion 10 8 7 8
2402900000041 Marinica Maria 9 10 8 8 8
1412900000041 Petrescu Petrica 8 10 4 7

a) Memorați lista de elevi din fișier astfel încât să se poată răspundă cât mai eficient la
întrebări de tipul celor de la subpunctele următoare (dat cnp elev, care sunt numele, notele, să
se lista de note a elevului).

b) Scrieți o funcție care primește ca parametri un cnp și structura de date în care s-au
memorat datele despre elevi la punctul a) și crește cu 1 prima notă a elevului cu cnp-ul primit
ca parametru. Funcția returnează nota după modificare sau None dacă cnp-ul nu există.
Apelați funcția pentru un cnp citit de la tastatură.

c) Scrieți o funcție care primește ca parametri un cnp, o listă de note și structura de date în
care s-au memorat datele despre elevi la punctul a) și adaugă lista de note la notele elevului
cu cnp-ul primit ca parametru. Funcția returnează lista de note după modificare sau None
dacă cnp-ul nu există. Apelați funcția pentru un cnp citit de la tastatură si lista l_note=[10,8].

d) Scrieți o funcție care primește ca parametri un cnp și structura de date în care s-au
memorat datele despre elevi la punctul a) și șterge informațiile despre elevul cu acest cnp.
Apelați funcția pentru un cnp citit de la tastatură (dacă cnp-ul nu este în listă funcția nu va
modifica nimic și nu va da eroare)

e) Folosind structura de date în care s-au memorat datele despre elevi la punctul a) (nu citind
din nou datele) construiți în memorie o lista de liste cu elevii din fișier, un element din lista
fiind de forma [nume, prenume, lista de note] ordonată descrescător după medie și, în caz de
egalitate, după nume și afișați elementele listei în fișierul „elevi.out”.

f) Scrieți o funcție care primește ca parametru structura de date în care s-au memorat datele
despre elevi la punctul a) și adaugă la informațiile asociate unui student un cod de lungime 6
generat aleator care conține 3 litere urmate de 3 cifre. Exemplu de apel:
genereaza
coduri(d)
_
print(d)
'''

#a)
fin=open("elevi.in","r")

lines=fin.readlines()
d={}
for line in lines:
    line=line.split()
    cnp=line[0]
    
    nume=line[1]
    prenume=line[2]
    note=[int(x) for x in line[3:]]
    
    d[cnp]={"nume":[nume,prenume],"note":note}
    
#b)
def marire_prima_nota(cnp,d):
    if cnp in d:
        if d[cnp]['note'][0]<10:
            d[cnp]['note'][0]+=1
        return d[cnp]['note'][0]
    else:
        return None

print(marire_prima_nota("1412900000041", d))


#c)
def adauga_note(cnp,l_note,d):
    if cnp in d:
        d[cnp]['note'].extend(l_note)
        return d[cnp]['note']
    else:
        return None
l_note=[10,8]
adauga_note('2402900000041',l_note,d)


#d)
def sterge(cnp,d):
    if cnp in d:
        del d[cnp]
#e)
fout=open("elevi.out",'w')

lista_elevi=[]
for x in d:
    
    elev=[]
    elev.append(d[x]['nume'][0])
    elev.append(d[x]['nume'][1])
    elev.append(d[x]['note'])
    lista_elevi.append(elev)

def medie(x):
    suma=sum(x[2])
    nr_note=len(x[2])
    medie=suma/nr_note
    return medie

lista_elevi=sorted(lista_elevi, key=lambda x:x[0])
lista_elevi=sorted(lista_elevi, key=medie, reverse=True)
for elevi in lista_elevi:
    mystring=" ".join(map(str,elevi))
    fout.write(mystring+'\n')
    
#g
def genereaza_coduri(d):
    for elevi in d:
        nr_random=str(300*int(elevi[0:2]))
        nr_random=nr_random[0:3]
        print(nr_random)
        litere_random=""
        for i in nr_random:
            litere_random+=chr(ord('a')+int(i))
        print(litere_random)
        codd=litere_random+nr_random
        d[elevi]['cod']=codd
        
        
genereaza_coduri(d)
print(d)












fout.close()
fin.close()

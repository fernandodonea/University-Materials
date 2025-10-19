#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 01:00:29 2025

@author: fernandodonea
"""

'''
Fișierul text cinema.in conține programul dintr-o zi al unui lanț de
cinematografe. Fiecare linie din fișier are următoarea structură:
nume_cinemat ogr af%nume_film%or e_de_difuzar e
unde nume_cinemat ogr af este un șir de caractere reprezentând numele unui
cinematograf, nume_film este numele unui film (numele cinematografului și al filmului
sunt formate din cuvinte separate prin câte un spațiu și nu conțin caracterul '%'), iar
or e_de_difuzar e este un șir de caractere conținând orele (sub forma hh:mm) la care este
programat filmul în cinematograf, orele fiind separate prin câte un spațiu. Un exemplu
de astfel de fișier este:
    
a) [2,5 p.] Să se memoreze datele din fișier într-o singură structură de date astfel încât
să se răspundă cât mai eficient la cerințele de la punctele următoare.
b) [1 p.] Scrieți o funcție st er ge_or ecare are următorii parametri (în această ordine):
● structura în care s-au memorat datele la cerința a)
● un șir de caractere cinemareprezentând numele unui cinematograf
● un șir de caractere filmreprezentând numele unui film
● mulțime or eavând ca elemente șiruri de caractere de forma hh :mm
Funcția va șterge din programul cinematografului cinema programările filmului film de
la orele din mulțimea or e și va returna o listă cu filmele programate la cinematograful
cinema după această actualizare. Se citesc de la tastatură un nume de film f , un nume de
cinematograf c și un șir de caractere o de forma hh :mm reprezentând o oră. Să se
apeleze funcția st er ge_or e pentru a șterge programarea filmului fla cinematograful cla
ora o și să se afișeze lista returnată; după apelul funcției să se afișeze și structura în care
s-au memorat datele.
c) [1,5 p.] Scrieți o funcție cinema_filmcare primește următorii parametri: structura în
care s-au memorat datele la cerința a), un număr variabil de șiruri de caractere
reprezentând nume de cinematografe și doi parametri or a_minima și or a_maxima
șiruri de caractere de forma “hh:mm” reprezentând ore. Funcția returnează o listă de
tupluri cu elementele de tip (nume_film , nume_cinema , lista_de_or e ) cu filmele care
rulează (încep) la cel puțin unul dintre cinematografele primite ca parametru între
orele or a_minimași or a_maxima , unde:
● nume_filmeste numele unui astfel de film
● nume_cinemaeste un nume de cinema dintre cele primite ca parametru la care
rulează filmul nume_film
● lista_de_or eeste lista orelor la care este programat filmul nume_filmla
cinematograful nume_cinemaîntre orele or a_minimași or a_maxima, ordonată
crescător
Lista returnată va fi ordonată crescător după numele filmului, apoi, în caz de egalitate,
descrescător după numărul de elemente din lista_de_or e. Să se apeleze funcția pentru
cinematografele ‘Cinema 1’și ‘Cinema 2’ , or a_minima "14:00" și or a_maxima "22:00" și
să se afișeze lista returnată. Explicații : pentru datele din fișier lista returnată va fi
[('Gasca Animalut elor', 'Cinema 2', ['15:00', '18:30', '20:00']), ('Minionii 2', 'Cinema 2',
['15:00', '18:30', '20:30']), ('Minionii 2', 'Cinema 1', ['18:30'])] ; filmul ‘Elfii cof etari’ nu
apare în listă deoarece este programat mai devreme de ora “14:00”.
'''

#a
fin=open("cinema.in",'r')
lines=fin.readlines()
d={}
for line in lines:
    line=line.strip()
    cinema,film,orar=line.split(" % ")
    orar=orar.split()
    if cinema not in d:
        d[cinema] = {}
    
    if film not in d[cinema]:
        d[cinema][film] = orar
    else:
        d[cinema][film].extend(orar)  # Extinde lista de ore dacă filmul există deja
            
           

#b
def sterge_ore(d,cinema,film,ore):
   ore=ore.split()
   
   if cinema in d:
       if film in d[cinema]:
           d[cinema][film]=[x for x in d[cinema][film] if x not in ore]
       #stergem daca nu mai exista filme
       if not d[cinema][film]:
           del d[cinema][film]
   return list(d[cinema])

print(sterge_ore(d,"Cinema 1", "Minionii 2", "20:30"))

#c)

def cinema_film(d,*cinematografe,ora_minima,ora_maxima):
    h1,m1=ora_minima.split(":")
    h2,m2=ora_maxima.split(":")
    
    for cinema in cinematografe:
        lista=[]
        for film in d[cinema]:
            ore_disp=[]
            l=[]
            for ora in d[cinema][film]:
                hh,mm=ora.split(":")
                
                if hh>h1 or (hh==h1 and mm>m1):
                    if hh<h2 or (hh==h2 and mm<m2):
                        x=hh+":"+mm
                        ore_disp.append(x)
            if len(ore_disp)!=0:
                l=[film,cinema,ore_disp]
                lista.append(l)
                        
    lista=sorted(lista,key=lambda x:(x[0],len(x[1])))
    print(lista)
    
    
cinema_film(d,"Cinema 1","Cinema 2",ora_minima="14:00",ora_maxima="22:00")



    

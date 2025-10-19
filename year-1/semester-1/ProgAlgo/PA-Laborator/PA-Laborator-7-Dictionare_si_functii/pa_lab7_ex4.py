#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 22:43:14 2025

@author: fernandodonea
"""

'''

Fișierul text cinema.in conține programul dintr-o zi al unui lanț de cinematografe. Fiecare
linie din fișier are următoarea structură:
nume_cinematograf % nume_film % ore_de_difuzare
unde nume_cinematograf este un șir de caractere reprezentând numele unui cinematograf,
nume_film este numele unui film (numele cinematografului și al filmului sunt formate din
cuvinte separate prin câte un spațiu și nu conțin caracterul '%'), iar ore_de_difuzare este un șir
de caractere conținând orele (sub forma hh:mm) la care este programat filmul în
cinematograf, orele fiind separate prin câte un spațiu. Un exemplu de astfel de fișier este:
    
    
a) [2,5 p.] Să se memoreze datele din fișier într-o singură structură de date astfel încât să
se răspundă cât mai eficient la cerințele de la punctele următoare.
b) [1 p.] Scrieți o funcție sterge_ore care are următorii parametri (în această ordine):
· structura în care s-au memorat datele la cerința a)
· un șir de caractere cinema reprezentând numele unui cinematograf
· un șir de caractere film reprezentând numele unui film
· mulțime ore având ca elemente șiruri de caractere de forma hh:mm

    Funcția va șterge din programul cinematografului cinema programările filmului film de la
orele din mulțimea ore și va returna o listă cu filmele programate la cinematograful cinema
după această actualizare. Se citesc de la tastatură un nume de film f, un nume de cinematograf
c și un șir de caractere o de forma hh:mm reprezentând o oră. Să se apeleze funcția sterge_ore
pentru a șterge programarea filmului f la cinematograful c la ora o și să se afișeze lista
returnată; după apelul funcției să se afișeze și structura în care s-au memorat datele.
c) [1,5 p.] Scrieți o funcție cinema_film care primește următorii parametri: structura în
care s-au memorat datele la cerința a), un număr variabil de șiruri de caractere
reprezentând nume de cinematografe și doi parametri ora_minima și ora_maxima
șiruri de caractere de forma “hh:mm” reprezentând ore. Funcția returnează o listă de
tupluri cu elementele de tip (nume_film, nume_cinema, lista_de_ore) cu filmele care
rulează (încep) la cel puțin unul dintre cinematografele primite ca parametru între
orele ora_minima și ora_maxima, unde:
nume_film este numele unui astfel de film
· nume_cinema este un nume de cinema dintre cele primite ca parametru la care rulează
filmul nume_film
· lista_de_ore este lista orelor la care este programat filmul nume_film la cinematograful
nume_cinema între orele ora_minima și ora_maxima, ordonată crescător
Lista returnată va fi ordonată crescător după numele filmului, apoi, în caz de egalitate,
descrescător după numărul de elemente din lista_de_ore. Să se apeleze funcția pentru
cinematografele ‘Cinema 1’ și ‘Cinema 2’, ora_minima "14:00" și ora_maxima "22:00" și să
se afișeze lista returnată. Explicații: pentru datele din fișier lista returnată va fi [('Gasca
Animalutelor', 'Cinema 2', ['15:00', '18:30', '20:00']), ('Minionii 2', 'Cinema 2', ['15:00',
'18:30', '20:30']), ('Minionii 2', 'Cinema 1', ['18:30'])]; filmul ‘Elfii cofetari’ nu apare în listă
deoarece este programat mai devreme de ora “14:00”.    
    
'''

fin = open("cinema.in", 'r')
lines = fin.readlines()
d = {}

for line in lines:
    line = line.strip()
    cinema, film, orar = line.split(" % ")
    orar = orar.split()
    if cinema not in d:
        d[cinema] = {}
    if film not in d[cinema]:
        d[cinema][film] = orar
    else:
        d[cinema][film].extend(orar)  # Extinde lista de ore dacă filmul există deja

# Afișează structura


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
for x in d:
    print(x,d[x])
    


print()
def cinema_film(d,*cinematografe,ora_minima,ora_maxima):
    h1,m1=ora_minima.split(":")
    h2,m2=ora_maxima.split(":")
    
    rez=[]
    for cinema in cinematografe:
        if cinema in d:
            for film in d[cinema]:
                ore_disp=d[cinema][film]
                l=[]
                for ora in ore_disp:
                    
                    hh,mm=ora.split(":")
                    
                    if hh>h1 or (hh==h1 and mm>m1):
                        if hh<h2 or(hh==h2 and mm<m2):
                            y=hh+":"+mm
                            l.append(y)
                            
                if len(l)!=0:
                   film_lista=[film,cinema,l]
                   rez.append(film_lista)
    rez=sorted(rez,key=lambda x:(x[0],-len(x[2])))
    print(rez)

    
cinema_film(d,"Cinema 1","Cinema 2",ora_minima="14:00",ora_maxima="22:00")


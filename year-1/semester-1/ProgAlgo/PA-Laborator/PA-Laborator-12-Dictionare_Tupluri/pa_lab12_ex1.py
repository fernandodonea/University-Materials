#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:04:58 2025

@author: fernandodonea
"""

'''
Fișierul text banci.in conține informații despre diverse bănci. Fiecare linie din fișier are
următoarea structură:
id_banca % nume_banca % numar_clienti % capital_total
Unde:
- id_banca este un număr întreg reprezentând identificatorul unic al unei bănci
- nume_banca este un șir de caractere reprezentând numele unei bănci
- numar_clienti este un număr întreg indicând numărul total de clienți ai băncii,
- capital_total este un număr real reprezentând capitalul total al băncii

Cerinte:
a) [2.5 p.] Implementați o funcție citeste_informatii_banci cu un parametru reprezentând
numele unui fișier text ("banci.in") care conține informații despre bănci. Funcția trebuie să
returneze o structură de date care să memoreze eficient informațiile din fișier pentru a
răspunde la cerințele următoare.


b) [1 p.] Scrieți o funcție sterge_banca care are următorii parametri (în această ordine):

- structura în care s-au memorat datele la cerința a)
- un număr întreg id_banca reprezentând identificatorul unic al unei bănci

Funcția va șterge banca cu identificatorul id_banca și va returna o listă cu informațiile despre
celelalte bănci după această actualizare. Se citeste de la tastatură un id_banca și se apelează
funcția sterge_banca pentru a șterge banca respectivă și a afișa lista returnată; după apelul
funcției să se afișeze și structura în care s-au memorat datele.


c) [1.5 p.] Scrieți o funcție media_clienti_banca care primește ca parametru structura în care
s-au memorat datele la cerința a). Funcția va calcula și returna media generală a numărului de
clienți al tuturor băncilor. Să se apeleze funcția și să se afișeze rezultatul obtinut

'''

#a)
def citire(fisier):
    fin=open(fisier,'r')
    
    d={}
    lines=fin.readlines()
    for line in lines:
        line=line.strip()
        id_banca,nume_banca,numar_clienti,capital_total=line.split(" % ")
        id_banca=int(id_banca)
        numar_clienti=int(numar_clienti)
        capital_total=float(capital_total)
        if id not in d:
            d[id_banca]=[nume_banca,numar_clienti,capital_total]
    return d


d=citire("banci.in")
def sterge_banca(d,id_banca):
    if id_banca in d:
        del d[id_banca]
    l=[]
    for x in d:
        lista=[x,d[x][0]]
        l.append(lista)
    return l

id_ster=int(input("citeste idul bancii pt sters: "))
print(sterge_banca(d,id_ster))
print(d)

def medie_clienti(d):
    n=len(d)
    suma=0
    for x in d:
        suma+=d[x][2]
    return suma/n
print(medie_clienti(d))

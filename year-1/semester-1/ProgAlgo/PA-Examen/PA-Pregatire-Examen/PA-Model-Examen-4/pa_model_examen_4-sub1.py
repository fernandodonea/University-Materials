#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 00:24:01 2025

@author: fernandodonea
"""

#a)
'''
Scrieți o funcție palindrom care primește un număr variabil de cuvinte formate doar
din litere mici ale alfabetului englez și returnează informații despre cuvintele palindrom
sub forma unui dicționar de perechi {cuvant palindrom: lista de litere}. Cheia
este cuvântul primit ca parametru dacă acesta este palindrom, iar lista de litere este
formată din vocalele cuvântului dacă numărul vocalelor este mai mare decât numărul
consoanelor, altfel lista va fi formată din consoanele cuvântului. Listele de litere vor fi
sortate în ordine lexicografică. De exemplu, pentru apelul palindrom ('asa',
'merem', 'palindrom') funcția va returna dicționarul {'asa': ['a'], 'merem':
['m', 'r']} (1.5 p.)
                                                      
'''
def palindrom(*cuvinte):
    d={}
    for cuv in cuvinte:
        if cuv==cuv[::-1]:
            voc=0
            cons=0
            v=[]
            c=[]
            for lit in cuv:
                if lit in "aeiou":
                    voc+=1
                    if lit not in v:
                        v.append(lit)
                else:
                    cons+=1
                    if lit not in c:
                        c.append(lit)
            v.sort()
            c.sort()
            if voc>cons:
                d[cuv]=v
            else:
                d[cuv]=c
    return d
print(palindrom("asa","merem","palindrom"))

#b)
'''
Înlocuiți punctele de suspensie din instrucțiunea numere = […] cu o secvență de
inițializare (list comprehension) astfel încât, după executarea sa, lista să conțină numerele
naturale formate din exact două cifre care nu sunt pătrate perfecte și nici divizibile cu 7.
(0.5 p.)
'''
numere=[x for x in range(10,100) if (x%7==0 or x==(int(x**0.5))**2)]
print(numere)
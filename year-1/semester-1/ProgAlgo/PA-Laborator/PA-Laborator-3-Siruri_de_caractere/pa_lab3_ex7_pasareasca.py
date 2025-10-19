#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 21:22:10 2025

@author: fernandodonea
"""

'''
Se citește de la tastatură un text. Se cere să se “traducă” în limba păsărească textul dat
astfel: după fiecare vocală se adaugă litera p și încă o dată acea vocală (după a, e, i, o, u
se adaugă respectiv pa, pe, pi, po, pu). Exemplu: “ Ana are mere.” devine “ Apanapa
aparepe meperepe.” Fiind dat un astfel de text în limba păsărească, se poate obține
textul original? Dacă da, scrieți un program care primind un text în limba păsărească
construiește în memorie și afișează textul inițial.
'''
s=input("Citit o fraza ce trebuie tradusa in pasareasca: ")

prop=""

for i in s:
    prop+=i
    if i in "aeiou":
        prop+="p"
        prop+=i
    elif i in "AEIOU":
        prop+="p"
        prop+=chr(ord(i)+32)
print(prop)

for i in "aeiou":
    pasare=i+"p"+i
    prop=prop.replace(pasare,i)
for i in "AEIOU":
    pasare=i+"p"+chr(ord(i)+32)
    prop=prop.replace(pasare,i)
    
print(prop)
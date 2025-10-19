#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 20:42:13 2025

@author: fernandodonea
"""
'''
Într-o propoziție a fost efectuată, posibil de mai multe ori, aceeași greșeală de
ortografie. Se citesc de la tastatură o propoziție și două șiruri s și t - cel corect și cum a
fost scris greșit, fiecare dintre cele trei date de intrare fiind date pe câte o line
a) Să se afișeze propoziția corectă. 
De exemplu, pentru propoziția 
"Problemele cu șiruri de caracteger nu sunt ggerle!" 
s= “re”
t=“ger” 
se va afișa 
"Problemele cu șiruri de caractere nu sunt grele!".
b) Modificați programul astfel încât să citească un număr natural p și să corecteze
maxim p astfel de greșeli (care nu se suprapun), iar dacă sunt mai multe să afișeze
mesajul: “textul contine prea multe greseli, doar p au fost corectate”
'''

''' a)
prop=input("Cititi fraza: ")
s=input("sir corect=")
t=input("sir gresit=")

prop=prop.replace(t,s)
print(prop)

'''
prop=input("Cititi fraza: ")
s=input("sir corect: ")
t=input("sir gresit: ")

p=int(input("p="))

greseli=prop.count(t)

prop=prop.replace(t,s,p)

if p<greseli:
    print(f"textul contine prea multe greseli, doar {p} au fost corectate")
else:
    print(prop)


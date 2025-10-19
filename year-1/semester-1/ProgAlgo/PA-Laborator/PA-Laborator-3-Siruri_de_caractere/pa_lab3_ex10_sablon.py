#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 21:41:04 2025

@author: fernandodonea
"""

'''
Un șir de caractere s este șablon pentru un șir de caractere x dacă 
- are aceeași lungime cu x 
- este alcătuit numai din caractere ale mulțimii {*,#,?}, 
- pe fiecare poziție din s în care apare * în x apare vocală, 
- pe fiecare poziție din s în care apare # în x apare consoană, 
- pe fiecare poziție din s în care apare ? în x putem avea orice caracter



Scrieți un program care citește de tastatură două șiruri de cel mult 30 caractere de aceeași lungime 
care conțin doar litere mici ale alfabetului englez și construiește în memorie și apoi afișează pe ecran un cel mai bun șablon comun al lor, adică șablonul comun cu număr minim de caractere ?.

intrare:
    
diamant pierdut

iesire

#**#??#
'''

s,t=input("Citit cele doua siruri: ").split()
n=len(s)
sablon=""
for i in range(n):
    if s[i] in "aeiou" and t[i] in "aeiou":
        sablon+="*"
    elif s[i] not in "aeiou" and t[i] not in "aeiou":
        sablon+="#"
    else:
        sablon+="?"
print(f"Sablonu:{sablon}")
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:45:38 2025

@author: fernandodonea
"""

'''
Scrieți un program care să afișeze pe ecran cuvintele distincte dintr-un
fișier text, grupate în ordinea descrescătoare a frecvențelor lor de apariție, iar în cazul
unei anumite frecvențe, cuvintele vor fi afișate în ordine alfabetică. Nu se va face
distincție între litere mici și litere mari. Textul poate fi împărțit pe mai multe linii, iar pe
o linie cuvintele sunt despărțite între ele prin spații. Fișierul poate să conțină și linii
vide. Numele fișierului text se va citi de la tastatură.
'''

fin=open("exemplu.txt",'r')
lines=fin.readlines()
d={}
for line in lines:
    line=line.split()
    for cuv in line:
        cuv=cuv.lower()
        if cuv not in d:
            d[cuv]=1
        else:
            d[cuv]+=1
d2={}
for x in d:
    if d[x] not in d2:
        d2[d[x]]=[x]
    else:
        d2[d[x]].append(x)


l=[]
l=sorted(d2,reverse=True)
for x in l:
    print(f"Frecventa {x}:",end=" ")
    cuvinte=[]
    for y in d2[x]:
        cuvinte.append(y)
    cuvinte.sort()
    print(*cuvinte,sep=", ")

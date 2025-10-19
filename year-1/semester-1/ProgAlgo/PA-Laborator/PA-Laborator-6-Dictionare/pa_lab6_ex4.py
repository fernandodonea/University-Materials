#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 20:27:42 2025

@author: fernandodonea
"""

'''
Se dă un fișier cu cuvinte pe mai multe linii separate prin spații. Scrieți un program
are să determine grupurile de cuvinte din fișier care au aceleași litere (nu neapărat cu aceeași
frecvență). Numele fișierului de intrare se va citi de la tastatură, iar grupurile formate din cel
puțin două cuvinte se vor scrie în fișierul text “litere.txt”, câte un grup pe o linie. Cuvintele
din fiecare grup vor fi sortate după lungime, iar în caz de lungimi egale, lexicografic, iar
grupurile se vor scrie în fișier în ordinea descrescătoare a numărului de elemente din
mulțimile literelor.

Pentru fișierul de intrare:
apar mare
si amara rapa para
par isi rama

fișierul de ieșire va fi
par apar para rapa
rama amara
si isi
'''
fin=open('litere.in','r')
fout=open('litere.out','w')
lines=fin.readlines()
l=[x for line in lines for x in line.split()]
alfabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
d={}
for cuv in l:
    cod=""
    for lit in alfabet:
        if lit in cuv:
            cod+=lit
    if cod not in d:
        d[cod]=[cuv]
    else:
        d[cod].append(cuv)
#sortare dictionar
for cod in d:
    d[cod].sort()
    d[cod].sort(key=lambda x:len(x))

l=sorted(d,key=lambda x:-len(d[x]))

for x in l:
    mystring=""
    if len(d[x])>=2:
        for cuv in d[x]:
            mystring+=" "+cuv
        mystring=mystring.strip()
        fout.write(mystring+"\n")


fout.close()
fin.close()       
    
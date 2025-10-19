#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 20:05:19 2025

@author: fernandodonea
"""

'''
Scrieți un program care să determine grupurile de cuvinte dintr-un fișier text care
p-rimează între ele = au aceleași ultime p-litere (p citit de la tastatura). Numele fișierului de
intrare se va citi de la tastatură, iar grupurile se vor scrie în fișierul text “rime.txt”, câte un
grup pe o linie, în ordine descrescătoare în raport cu numărul de elemente din grup.
Cuvintele din fiecare grup vor fi sortate lexicografic descrescător.
De exemplu, pentru p=2 și fișierul:

    
ana dana
mere pere prune
bune
banana si gutui amare are

rime.txt va fi:
pere mere are amare
dana banana ana
prune bune
si
gutui

'''
nume_fisier=input("cititi numele fisierului: ")
#nume_fisier='rime.in'
p=int(input("p="))

fin=open(nume_fisier,'r')
fout=open("rime.txt",'w')

lines=fin.readlines()
cuvinte=[]
d={}
for line in lines:
    line=line.split()
    for cuv in line:
        sufix=cuv[-p:]
        if sufix not in d:
            d[sufix]=[cuv]
        else:
            d[sufix].append(cuv)
for sufix in d:
    d[sufix].sort(reverse=True)

l=sorted(d,key=lambda x:-len(d[x]))
for suf in l:
    mystring=""
    for cuv in d[suf]:
        mystring+=" "+cuv
    mystring=mystring.strip(" ")
    fout.write(mystring+'\n')



    
fin.close()
fout.close()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 22:14:29 2025

@author: fernandodonea
"""

'''
Mirel a învățat astăzi la școală la ora de matematică despre baze de numerație. De exemplu a învățat cum să transforme un număr dintr-o bază oarecare în baza zece. Pentru acasă a primit următoarea temă:

Pentru un cuvânt dat, se înlocuiește fiecare literă a acestuia cu numărul de litere de dinaintea sa în alfabet, astfel litera a devine 0, litera b devine 1, litera c devine 2 ș.a.m.d. , iar cuvântul dat devine un număr în baza 26.

Să se transforme acest număr în baza zece.
'''

fin=open("baza.in",'r')
fout=open("baza.out",'w')

cuv=fin.readline()

n=len(cuv)
sum=0
cuv=cuv[::-1]

for i in range(0,n):
    lit=ord(cuv[i])-97
    sum+=lit*(26**i)
fout.write(str(sum))


    
fout.close()
fin.close()

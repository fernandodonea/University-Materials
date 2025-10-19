#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:18:20 2025

@author: fernandodonea
"""

'''
Scrieți un program care să citească de la tastatură două numere întregi, două numere reale și două
caractere (variantă: datele se dau fiecare pe o linie / date se dau pe aceeași linie, separate cu spațiu/
datele se dau câte două pe linie, separate cu spațiu), iar apoi se le afișeze astfel:
● toate pe un singur rând, în ordinea în care au fost citite;
● toate pe un singur rând, sub forma: un număr întreg, un număr real, un caracter, un număr
întreg, un număr real, un caracter;
● fiecare pe câte un rând;
● câte două pe un rând.
'''
l=input("Cititi ouă numere întregi, două numere reale și două caractere:\n ").split()

for i in range(0,2):
    l[i]=int(l[i])
for i in range(2,4):
    l[i]=float(l[i])
 #toate pe un singur rând, în ordinea în care au fost citite   
print(*l)

#toate pe un singur rând, sub forma: un număr întreg, un număr real, un caracter, un număr întreg, un număr real, un caracter;
for i in range(0,len(l),2):
    print(l[i],end=" ")
for i in range(1,len(l),2):
    print(l[i],end=" ")
print()

#fiecare pe câte un rând;
for i in l:
    print(i)

#câte două pe un rând
for i in range(0,len(l),2):
    print(l[i],l[i+1])


    



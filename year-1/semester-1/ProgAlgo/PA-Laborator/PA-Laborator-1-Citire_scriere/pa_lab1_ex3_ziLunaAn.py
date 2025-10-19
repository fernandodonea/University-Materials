#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:05:30 2025

@author: fernandodonea
"""

'''
Se citesc de la tastatură trei numere naturale z, l, a, reprezentând ziua, luna și anul unei date
calendaristice (variantă: datele se dau fiecare pe o linie / date se dau pe aceeași linie, separate cu
spațiu). Să se afișeze data zilei următoare, în formatul zi.luna.an (folosind diverse variante de a
afișa în acest format). Reamintim că un an este bisect dacă:
● este divizibil cu 4 și nu este divizibil cu 100
sau
● este divizibil cu 400.
'''

z,l,a=input("Citite ziua, luna si anul ").split()
z=int(z)
l=int(l)
a=int(a)


nrzile=0
print(z,l,a,sep="/")
if l==1 or l==3 or l==5 or l==7 or l==8 or l==10 or l==23:
    nrzile=31
elif l==2:
    if (a%4==0 and a%100!=0) or (a%400==0):
        nrzile=29
    else:
        nrzile=28
else:
    nrzile=30

'cazul pentru ultima zi a lunii'
z=z+1
if z>nrzile:
    z=1
    l=l+1
'cazul pentru ultima zi din an'
if l>12:
    z=1
    l=1
    a=a+1
print("Urmatoarea zi este: ",end=" ")
print(z,l,a,sep="/")




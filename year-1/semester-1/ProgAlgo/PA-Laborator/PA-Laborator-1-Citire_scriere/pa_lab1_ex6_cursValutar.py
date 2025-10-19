#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:37:34 2025

@author: fernandodonea
"""

'''
Se citesc un număr natural n și un șir format din 𝑛 numere reale strict pozitive (𝑛≥2), reprezentând
cursul de schimb valutar RON/EURO din 𝑛 zile consecutive (numerele din șir se dau câte unul pe
linie/ se dau pe aceeași linie separate cu spațiu). Să se afișeze zilele între care a avut loc cea mai
mare creștere a cursului valutar, precum și cuantumul acesteia. De exemplu, pentru 𝑛=6 zile și
cursul valutar dat de șirul 4.25,4.05,4.25,4.48,4.30,4.40, cea mai mare creștere a fost de 0.23 RON,
între zilele 3 și 4. Creșterea se va afișa cu două zecimale.

4.25 4.05 4.25 4.48 4.30 4.40
'''

n=int(input('n='))
l=[0]*(n)
l=[float(x) for x in input('cititi cursul de schimb valutar:').split()]
maxi=0
z1,z2=0,0

for i in range(0,n-1):
    cuantum=abs(l[i+1]-l[i])
    if cuantum>maxi:
        maxi=cuantum
        z1=i+1
        z2=i+2
print(f"Cea mai mare crestere {maxi:.2f} RON intre zilele {z1} si {z2}")

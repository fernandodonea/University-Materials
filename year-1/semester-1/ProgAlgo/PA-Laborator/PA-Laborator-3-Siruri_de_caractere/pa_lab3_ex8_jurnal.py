#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 21:29:54 2025

@author: fernandodonea
"""

'''
Jurnalul electronic al Anei conține, în fiecare zi, câte o frază cu informații despre
cheltuielile pe care ea le-a efectuat în ziua respectivă. Scrieți un program care să
citească o frază de acest tip din jurnalul Anei și apoi să afișeze suma totală cheltuită de
ea în ziua respectivă. De exemplu, pentru fraza “ Astăzi am cumpărat pâine de 5 RON, pe
lapte am dat 10 RON, iar de 15 RON am cumpărat niște cașcaval. De asemenea, mi-am
cumpărat și niște papuci cu 50 RON!” , programul trebuie să afișeze suma totală de 80
RON. Fraza se consideră corectă, adică toate numerele care apar în ea sunt numere
naturale reprezentând sume cheltuite de Ana în ziua respectivă!


Astăzi am cumpărat pâine de 5 RON, pe lapte am dat 10 RON, iar de 15 RON am cumpărat niște cașcaval. De asemenea, mi-am cumpărat și niște papuci cu 50 RON!”

'''

s=input("Cititi fraza din jurnal: ")

prop=s.split()
n=len(prop)
s=0
for i in range(n-1):
    if prop[i].isdigit()==True:
        if "RON" in prop[i+1]:
            x=int(prop[i])
            s+=x
print(f"{s} RON")
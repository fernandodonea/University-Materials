#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:48:18 2025

@author: fernandodonea
"""

'''
Gigel își dorește foarte mult să-și cumpere o jucărie care costă 𝑠
lei. Pentru a reuși cât mai repede
acest lucru, el se hotărăște să depună în pușculița sa, în fiecare zi, câte o sumă de bani (număr
natural nenul). Cunoscând sumele depuse de Gigel zilnic (variantă: datele se dau fiecare pe o linie /
date se dau pe aceeași linie, separate cu spațiu) afișați după câte zile Gigel reușește să strângă în
pușculiță suma necesară, suma medie zilnică pe care acesta a depus-o în pușculiță (cu 3 zecimale),
precum și suma care îi rămâne după ce își cumpără jucăria.
'''

S=int(input("S="))

l=[int(x) for x in input().split()]
n=len(l)


suma=0
ok=False
for i in range(0,n):
    suma=suma+l[i]
    if suma>=S and ok==False:
        print(f"numar zile necesare:{i+1}")
        ok=True
medie=suma/n
print(f'suma medie zilnica {medie:.2f}')

if ok==True:
    print(f"suma ramasa: {suma-S}")
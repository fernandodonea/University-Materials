#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:10:29 2025

@author: fernandodonea
"""

'''
Se citește o expresie de forma 𝑥 𝑜𝑝 𝑦 𝑥 𝑦 , unde și sunt două numere reale nenule, iar este unul
𝑜𝑝
dintre operatorii +,
−
,
* /
sau (variantă: datele se dau fiecare pe o linie / date se dau pe aceeași
linie, separate cu spațiu) Să se afișeze pe ecran rezultatul expresiei citite sub forma 𝑥 𝑜𝑝 𝑦 = 𝑟
, cu
o precizie de 3 zecimale. Dacă operatorul introdus este incorect, se va afișa un mesaj de eroare.
'''

x,op,y=input('citit x op y: ').split()
x=int(x)
y=int(y)


if op in "+-*/":
    if op=='+':
        r=x+y
    elif op=='-':
        r=x-y
    elif op=='*':
        r=x*y
    elif op=='/':
        r=x/y
    print(f"{x}{op}{y}={r:.3f}")
else:
    print("operator gresit")    
    
    
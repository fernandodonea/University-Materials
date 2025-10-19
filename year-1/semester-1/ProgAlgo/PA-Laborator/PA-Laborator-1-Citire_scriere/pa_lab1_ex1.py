#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 16:51:56 2025

@author: fernandodonea
"""

'''
Se citesc două numere întregi (variantă: datele se dau fiecare pe o linie / date se dau pe aceeași
linie, separate cu spațiu). Să se afișeze suma acestor numere și produsul acestora. Variante de
afișare:
● pe aceeași linie separate cu spațiu /separate cu virgula
● pe linii diferite
● mesaj de forma: suma numerelor…. si … este ...., iar produsul este ...
'''



a=int(input('a='))
b=int(input('b='))

n,m=input('n,m=').split()
n=int(n)
m=int(m)


print(a+b,a*b,sep=',')
print(n+m,n*m,sep='\n')
print(f"suma numerelor este {a+b} si produsul este {a*b}")


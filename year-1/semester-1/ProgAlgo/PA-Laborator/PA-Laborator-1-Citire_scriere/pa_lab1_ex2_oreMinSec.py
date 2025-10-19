#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:00:27 2025

@author: fernandodonea
"""

'''
Se citesc 3 numere naturale 𝑎, 𝑏
și c (variantă: datele se dau fiecare pe o linie / date se dau pe
aceeași linie, separate cu spațiu). Verificați faptul că numerele respective pot reprezenta ore, minute
și secunde, iar în caz afirmativ afișați cele 3 numere sub forma ℎℎ: 𝑚𝑚: 𝑠𝑠
. Dacă valorile citite
sunt incorecte, afișați un mesaj corespunzător.
'''

'varianta 1'
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))

if 0<=a<=23 and 0<=b<=59 and 0<=c<=59:
    if 0<=a<=9 :
        print("0",sep="",end="")
    print(a,":",sep="",end="")
    if 0<=b<=9 :
        print("0", sep="",end="")
    print(b, ":", sep="",end="")
    if 0<=c<=9:
        print("0", sep="",end="")
    print(c)
else:
    print("Date incorecte")

'variata 2'
a,b,c=input("Citite numerele a,b si c: ").split()
a=int(a)
b=int(b)
c=int(c)
if 0<=a<=23 and 0<=b<=59 and 0<=c<=59:
    if 0<=a<=9 :
        print("0",sep="",end="")
    print(a,":",sep="",end="")
    if 0<=b<=9 :
        print("0", sep="",end="")
    print(b, ":", sep="",end="")
    if 0<=c<=9:
        print("0", sep="",end="")
    print(c)
else:
    print("Date incorecte")

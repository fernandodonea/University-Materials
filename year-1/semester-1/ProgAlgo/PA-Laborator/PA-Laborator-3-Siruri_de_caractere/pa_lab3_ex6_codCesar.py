#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 21:13:16 2025

@author: fernandodonea
"""

'''
Cifrul lui Cezar
a) Se citește un text și un număr natural k. Să se afișeze textul cifrat cu cifrul lui Cezar ,
prin care fiecare literă (!doar literele) este înlocuită cu litera aflată peste 𝑘 poziții la
dreapta în alfabet în mod circular (valoarea 𝑘 reprezintă cheia secretă comună pe
care trebuie să o cunoască atât expeditorul, cât și destinatarul mesajului criptat).

De exemplu, pentru textul "O zi frumoasa!" și k=9 se va afișa “X ir oadvxjbj! "

b) Se citește un număr natural k și text criptat cu cifrul lui Cezar cu cheia k. Să se
afișeze textul decriptat.
'''

s=input("Cititi un mesaj ce tb criptat: ")
k=input("Cititi cheia secreta: ")
k=int(k)

prop=""

for i in s:
    x=ord(i)
    if (x>=65 and x<=90):
        x=x+k-65
        x=x%26
        x=x+65
    if (x>=97 and x<=122):
        x=x+k-97
        x=x%26
        x=x+97
    prop+=chr(x)
print(prop)


k=int(input('cititi cheia de decriptare: '))
s=input("cititi un mesaj de decriptat: ")

prop=""
for i in s:
    x=ord(i)
    if(x>=65 and x<=90):
        x=x-65
        x=x+26-k
        x=x%26
        x=x+65
    if (x>=97 and x<=122):
        x=x-97
        x=x+26-k
        x=x%26
        x=x+97
    prop+=chr(x)
print(prop)
        
        
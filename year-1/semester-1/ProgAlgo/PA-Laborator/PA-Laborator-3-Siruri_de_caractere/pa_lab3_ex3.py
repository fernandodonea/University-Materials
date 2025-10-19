#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 20:35:39 2025

@author: fernandodonea
"""

'''
Să se verifice (folosind întâi metoda find, apoi index) dacă un șir de caractere 𝑡 apare ca
subșir într-un șir 𝑠, iar în caz afirmativ să se afișeze toate pozițiile la care începe 𝑡 în 𝑠
(aparițiile care nu se suprapun), altfel să se afișeze un mesaj corespunzător . De
exemplu, șirul 𝑡 ="𝑎𝑏𝑐" apare ca subșir în șirul 𝑠 ="𝑎𝑏𝑐𝑐𝑎𝑏𝑐𝑎𝑏𝑎𝑏𝑐𝑐" începând cu
pozițiile 0, 4 și 9.
'''

s=input("Cititi un sir s: ")
t=input("Cititi un subsir t: ")

p=s.find(t)
while p!=-1:
    print(p)
    p=s.find(t,p+len(t))

try:
    p1=s.index(t)
    print(p1)
except:
    print("eroare")
    
try:
    while True:
        p1=s.index(t,p1+len(t))
        print(p1,end=" ")
except:
    pass



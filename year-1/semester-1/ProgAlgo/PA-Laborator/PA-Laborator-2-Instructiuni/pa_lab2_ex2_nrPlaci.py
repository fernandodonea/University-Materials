#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:22:22 2025

@author: fernandodonea
"""

'''
Un meșter trebuie să paveze întreaga pardoseală a unei bucătării cu formă dreptunghiulară
de dimensiune 𝐿1×𝐿2 centimetri, cu plăci de gresie pătrate, toate cu aceeași dimensiune.
Știind că meșterul nu vrea să taie nici o placă de gresie și vrea să folosească un număr
minim de plăci, să se determine dimensiunea plăcilor de gresie de care are nevoie, precum
și numărul lor. De exemplu, dacă 𝐿1=440 cm și 𝐿2=280 cm, atunci meșterul are nevoie de
77 de plăci de gresie, fiecare având latura de 40 cm. Dimensiunile L1 și L2 se citesc de la
tastatură de pe linii diferite / de pe aceeași linie separate cu spațiu). Numărul minim de
plăci și dimensiunea plăcilor se vor afișa pe aceeași linie, separate prin spațiu.
'''
l1,l2=input('Citeste lungimile bucatariei: ').split()
l1=int(l1)
l2=int(l2)
a=l1*l2 #aria
r=l1%l2
while r!=0:
    l1=l2
    l2=r
    r=l1%l2
print(l2)

nr=l2
dim=a//(nr*nr)
print('Numarul minim de placi este ',nr, 'iar dimensiunea placilor este',dim)

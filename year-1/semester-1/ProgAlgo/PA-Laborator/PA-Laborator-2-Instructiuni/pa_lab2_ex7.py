#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:56:29 2025

@author: fernandodonea
"""
'''
Se citește de la tastatură un număr natural 𝑛 și apoi un șir format din 𝑛 numere întregi
(date câte unul pe linie). Să se afișeze cea mai mică valoare citită, precum și numărul său
de apariții.
'''
n=int(input('n='))
print('citi sirul')
l=[int(x) for x in input().split()]

mini=min(l)
k=0
for i in l:
    if i==mini:
        k=k+1
print("minimul este",mini,"si apare de ",k,"ori")
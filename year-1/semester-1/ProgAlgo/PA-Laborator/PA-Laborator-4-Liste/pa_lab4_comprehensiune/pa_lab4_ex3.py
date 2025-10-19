#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 00:02:35 2025

@author: fernandodonea
"""

'''
Păsărească- traducerea în limba păsărească folosind comprehensiune: Se citește de
la tastatură un text. Se cere să se “traducă” în limba păsărească textul dat astfel: după
fiecare vocală se adaugă litera p și încă o dată acea vocală (după a, e, i, o, u se adaugă
respectiv pa, pe, pi, po, pu). Exemplu: “ Ana are mere.” devine “ Apanapa aparepe meperepe.”

'''

s=input("cititi un sir")

l=[x if x not in "AEIOUaeiou" else x+'p'+chr(ord(x)+32) if x in "AEIOU" else x+'p'+x for x in s ]
s_pasareasca="".join(l)
print(s_pasareasca)
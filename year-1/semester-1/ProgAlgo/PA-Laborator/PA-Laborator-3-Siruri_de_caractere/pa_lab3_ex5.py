#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 20:50:19 2025

@author: fernandodonea
"""

'''
a) Scrieți un program care să înlocuiască într-o propoziție toate aparițiile unui cuvânt 𝑠
cu un cuvânt 𝑡 (cuvânt, nu subșir). Cuvintele sunt separate prin unul sau mai multe
spații.
b) Aceeași cerință ca la a), dar pentru cazul în care cuvintele din propoziție sunt
despărțite între ele prin spații și semnele de punctuație uzuale
'''
prop=input("cititi o propozitie ")
s=input("cuvant gresit=")
t=input("cuvant corect=")

l=prop.split()
for i in range(len(l)):
    if l[i]==s:
        l[i]=t
prop=" ".join(l)
print(prop)



    

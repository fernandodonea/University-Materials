#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:44:29 2025

@author: fernandodonea
"""

'''
Se citește un număr natural nenul 𝑛. Să se afișeze cel mai mic și cel mare număr care pot
fi formate din cifrele lui 𝑛. De exemplu, pentru 𝑛=812383 trebuie afișate numerele
883321 și 123388.
'''

n=int(input('n='))

#maximul
maxi=0
for i in range(9,-1,-1):
    cn=n
    while cn!=0:
        c=cn%10
        cn=cn//10
        if c==i:
            maxi=maxi*10+c
print("maximul este:",maxi)

mini=0
pp=1
pz=1
for i in range(1,10,1):
    cn=n
    while cn!=0:
        c=cn%10
        if(c==i):
            mini=mini*10+c
            pp=pp*10
        cn=cn//10
cn=n
while cn!=0:
    if cn%10==0:
        pz=pz*10
    cn=cn//10
mini=mini//(pp//10)*(pp//10*pz)+mini%(pp//10)
print("minimul=",mini)

    
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 01:00:55 2025

@author: fernandodonea
"""

'''
Se dă o listă de numere naturale și un număr natural k. Să se elimine din listă
subsecvența de lungime k de sumă minimă (dacă sunt mai multe se va elimina prima = cea
mai din stânga) – fără a folosi liste suplimentare.
'''
k=int(input("k="))
l=[1,2,3,4,1,2,3,4,54,65]
mini=0
poz=0
for j in range(0,k):
    mini+=l[j]
print(mini)
for i in range(len(l)-k):
    suma=0
    for j in range (i,i+k):
        suma+=l[j]
    if suma<mini:
        mini=suma
        poz=i
print(mini,poz)
l[poz:(poz+k)]=[]
print(l)
    
    
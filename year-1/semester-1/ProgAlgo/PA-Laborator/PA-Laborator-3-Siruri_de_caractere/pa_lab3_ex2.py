#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 20:27:20 2025

@author: fernandodonea
"""

'''
Se citește un cuvânt s de cel mult 10 de caractere. Sa se afișeze pe câte o linie cuvintele
obținute succesiv din s tăind prima și ultima literă (afișate centrat pe 10 de caractere):
algoritm
lgorit
gori
or
'''
s=input('Cititi un sir de 10 caractere ')
print(s)
n=len(s)//2
for i in range (1,n,1):
    print(s[i:-i].center(10))


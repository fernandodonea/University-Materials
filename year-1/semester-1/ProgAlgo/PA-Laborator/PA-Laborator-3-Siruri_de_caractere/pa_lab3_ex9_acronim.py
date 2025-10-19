#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 21:36:38 2025

@author: fernandodonea
"""

'''
Se consideră un text cu cel mult 100 de caractere, în care cuvintele sunt formate numai din litere mari și mici ale alfabetului englez și sunt separate prin câte un spațiu.
Textul reprezintă numele unei instituții sau al unei organizații.

Scrieți un program care citește de la tastatură un text de tipul precizat și construiește în memorie, a
poi afișează pe ecran, un șir de caractere ce reprezintă acronimul corespunzător numelui citit. Acronimul este format din primul caracter al fiecărui cuvânt al numelui care începe cu majusculă.


intrare

Universitatea de Arte Plastice BUCURESTI

iesire:
UAPB


'''

s=input("Numele institutiei: ")

acronim=""
nume=s.split()
for cuvant in nume:
    if cuvant[0]>='A' and cuvant[0]<='Z':
        acronim+=cuvant[0]
        
print(acronim)

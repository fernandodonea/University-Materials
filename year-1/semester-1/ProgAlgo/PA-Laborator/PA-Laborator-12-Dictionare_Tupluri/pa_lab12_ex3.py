#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:23:23 2025

@author: fernandodonea
"""

'''

Considerăm o listă de tupluri care conțin informații despre filme, fiecare tuplu având
următoarele elemente: (nume_film, rating, an_aparitie, gen). Implementați un program care
să ofere opțiuni pentru sortarea listei de filme în funcție de diferite criterii. Aveți de
implementat mai multe subpuncte:
    
a. Sortați lista de filme în ordine descrescătoare în funcție de rating. Pentru fileme cu acelaşi
rating , sortați-le în ordine lexicografică descrescătoare în funcție de numele filmului.

b. Sortați lista de filme în ordine crescătoare după gen. Pentru filmele cu același gen,
sortați-le în ordine descrescătoare în funcție de rating.

c. Sortați lista de filme în ordine crescătoare după anul de apariție. Pentru filmele cu același
an de apariție, sortați-le în ordine lexicografică crescătoare în funcție de numele filmului.
'''
l=[("Titanic", 9.8, 1900, 'romance'),('Hobbit', 10, 1980, 'fantasy'), ("Starwars", 10, 1950, "scifi")]

a=sorted(l,reverse=True)
a=sorted(a,key=lambda x:-x[1])
print(a)


b=sorted(l,key=lambda x:-x[1])
b=sorted(b,key=lambda x:x[3])
print(b)



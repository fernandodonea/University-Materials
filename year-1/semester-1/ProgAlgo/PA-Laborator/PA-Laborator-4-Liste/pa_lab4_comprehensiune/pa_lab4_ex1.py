#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 23:33:47 2025

@author: fernandodonea
"""
'''
 Se citește o propoziție cu cuvintele separate prin spații (unul sau mai multe). 
 Să se creeze o listă cu cuvintele care încep cu o vocală (folosind și comprehensiune).
'''

prop=input("cititi o propozitie: ").split()

l1=[]
for cuv in prop:
    if cuv[0] in "aeiou":
        l1.append(cuv)
print(l1)


l2=[x for x in input().split() if x[0] in "aeiou"]
print(l2)
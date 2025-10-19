#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 02:09:05 2025

@author: fernandodonea
"""

'''
Se dau două mulțimi cu elementele ordonate crescător (elementele fiecărei mulțimi
se vor da pe o linie separate prin spațiu). Să se determine eficient reuniunea și intersecția
celor două mulțimi (fără a folosi set).
'''
l1=[int(x) for x in input().split()]
l2=[int(x) for x in input().split()]


intersectie=[ x for x in l1 if x in l2]
print(intersectie)

reuniune=[x for x in l1]
temp=[x for x in l2 if x not in l1]
reuniune.extend(temp)
reuniune=sorted(reuniune)
print(reuniune)
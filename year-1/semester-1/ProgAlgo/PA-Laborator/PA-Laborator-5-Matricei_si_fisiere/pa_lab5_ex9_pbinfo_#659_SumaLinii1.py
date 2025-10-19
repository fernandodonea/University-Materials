#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 14:33:01 2025

@author: fernandodonea
"""

'''
Se citesc m, n și o matrice cu m linii și n coloane, elementele unei linii fiind date
pe o linie (elementele unei linii date pe o linie separate cu spațiu). Să se
determine pentru fiecare linie, cea mai mică valoare care se poate obține
adunând elementele de pe linie, cu excepția unuia. (folosind și comprehensiune).
https://www.pbinfo.ro/probleme/659/sumalinii1

3 4
5 5 10 5 
3 9 1 9 
4 10 1 2 
'''

#n,m=[int(x) for x in input().split()]
#a=[[int(x) for x in input().split()] for _ in range(n)]

a=[[5,5,10,5],[3,9,1,9],[4,10,1,2]]

rez=[sum(x)-max(x) for x in a]
print(*rez)



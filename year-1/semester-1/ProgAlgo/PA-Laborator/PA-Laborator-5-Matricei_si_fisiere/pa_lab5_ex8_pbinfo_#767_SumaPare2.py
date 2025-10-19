#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 14:20:50 2025

@author: fernandodonea
"""

'''

Se citesc m, n și o matrice cu m linii și n coloane, elementele unei linii fiind date
pe o linie (elementele unei linii date pe o linie separate cu spațiu). Să se
determine numărul de valori pare din matrice (folosind și comprehensiune)

'''

#n,m=[int(x) for x in input().split()]
#a=[[int(x) for x in input().split()] for _ in range(m)]

a=[
[0, 2, 2, 2],
[6, 8, 8, 10],
[1, 2, 6, 6],
[1, 2, 3, 21]
]

m=len(a)
n=len(a[0])

#varinata comprehensiune


#sau
k=sum([x for line in a for x in line if x%2==0])
print(k)


    
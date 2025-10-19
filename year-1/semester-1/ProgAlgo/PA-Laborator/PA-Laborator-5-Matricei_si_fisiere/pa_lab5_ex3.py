#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 13:15:37 2025

@author: fernandodonea
"""

'''
Se citesc m, n și o matrice cu m linii și n coloane, elementele unei linii fiind date
pe o linie (elementele unei linii date pe o linie separate cu spațiu). Să se creeze o
listă cu maximele de pe fiecare linie (folosind și comprehensiune)
'''

m,n=[int(x) for x in input().split()]
a=[[int(x) for x in input().split()] for _ in range(m)]
print(a)


'afisare matrice'
#afisare mai c++
for i in range(m):
    for j in range(n):
        print(a[i][j],end=' ')
    print()
#afisare mai python
for l in a:
    for x in l:
        print(x,end=" ")
    print()



#%% afisare
ll=[x for l in a for x in l]
print(ll)
#%% suma pe linie
#print(sum[a[0]])

#%%
print(" ".join([str(x) for x in a[0]]))

#%%
print(a[0][::-1])
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:04:46 2025

@author: fernandodonea
"""

'''
Subsecvența de sumă maximă a unui șir: Se dă un șir de numere (în fișier,
separate prin spații). Să se afișeze o subsecvenţă de sumă maximă a șirului
(formată cu elemente consecutive) O(n)

l: 1  -2  3  -1  5  2  -6  1  3
d: 1  -1  3   2  7  9   3  4  5

3 -1 5 2

'''

l=[1,-2,3,-1,5,2,-6,1,3]
n=len(l)
d=[0]*n

start=0
end=0
start_temp=0
d[0]=l[0]

for i in range(1,n):
    if l[i]>l[i]+d[i-1]:
        start_temp=i
        d[i]=l[i]
    else:
        d[i]=l[i]+d[i-1]
    if d[i]>d[end]:
        start=start_temp
        end=i
print(l[start:end+1])



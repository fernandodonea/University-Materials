#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 11:42:58 2025

@author: fernandodonea
"""
'''
Se dă numărul natural n și un șir de n numere naturale. 
Determinați numărul minim de operații necesare pentru a face șirul palindromic. 
Singura operație admisă este înlocuirea a două elemente adiacente cu un element care conține suma lor.

intrare:
4
1 4 5 1
iesire:
1

1 2 2 2 4 2 1
1 2 4 4 2 1

explicatie:
Se adună 4 cu 5 și șirul devine 1 9 1
'''

n=int(input())
l=[int(x) for x in input().split()]

k=0
i=0
j=n-1
while (l[::] != l[::-1]) and (i<j) and (i<n) and (j>1):
    if(l[i]==l[j]):
        i=i+1
        j=j-1
    else:
        if l[i]+l[i+1]==l[j]:
            s=l[i]+l[i+1]
            l[i:i+2]=[s]
            k+=1
            j=j-1
        elif l[j]+l[j-1]==l[i]:
            s=l[j]+l[j-1]
            l[j-1:j+1]=[s]
            k+=1
            i=i+1
        else:
            s=l[i]+l[i+1]
            l[i:i+2]=[s]
            k+=1
print(k)
print(l)
            
            
                
                
                
    
    
    


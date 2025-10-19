#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:08:35 2025

@author: fernandodonea
"""

'''
Într-o anumită zi a săptămânii, toți cei 𝑛
studenți ai Facultății de Informatică sunt prezenți
la cursuri, însă fiecare într-un anumit interval orar de forma [𝑎, 𝑏] 𝑎, 𝑏∈𝑁 𝑎 < 𝑏
, unde și .
Decanul Facultății dorește să convoace o ședință la care să participe toți studenții. Pentru
a-l ajuta, scrieți un program care să determine intervalul orar din ziua respectivă în care
sunt prezenți în Facultate toți studenții.
'''
mini=maxi=0
n=int(input("nr studenti "))
l=[]
for i in range(0,n):
    a,b=input(f"Program student {i+1} ").split()
    a=int(a)
    b=int(b)
    student=[a,b]
    l.append(student)
maxi=l[0][0]
mini=l[0][1]

for student in l:
    if student[0]>maxi:
        maxi=student[0]
    if student[1]<mini:
        mini=student[1]

if maxi>mini:
    print('nu se poate')
else:
    print(maxi,mini)
    
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 08:29:46 2024

@author: maiar
"""

#comprehensiune!!!!
#%%

#%%
#citire lista -- urata
l = input().split()
for i in range(len(l)):
    l[i] = int(l[i])
print(l)
#%%
#citire lista mai frumoasa lol CU COMPREHENSIUNE
l = [int(x) for x in input().split()]
print(l)
#%%
#Exc 4
l = [chr(i) for i in range(ord('a'), ord('z') + 1)]
print(l)
#%%
#Exc 5
n = int(input())
l = [- i if i % 2 == 0 else i for i in range(1, n + 1)]
print(l)
#%%
#Exc 6
l = [10, 3, 5, 7, 9, 11, 23, 20, 14]
ll = [i for i in l if i % 2 != 0]
print(ll)
#%%
#Exc 7
l = [int(x) for x in input().split()]
ll = [l[i] for i in range(len(l)) if i % 2 != 0]
print(ll)
#%%
#Exc 8
l = [2, 4, 1, 7, 5, 1, 8, 10]
ll = [l[i] for i in range(len(l)) if l[i] % 2 == i % 2]
print(ll)
#%%
#Exc 9
#tupluri = liste  are sunt UNMUTABLE
#unmutable = nu pot fi modificate
#se declara in felul urmator: tuple = (10, 20, ...)
l = [1, 2, 3, 4]
ll = [(l[i], l[i + 1]) for i in range(len(l) - 1)]
print(ll)
#%%
#Exc 10
sir = "abcde"
# for i in range(len(sir)):
#     print(sir[i:] + sir[:i])
l = [sir[i:] + sir[:i] for i in range(len(sir))]
print(l)
#%%
#Exc 1
l = [x for x in input().split()]
l = [x for x in l if x[0] in "aeiouAEIOU"]
print(l)
#%%
#Exc 2
l = input()
k = int(input())
ll = [chr(ord(l[i]) + k) if ord('a') <= ord(l[i]) + k <= ord('z') else chr(ord('a') + (k - 1 - ord('z') - ord(l[i]))) for i in  range(len(l))]
print(ll)
#%%
#Exc 3 GRESIT / NETERMINAT
#sir = input()
#l = [p + l[i] if l[i] in "aeiou" else l[i] for i in range[len(sir)]]
#print(l)
#%%
#Exc 12

#METODA 1
# l = [2, 3, 4, 5, 6]
# k = int(input())
# l = l[k:len(l)]
# print(l)

#METODA 2
l = [2, 3, 4, 5, 6]
k = int(input())
ll = [l[i] for i in range(k, len(l))]
print(ll)
#%%
#Exc 13
l = [2, 3, 0, 3, 3, 0, 1, 0]
p1 = -1
p2 = -1
for i in range(len(l)):
    if l[i] == 0 and p1 == -1:
        p1 = i
    elif l[i] == 0 and p2 == -1:
        p2 = i
del l[p1:p2 + 1]
print(l)
#%%
#Exc 14 DE CE E CU -1?????
l = [2, 3, 4, 0, 4, 5, 0]
for i in range(len(l) - 1):
    if l[i] == 0:
        del l[i]
print(l)
#%%
#Exc 15
l = [int(x) for x in input().split()]
k = int(input())

#%%
#Exc 16
l = [int(x) for x in input().split()]
i = 0
while i < len(l) - 1 :
    if l[i] == l[i + 1]:
        del l[i + 1]
    else:
        i = i + 1 
print(l)
#%%
#Exc 17
l = [int(x) for x in input().split()]
i = 0
while i < len(l):
    if l[i] < 0:
        l.insert(i + 1, 0)
        i = i + 2
    else:
        i = i + 1
print(l)
#%%
#Exc 18
n = int(input())
l = []
for i in range(n + 1):
    ok = 1
    if i <= 1:
        ok = 0
    if i % 2 == 0:
        ok = 0
    for j in range(3, i // 2, 2):
        if i % j == 0:
            ok = 0
    if ok == 1:
        l.append(i)
print(l)
#%%
#Exc 19 DE INTREBAT PROFA LOL ??? VECTOR DE FRECVENTA??

#%%
#Exc 20
l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
i = 0
j = 0
reuniune = []
intersectie = []
while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
        reuniune.append(l1[i])
        i = i + 1
    elif l2[j] < l1[i]:
        reuniune.append(l2[j])
        j = j + 1
    else:
        reuniune.append(l1[i])
        i = i + 1 
        j = j + 1 
while i < len(l1):
    reuniune.append(l1[i])
    i = i + 1
while j < len(l2):
    reuniune.append(l2[j])
    j = j + 1 
print(reuniune)
i = 0
j = 0
while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
        i = i + 1
    elif l2[j] < l1[i]:
        j = j + 1
    else:
        intersectie.append(l1[i])
        i = i + 1
        j = j + 1
print(intersectie)
#%%
#Exc 21 GRESIT 
n = int(input())
l = [[1]]
for i in range(1, n):
    for j in range(len(l[i - 1]) + 1):
        x = 0
        if j == 0:
            x = 1
        elif j == i:
            x = 1
        else:
            x = x + l[i - 1][j] + l[i - 1][j - 1]
for i in range(n):
    for j in range(len(l[i])):
        print(l[i][j], end = " ")
    print()
#%%


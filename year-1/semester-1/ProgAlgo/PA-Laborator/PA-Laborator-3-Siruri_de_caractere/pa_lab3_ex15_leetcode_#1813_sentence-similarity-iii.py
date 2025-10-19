#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 23:17:09 2025

@author: fernandodonea
"""

'''
For example,

s1 = "Hello Jane" and s2 = "Hello my name is Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in s1.
s1 = "Frog cool" and s2 = "Frogs are cool" are not similar, since although there is a sentence "s are" inserted into s1, it is not separated from "Frog" by a space.
Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.
'''
s1=input()
s2=input()

a=s1.split(" ")
b=s2.split(" ")

n=len(a)
m=len(b)

if a==b:
    print("Da")
else:
    if n>m:
        k=0
        for i in range(0,n):
            if k==m:
                break
            if a[i]==b[k]:
                k+=1
        if k==m:
            print("Da")
        else:
            print('Nu')
    else:
        k=0
        for i in range(0,m):
            if k==n:
                break
            if b[i]==a[k]:
                k+=1
        if k==n:
            print("Da")
        else:
            print('Nu')
        
                
    

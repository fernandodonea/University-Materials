"""
Recursivitate
"""
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(50))
print(fact(70))
import sys
sys.setrecursionlimit(2000)
print(fact(1090))
ls_nr = [int(x) for x in input().split()]
print("stiva")
stiva = []
for x in ls_nr:
    stiva.append(x)
for i in range(2):
    if len(stiva)>0:
        print(stiva.pop(),end= " ")#extrage ultimul element adaugat
print("\ncoada")
import collections
coada = collections.deque()
for x in ls_nr:
    coada.append(x)
for i in range(2):
    if len(coada) > 0:
        print(coada.popleft(), end=" ") #extrage primul element adaugat
print("\ncoada 2: ")
import queue
coada = queue.Queue()
for x in ls_nr:
    coada.put(x)
for i in range(2):
    if coada.qsize() > 0:
        print(coada.get(), end=" ")#extrage primul element adaugat

print("\ncoada prioritati 1: ")
import heapq

h = [] #un heap este un vector
for x in ls_nr:
    heapq.heappush(h,x)
for i in range(2):
    if len(h) > 0:
        print(heapq.heappop(h),end=" ") #extrage elementul minim

import queue
print("\ncoada prioritati 2: ")
coada = queue.PriorityQueue()
for x in ls_nr:
    coada.put(x)
for i in range(2):
    if coada.qsize() > 0:
        print(coada.get(),end=" ")#extrage elementul minim



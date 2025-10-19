import collections


def citire(nume_fisier):
    f = open(nume_fisier)
    n, m, s = [int(x) for x in f.readline().split()]
    s -= 1
    l = [[] for i in range(n)]
    for linie in f:
    #for i in range(m):
        x, y = [int(a) for a in linie.split()]
        l[x - 1].append(y - 1)
    f.close()
    return n, s, l


def bfs(s):
    c = collections.deque()
    c.append(s)
    d[s] = 0
    viz[s] = 1
    while c:
        x = c.popleft()
        for y in l[x]:
            if viz[y] == 0:
                c.append(y)
                viz[y] = 1
                d[y] = d[x] + 1


n, s, l = citire("bfs.in")
d = [-1] * n
viz = [0] * n
bfs(s)
f = open("bfs.out", "w")
# f.write(" ".join(str(x) for x in d))
for x in d:
    f.write(str(x)+" ")
f.close()
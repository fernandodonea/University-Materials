# PROGRAMARE DINAMICA
# Ex 1 - subsecventa de suma maxima
# algoritmul lui cadan
l = [1 ,-2, 3, -1, 5, 2, -6, 1, 3];
def subsecventaSumaMax(l):
    s = l[0]
    sMax = l[0]
    start = 0 # poz start
    end = 0 # poz end
    tempS = 0 #  pozitia de start temporara
    for i in range(len(l)):
        if s + l[i] > l[i]:
            s += l[i]
        else:
            s = l[i]
            tempS = i
        if s > sMax:
            sMax = s
            start = tempS
            end = i
    return l[start:end + 1] # l[start: end : inc]
print(subsecventaSumaMax(l))
#%%
# a doua solutie 
l = [1 ,-2, 3, -1, 5, 2, -6, 1, 3];
def subsecventaSumaMax2(l):
    d = [0] * len(l)
    d[0] = l[0]
    start = 0
    end = 0
    tempS = 0
    for i in range(1, len(l)):
        if d[i - 1] + l[i] > l[i]:
            d[i] = d[i - 1] + l[i]
        else:
            d[i] = l[i]
            tempS = i
        if d[end] < d[i]:
            start = tempS
            end = i
    return l[start:end + 1]

print(subsecventaSumaMax2(l))
#%%
# Ex 2 - traseu cu suma maxima
a = [[2, 1, 4], [1, 3, 2], [1, 6, 1]]
n, m = len(a), len(a[0])
d = [[0] * m for _ in range(n)]
d[0][0] = a[0][0]
for j in range(1, m):
    d[0][j] = a[0][j] + d[0][j - 1]
for i in range(1, n):
    d[i][0] = a[i][0] + d[i - 1][0]
for i in range(1, n):
    for j in range(1, m):
        d[i][j] = a[i][j] + max(d[i][j - 1], d[i - 1][j])
path = []
i, j = n - 1, m - 1
while i > 0 and j > 0:
    path.append((i + 1, j + 1))
    if d[i - 1][j] >= d[i][j - 1]:
        i = i - 1
    else:
        j = j - 1
while i > 0:
    path.append((i + 1, 1))
    i = i - 1
while j > 0:
    path.append((1, j + 1))
    j = j - 1
path.append((1, 1))
path.reverse()
print(path)
#%%
# Ex 3 - fazan
sir = ['masa', 'carte', 'sac', 'teatru', 'tema', 'rustic', 'sare']
d = {cuv:(1, [cuv]) for cuv in sir}
# se porneste de la coada pt a lua mereu valoarea maxima
for i in range(len(sir)-1, -1, -1):
    for j in range(len(sir)-1, i, -1):
        if (sir[i][-2:]) == sir[j][:2]:
            if d[sir[i]][0] < d[sir[j]][0] + 1:
                d[sir[i]] = (d[sir[j]][0] + 1, [sir[i]] + d[sir[j]][1]) # reinitializez tuplul
print(d)













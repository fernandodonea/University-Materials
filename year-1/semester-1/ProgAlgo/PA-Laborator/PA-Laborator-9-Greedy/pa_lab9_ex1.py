#OBS: Sortarea din Python (fct .sort) foloseste quicksort (complexitate O(nlogn))
#GREEDY - face sortare!!!!!!! 99% din probleme
#Exc 1
def cheie(x):
    return -x[0] #sortam descrescator

fin = open("date.in", 'r')
lines = fin.readlines()
n, p = lines[0].strip().split()
n , p = int(n), int(p)
cuburi = []
cnt = 1
for line in lines[1:]:
    l, c = line.strip().split()
    l, c = int(l), int(c)
    cuburi.append((l, c, cnt))
    cuburi.append((l, c, cnt))
    cnt += 1
    print(cuburi)

cuburi = sorted(cuburi, key = cheie)
solutie = []
suma = 0
for x in cuburi:
    if suma == 0:
        suma += x[0]
        solutie.append(x)
    else:
        if x[1] != solutie[-1][1]:
            suma += x[0]
            solutie.append(x)
print(suma)
    
fin.close()
# Raspunsul la b este NU, solutia u ar fi mers pe posibile dimensiuni egale
#%%
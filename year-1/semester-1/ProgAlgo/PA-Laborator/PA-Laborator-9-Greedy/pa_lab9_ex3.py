#luam fiecare interval si il sortam in functie de coada
def cheie(x):
    return x[1]
fin = open("intervale.txt", "r")
lines = fin.readlines()
intervale = []
for line in lines:
    line = line.strip()
    st, dr = line.split()
    st, dr = int(st), int(dr)
    intervale.append((st, dr))
    intervale = sorted(intervale, key = cheie)
    #sortareaaaaa
#print(intervale)
cuie = []
cui = float('-inf')
for interval in intervale:
    if interval[0] > cui:
        cui = interval[1]
        cuie.append(cui)
print(cuie)
fin.close()
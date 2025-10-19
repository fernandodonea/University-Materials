#Exc 5 - cel cu eureni pbinfo
s = 107
n = 4
crcy = 5
bani = []
for i in range(n, - 1, -1):
    bani.append(crcy ** i)
print(bani)
cnt = 0
i = 0
while s > 0:
    cc = 0
    while s>= bani[i]:
        s = s - bani[i]
        cc += 1
    if cc != 0:
        print(bani[i], cc)
        cnt += cc
    i += 1
print(f"in total s-au folosit pt suma lui Mos Craciun {cnt} bancnote")

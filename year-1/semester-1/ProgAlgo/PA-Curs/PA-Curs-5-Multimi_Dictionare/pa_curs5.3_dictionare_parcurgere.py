d1={"unu":6,"doi":3,"trei":4}
d2={"unu":5,"doi":7,"patru":3}
print(d1.keys())
print(d1.values())
print(d1.items())
#implicit - parcurse cheile
for x in d1:
    print(x,d1[x])
print(sorted(d1))
#d.keys()- operatori cu multimi &,|
#Exp d1, d2- dictionare cu frecv cuv in 2 fisiere
#sa se afiseze cuv din cel doua fisiere reunie cu frecv lor
# sa se afiseze cuv din intersectie cu frec lor
d1={"unu":6,"doi":3,"trei":4}
d2={"unu":5,"doi":7,"patru":3}
d_reunit={k:d1.get(k,0)+d2.get(k,0)  for k in d1.keys()|d2.keys()}
#d_reunit={k:d1[k]+d2[k]  for k in d1.keys()|d2.keys()}
print(d_reunit)
d_intersect={k:min(d1[k],d2[k]) for k in d1.keys()&d2.keys()}
print(d_intersect)
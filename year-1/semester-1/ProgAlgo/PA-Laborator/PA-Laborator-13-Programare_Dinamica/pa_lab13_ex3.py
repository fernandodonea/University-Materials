#Dat un șir de cuvinte formate cu litere mici, să se determine cel mai lung subșir al
#său astfel încât pentru orice două cuvinte consecutive din subșir ultimele două
#litere din primul să coincidă cu primele două litere din cel de al doilea. Exemplu:
#Pentru șirul: seara, carte, teorema, temperatura, rar, mare, arbore cel mai lung
#subşir care verifică cerinţele este - carte, temperatura, rar, arbore O(n2) /O(n)

#masa carte sac teatru tema rustic sare
#folosim dictionare:
#masa: (2,[masa,sare])
#carte: (3,[carte,teatru,rustic])
#sac: (1, [sac])
#teatru: (2, [teatru, rustic)]
#tema: (1, [tema])
#rustic (1, [restuic])
#sare   (1, [sare])

#!!!! INCEPEM DE LA CAPAT LA COADA

cuvinte=['masa', 'carte', 'sac', 'teatru', 'tema', 'rustic', 'sare']
#dictionarul e un fel de matrice de P.D.
d={cuv:(1,[cuv]) for cuv in cuvinte}
print(d)

for i in range(len(cuvinte)-1,-1,-1):
    for j in range(len(cuvinte)-1,i,-1):
        if cuvinte[i][-2:]==cuvinte[j][:2]:
            if d[cuvinte[i]][0]<d[cuvinte[j]][0]+1:
                d[cuvinte[i]]=(d[cuvinte[j]][0]+1,[cuvinte[i]]+d[cuvinte[j]][1])
print(d)





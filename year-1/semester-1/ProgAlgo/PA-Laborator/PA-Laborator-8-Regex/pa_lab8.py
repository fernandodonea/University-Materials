
# Translate si maketrans = un fel de mapare
# ajuta la preucrare string-uri
s = "ana are mere"
tabel = str.maketrans("ae", "xy") #OBS: must have equal lenghts !! a--> x si e --> y !!
s = s.translate(tabel)
print(s)
tabel = str.maketrans("xy", "ae", " ") # OBS: al treilea parametru apare daca e de STERS ceva
s = s.translate(tabel)
print(s)
#%%
s = "ana are mere"
d = {"a" : "gigel", "e" : "ionel"}
tabel = str.maketrans(d)
s = s.translate(tabel)
print(s)
#%%




#Problema REGEX 2
import re

fin = open("log.txt", "r")
lines  = fin.readlines()
d = {}
c = 0
for line in lines:
    line = line.strip()
    if "Automation Task" not in line:
        c += 1
        nume = re.findall(r'^[a-zA-Z ]*', line)[0].strip()
        print(nume)
        logare = re.findall(r"\d{2}\.\d{2}\.\d{4}, \d{2}:\d{2} [AP]M", line)[0].strip() #OBS cand pui [AC] iei A SAU C; pui [a-z] iei a sau b sau c sau.. z
        print(logare)
        if nume not in d:
            d[nume] = [logare]
        else:
            d[nume].append(logare)
print(c)
print(d)
fin.close()
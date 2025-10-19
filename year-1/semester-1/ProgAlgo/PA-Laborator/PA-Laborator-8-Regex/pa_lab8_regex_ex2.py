'''
Fiind dat un fișier log.txt care conține pe fiecare linie anumite acțiuni înregistrate
într-un sistem informatic făcute de utilizatorii care au acces la el sau proceduri rulate
automat fără intervenția utilizatorilor trebuie să:

a. Determinați numărul de acțiuni făcute de utilizatori (i.e. fără proceduri rulate
automat). (în cazul fișierului prezentat ca exemplu programul ar trebui să
afișeze 3).

'''

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
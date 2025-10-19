'''

fin=open("angajati.in",'r')
lines=fin.readlines()
angajati={}
for line in lines:
    line=line.split(" % ")
    nume_angajat=line[0]
    angajati[nume_angajat] = {
        'functie':line[1],
        'salariu':line[2],
        'program_lucru':line[3]
    }
print(angajati)
'''

fin=open("angajati.in",'r')
lines=fin.readlines()
d={}
for line in lines:
    line=line.strip()
    l=line.split(' % ')
    if l[0] not in d:
        d[l[0]]={
            'functie':l[1],
            'salariu':int(l[2]),
            'program':l[3]
        }


def modifica_salariu(d,nume_angajat,salariu_nou):
    "!!! ff important"
    if nume_angajat in d:
        d[nume_angajat]['salariu']='salariu_nou'
        l=[]
        for angajat in d:
            l.append((angajat,d[angajat]['salariu']))
        return l
    return 'nu exits angajatul'


def angajati_funcție(d,functie):
    l=[]
    for angajat in d:
        if d[angajat]['functie']==functie:
            l.append((angajat,d[angajat]['program']))
    return sorted(l)
print(angajati_funcție(d,'Programator'))

#%%
def adauga_angajat(d,nume,functie,salariu,program):
    if nume not in d:
        d[nume]={
            'functie': functie,
            'salariu': salariu,
            'program': program
        }
#%%
from datetime import datetime
def calcul_total(d):
    salariu_total=0
    ore_total=0
    for angajat in d:
        salariu_total+=d[angajat]['salariu']
        ora_i,ora_f=d[angajat]['program'].split()
        ora_i=datetime.strptime(ora_i,"%H:%M")
        ora_f = datetime.strptime(ora_f, "%H:%M")
        minute_i=ora_i.hour*60+ora_i.minute
        minute_f = ora_f.hour * 60 + ora_f.minute
        dif=(minute_f-minute_i)//60
        ore_total+=dif
    return salariu_total//len(d),ore_total
print(calcul_total(d))


fin.close()
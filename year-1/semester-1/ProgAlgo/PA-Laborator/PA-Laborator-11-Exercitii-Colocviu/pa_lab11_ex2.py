# a
def citeste_note_elevi(fisier):
    fin = open(fisier, "r")
    d = {}
    lines = fin.readlines()
    for line in lines:
        line = line.strip()
        idElev, nume, note = line.split(" % ")
        notaR, notaM, notaI = note.split(" ")
        d[idElev] = {
            'nume': nume,
            'note': {'romana': notaR, 'matematica': notaM, 'informatica': notaI}
        }
    return d

#print(citeste_note_elevi("elevi_note.in"))

#b
#print(d)
d = citeste_note_elevi("elevi_note.in")
def sterge_nota_elev(d, id_elev, numeMaterie):
    l = []
    if numeMaterie in d[id_elev]['note']:
        del d[id_elev]['note'][numeMaterie]
    for nota in d[id_elev]['note']:
        l.append(d[id_elev]['note'][nota])
    return l

#id_elev = input()
#materie = input()
#print(sterge_nota_elev(d, '1', 'romana'))
#print(sterge_nota_elev(d, id_elev, materie))
#print(d)

#c
def medie_clasa_materie(d, numeMaterie):
    suma = 0
    nr = 0
    for elev in d:
        nr += 1
        suma += int(d[elev]['note'][numeMaterie])
    return suma / nr

idElev = 0
vectMaterii = []
for elev in d:
    for materie in d[elev]['note']:
        if materie not in vectMaterii:
            vectMaterii.append(materie)
            #gasesc toate materiile posibile
for materie in vectMaterii:
    print(medie_clasa_materie(d, materie))

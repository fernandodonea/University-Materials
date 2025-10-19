'''
Se citește un cuvânt format cu litere mici. Să se înlocuiască fiecare vocală din cuvânt cu
următoarea literă din alfabet. In plus să se șteargă semnele: virgula, punct, două puncte.
'''


s = "ana are mere dar: :nu ,mereu."
import string
litere = string.ascii_lowercase
inlocuit = litere[1:] + 'a'
tabel = str.maketrans(litere, inlocuit, ",.:")
s = s.translate(tabel)
print(s)
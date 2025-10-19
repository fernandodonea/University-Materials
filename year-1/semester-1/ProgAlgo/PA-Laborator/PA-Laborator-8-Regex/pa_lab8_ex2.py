'''
Se citește un cuvânt format cu litere mici. Să se înlocuiască fiecare vocală din cuvânt cu
următoarea literă din alfabet.
'''

s = "ana are mere"
import string
litere = string.ascii_lowercase
#print(litere)
inlocuit = litere[1:] + 'a'
#print(inlocuit)
tabel = str.maketrans(litere, inlocuit)
s = s.translate(tabel)
print(s)
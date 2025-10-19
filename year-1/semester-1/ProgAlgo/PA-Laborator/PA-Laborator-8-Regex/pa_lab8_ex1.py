'''
Se citește un text conținând separatorii uzuali( ,.;:) Sa se înlocuiască toți separatorii cu
spațiu
'''

s = "ce,mai.faci:astazi;domnule?"
tabel = str.maketrans(",.:;", "    ")
s = s.translate(tabel)
print(s)
'''
Se citește o propoziție. Să se înlocuiască fiecare cifră < 5 care apare în text cu denumirea ei
(1-unu, 2-doi, 3- trei, 4 -patru)
'''

d = {"1": "unu", '2': "doi", '3': "trei", '4': "patru"}
s = "daca ai avea 2 cai si 3 mere ai incerca sa le dai 1 la fiecare si ti-ar mai ramane 1 sau ai vrea sa mai iei un mar, sa ai 4 si sa le dau doua mere fiecaruia"
tabel = str.maketrans(d)
s = s.translate(tabel)
print(s)
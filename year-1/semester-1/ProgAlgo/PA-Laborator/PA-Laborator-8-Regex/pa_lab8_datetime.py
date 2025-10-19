from datetime import datetime, timedelta
acum = datetime.now()
end = datetime(2024, 11, 29, 15, 40, 1)
print(acum)
print(end - acum)
#%%
from datetime import datetime
data1 = "28.11.2024 14:30"
dataConv1 = datetime.strptime(data1, '%d.%m.%Y %H:%M')

data2 = "28.11.2024 14:30"
dataConv2 = datetime.strptime(data2, '%d.%m.%Y %H:%M')
if dataConv1 > dataConv2: #merge si cu compararea data1 data 2 dar nu mereu
    print(data1)
else:
    print(data2)
print(dataConv1.weekday())
dataConv2 += timedelta(days = 10)
print(dataConv2)


#%%
from datetime import datetime, timedelta
fin = open("inputEvent.txt", 'r')
lines = fin.readlines()
acum = datetime.now()
for line in lines:
    line = line.strip()
    eveniment, data = line.split(',')
    data = data.strip() #ca sa scp de spatiul ala stupid in plus din fata lmao
    #convertesc data ca sa o pot manipula cu functiile importate (acuma e doar un string)
    dataConv = datetime.strptime(data, "%d-%m-%Y %H:%M")
    dif = (dataConv - acum).days
    dataD = dataConv.strftime("%d/%m/%Y %H:%M") #il converteste in STRING!!
    if dif > 0:
        print(f"{eveniment} - {dataD} - Zile pana la eveniment {dif}")
    else:
        print(f"{eveniment} - {dataD} - Eveniment trecut")
fin.close()
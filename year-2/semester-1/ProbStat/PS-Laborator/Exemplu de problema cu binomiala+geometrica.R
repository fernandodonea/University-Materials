#Se efectueaza 3 extrageri cu revenire dintr-o urna cu 30 de bile albe si 70 de bile negre
#a) Calculati probabilitatea sa extragem 2 bile albe
dbinom(2,3,3/10)
#b) Construiti un vector care intoarce toate probabilitatile variabilei aleatoare X
dbinom(0:3,3,3/10)
#c) Verificati prin simulare reuzultatul de la a)

y <- rbinom(10^6,3,3/10)
prob_emp <- length(y[y==2])/10^6
#d)Probabilitatea sa obtin o bila alba la a treia extragere
#Aici folosim repartitia geometrica
#In R se numara esecurile pana la primul succes, nu incercarile!!!
dgeom(2,3/10)
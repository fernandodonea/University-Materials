


library(probs)


#Tema:
# 1) Folosind pachetul prob creati obiectul moneda5 ce contine toate rezultatele posibile pe care le putem obtine
#la aruncarea succesiva de 5 ori a unei monede. Folosind selectia intr-un dataframe determinati urmatoarele
#probabilitati:
#a)Aparitia secventei HHTHH
#b)Aparitia secventei THHHT
#c)Numarul de aparitii "H" sa fie mai mare ca numarul de aparitii "T"



moneda5 <- tosscoin(5)

# a)
probHHTHH <- sum( (moneda5[,1]=='H') & (moneda5[,2]=='H') & (moneda5[,3]=='T') & (moneda5[,4]=='H') & (moneda5[,5]=='H') )/nrow(moneda5)
#0.03125


# b)
probTHHHT <- sum( (moneda5[,1]=='T') & (moneda5[,2]=='H') & (moneda5[,3]=='H') & (moneda5[,4]=='H') & (moneda5[,5]=='T') )/nrow(moneda5)
#0.03125


# c) 
prob_H_mare_decat_T <- sum(rowSums(moneda5=='H')>rowSums(moneda5=='T'))/nrow(moneda5)
#0.5







#--------------------------------------------------------------------------------



#Tema:
#Calculati probabilitatea:
#a) Sa extrag cate o bila din fiecare culoare(cu revenire/fara revenire)
#b)Sa extrag mai multe bile rosii decat albastre
#c) Sa extrag doar bile verzi
#d) Sa extrag prima bila rosie si celelalte doua de aceeasi culoare


Urn <- rep(c("Red","Green","Blue"),c(5,3,8))
urnsamples(x=Urn,size=1)
urnsamples(x=Urn,size=2,replace=TRUE)
urnsamples(x=Urn,size=2,replace=FALSE)


urna_revenire = urnsamples(x=Urn, size=3, replace=TRUE)
urna_fara = urnsamples(x=Urn, size=3, replace=FALSE)
n_revenire = nrow(urna_revenire)
n_fara = nrow(urna_fara)

# a)
fiecare_cul_revenire <-sum ( 
    (rowSums(urna_revenire=="Red")==1) &
    (rowSums(urna_revenire=="Green")==1) &
    (rowSums(urna_revenire=="Blue")==1)
  )/n_revenire
#0.1470588

fiecare_cul_fara <-sum ( 
  (rowSums(urna_fara=="Red")==1) &
    (rowSums(urna_fara=="Green")==1) &
    (rowSums(urna_fara=="Blue")==1)
)/n_fara
#0.2142857



# b)
rosii_mult_decat_albastre_revenire <- sum(
  (rowSums(urna_revenire=='Red')) > (rowSums(urna_revenire=='Blue'))
)/n_revenire
#0.2818627

rosii_mult_decat_albastre_fara <- sum(
  (rowSums(urna_fara=='Red')) > (rowSums(urna_fara=='Blue'))
)/n_fara
#0.2410714


# c)
doar_verzi_fara <- sum(rowSums(urna_fara=='Green')==3)/n_fara
#0.001785714

doar_verzi_revenire <- sum(rowSums(urna_revenire=='Green')==3)/n_revenire
#0.0122549


# d)

prima_rosie_restu_egale_fara = sum (
  (urna_fara[,1]=='Red') & (urna_fara[,2]==urna_fara[,3])
)/n_fara
#0.2946429

prima_rosie_restu_egale_revenire = sum (
  (urna_revenire[,1]=='Red') & (urna_revenire[,2]==urna_revenire[,3])
)/n_revenire
#0.3002451




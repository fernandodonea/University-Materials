#Aplicatii(folosim pachetul prob)

#A. Definirea unui spatiu de probabilitate: functia probspace
library(probs)


# probabilitate empericia - cea obtinuta in urma repetarii experimentului de mai multe ori
# pentru n tinzand la infinit (adica suficient de mare) prob_emp este foarte aproape de cea teoretica


" matrice = un vector de vectori
 data frame = o lista de vectori -> motivatie: 
 
  omogen pe coloana
  eterogen pe linie
"
omega2 <- rolldie(2)
"
  x1 si x2 ->aliasuri
"
omega2$X1 #intoarce un vector 
omega2[,1] #vigula separii indicii liniilor si coloanelor; intoarce prima coloana;


# Calculul probabilitatii teoretice
"
  - un fel de brute force
  - vreau ca la aruncarea a 2 zaruri vreau sa obtin valori mai mici decat 3
  1,1 1,2 1,3 2,1 2,2, 2,3, 3,1 3,2 3,3
"
sum(omega2[,1]<=3)
length(omega2) # afiseaza lungimea 2 deoarece data frame ul este bidimensional
nrow(omega2)
probt <- sum(omega2[,1]<=3)/nrow(omega2)




# Probabilitatea empirira

# repetam experimentul de a arunca zarul de n ori 
# si apoi numaram de cate ori din cele n incercari am obtinut conditia ceruta


n=10
sample(rolldie(2),n,replace=T)

#TEMA




outcomes <- rolldie(3)
prob_space <- prnb?pace(outcomes)
print(prob_space)

#B. Functia Prob() pentru calculul unui eveniment specific sau conditionat
S <- cards(makespace = TRUE)
Prob(S, suit == "Heart")
Prob(S, rank %in% c(7,8,9), given = suit == "Heart")

#C. Functia sim() pentru simularea unui experiment in baza spatiului de probabilitate definit
? <- cards(makespace = TRUE)
sim(S, ntrials = 5)

S <- rolldie(1, makespace = TRUE)
sim_results <- sim(S, ntrials = 100)
table(sim_results$X1) / 100


#D. Experimente cu urne: functia urnsamples()

urn <- a(9- 2, 3)
samples <- urnsamples(urn, size = 2, replace = FALSE, ordered = TRUE)
print(samples)

urn <- c(1, 2, 3, 4, 5)
samples <- urnsamples(urn, size = 3, replace = FALSE, ordered = FALSE)
print(samples)


#E. rolldie() pentru aruncarea unui zar.
#tosscoin() pentru aruncarea unei monede.
#cards() pentru un pachet standard de cărți.
#roulette() pentru roata ruletei (versiuni EU și SUA)

#F. Probabilitati conditionate
S <- rolldie(2, makespace = TRUE)
Prob(S, X1 + X2 > 8, given = X1 %% 2 == 0)



#G. Operatori de algebra pe multimi
A <- subset(S, X1 + X2 == 7)
B <- subset(S, (X1 + X2) %% 2 == 0)
event_union <- union(A, B)
Prob(event_union)

S <- rolldie(2, makespace = TRUE)
# Definire evenimente
A <- subset(S, X1 + X2 == 7)  # Suma 7
B <- subset(S, X1 == 4)        # Primul zar arată 4
# Operatori de mulțimi
reuniune <- union(A, B)        # A ∪ B
intersectie <- intersect(A, B) # A ∩ B
diferenta <- setdiff(A, B)     # A \ B
# Probabilități
Prob(reuniune)     # 0.1944444 [5]
Prob(intersectie)  # 0.02777778 [1]

S <- cards(makespace = TRUE)
A <- subset(S, suit == "Heart")    # Inimă roșie
B <- subset(S, rank %in% 7:9)      # Cărți 7-9
# Calcularea P(A ∪ B)
prob_reuniune <- Prob(union(A, B))  # 0.3653846 [4]

#Teorema lui DeMorgan
ts3(<- tosscoin(2, makespace = TRUE)
A <- subset(toss, toss1 == "H")     # Cap pe prima aruncare
B <- subset(toss, toss2 == "T")     # Pajură pe a doua

# Verificare: ¬(A∨B) = ¬A∧¬B
left <- setdiff(toss, union(A, B))
right <- intersect(setdiff(toss, A), setdiff(toss, B))
setequal(left, right)  # TRUE [1][5]

#Diagrame Venn probabilistice
S <- rolldie(3)
A <- subset(S, X1 > 4)
B <- subset(S, X2 %% 2 == 0)
C <- subset(S, X3 < 3)

# Calcularea P(A ∩ B ∩ C)
prob_ABC <- Prob(intersect(intersect(A, B), C))  # 0.02777778 [2]


#Partitii ale spatiului de probabilitate
S <- urnsamples(1:5, size=2, replace=FALSE, ordered=TRUE)
A <- subset(S, X1 == 3)
B <- subset(S, X2 == 3)
# Verificare P(A∪B) = P(A) + P(B) - P(A∩B)
PA <- Prob(A)       # 0.2
PB <- Prob(B)       # 0.2
PAB <- Prob(intersect(A, B)) # 0.05
PA + PB - PAB       # 0.35 [5]


#H. Modelarea de probabilitati particularizate
outcomes <- rolldie(1)
probs <- c(rep(1/10, 5), 5/10) # Probabilități personalizate
biased_space <- probspace(outcomes, probs = probs)
print(biased_space)

#I. Analiza jocurilor de noroc: modelarea unei rulete europene
roulette_space <- roulette(european=TRUE, makespace = TRUE)
Prob(roulette_space, num %in% c(17, "0"))

#Aplicatii
#1. Aruncarea cu moneda

t3 <- tosscoin(3)
str(t3)
t3$do3{2
t3[1,]
t3[,1]
#Se arunca o moneda de 3 ori si vrem probabilitatea de aparitie cel putin de 2 ori a H

#Se arunca o moneda o data si vrem probabilitatea de aparitie a H
omega1 <- tosscoin(1)
sum(omega1=='H')/nrow(omega1)

#Revenim la problema cu 3 aruncari
omega3 <- tosscoin(3)
sum(rowSums(omega3=='H')>=2)/nrow(omega3)

#Calculati probabilitatea de aparitie a secventei TT la aruncarea monedei de 3 ori

probTT31 <- (sum((omega3[,1] == 'T') & (omega3[,2] == 'T')) + sum((omega3[,2] == 'T') & (omega3[,3] == 'T')))/ nrow(omega3)

#Q: Calculati probabilitatea de aparitie a secventei TT la aruncarea monedei de 5 ori


#Probabiliatea ca din 3 aruncari sa apara capul cel putin o data
#Q: Comentati urmatoarele alternative de cod: pe care o preferati si de ce?

omega3 <- tosscoin(3)
sum(omega3=="H")/nrow(omega3) #Asa NU!
#SAU
sum(omega3[,1]=="H"|omega3[,2]=="H"|omega3[,3]=="H")/nrow(omega3)
#Alta varianta
sum(rowSums(omega3=='H')>0)/nrow(omega3)

#Arunc o moneda de 11 ori si vreau probabilitatea sa obtin cap de 6 ori
omega11 <- tosscoin(11)
sum(rowSums(omega11=="H")==6)/nrow(omega11)
choose(11,6)*1/2^11
dbinom(6,11,0.5)

#Arunc o moneda de 3 ori si vreau probabilitatea de a obtine secventa HH
omega3$toss1
omega3[,1]
omega3[6:8,1:2]
omega3[,-2]
o12 <- omega3[(omega3['toss1']=='H')&(omega3['toss2']=='H'),]
o23 <- omega3[(omega3['toss2']=='H')&(omega3['toss3']=='H'),]

#Determinati probabilitatea ca din 7 aruncari sa obtin 5 H
omega7 <- tosscoin(7)
sum(rowSums(omega7=='H')==5)/nrow(omega7)

#Q: Determinati probabilitatea ca din 7 aruncari sa obtinem secventa HH

o7_12 <- omega7[(omega7['toss1']=='H')&(omega7['toss2']=='H'),]
o7_23 <- omega7[(omega7['toss2']=='H')&(omega7['toss3']=='H'),]
o7_34 <- omega7[(omega7['toss3']=='H')&(omega7['toss4']=='H'),]
o7_45 <- omega7[(omega7['toss4']=='H')&(omega7['toss5']=='H'),]
o7_56 <- omega7[(omega7['toss5']=='H')&(omega7['toss6']=='H'),]
o7_78 <- omega7[(omega7['toss6']=='H')&(omega7['toss7']=='H'),]





#2.Aruncarea unui zar
zar2 <- rolldie(2)
str(zar2)
# Determinati probabilitatea ca la aruncarea a doua zaruri sa se obtina suma 7
#Q: Comentati urmatoarele alternative de cod: pe care o preferati si de ce?
sum(zar2[,1]+zar2[,2]==7)
#SAU
h <- sum(rowSums(zar2)==7)/nrow(zar2)

#Alta varianta
t <- table(rowSums(zar2))/nrow(zar2)
str(t)
t$7 #Asa NU!!
t[['7']]

#Care e probabilitatea ca la aruncarea unui zar de 4 ori sa obtinem suma 12?
zar4 <-rolldie(4) 
sum(rowSums(zar4)==12)/nrow(zar4)

#Jocuri de carti
s <- cards(jokers=T)
s[53,2] <- "Heart"

s <- cards()
str(s)
# Determinati probabilitatea de a extrage o carte de Inima

#Q: Comentati urmatoarele alternative de cod: pe care o preferati si de ce?

sum(s['suit']=='Heart')/nrow(s)
#SAU
(table(s["suit"])/nrow(s))[["Heart"]]

#Se extrag aleator dintr-un pachet 15 carti de joc. Calculati probabilitatea sa apara cel putin o carte de inima.
indici <- sample(1:52,15)
simulare_15 <- s[indici,]
(table(simulare_15["suit"])/nrow(simulare_15))[["Heart"]]



##############################################################
#Functiile cbind, rbind
a <- 1:3
b <- 4:6
c <- cbind(a,b)
d <- rbind(a,b)
##############################################################
obis <- rbind(o12,o23)
obis <- unique(obis)

#3.Jocul de carti
s <- cards()
str(s)
#Vreau probabilitatea de a extrage o carte <=7 de inima

####
s[('rank'=='7')&('suit'=='Heart'),]  #Asa NU      #Identificati eroarea 
s[(s$rank==7),]
s[(s$rank==7),(s$suit=="Heart")]   #Asa NU     #Identificati eroarea
p <- s[(s['rank'] == '7') & (s['suit'] == "Heart"),]
nrow(s[((s['rank']) ==  7) & (s['suit'] == "Heart"),]) / nrow(s)



#Vreau sa selectez din omega5 randurile 3 si 7 si coloanele 1,3,4
omega5[c(3,7),c(1,3,4)]
omega5[omega5$toss1=='H',]
omega5[(omega5['toss1']=='H')&(omega5['toss2']=='H'),]

#Q:Determinati probabilitatea ca din 7 aruncari cel putin 3
#sa fie pare

#Evenimente in R (doar in pachetul prob)
#union(A,B) reuniunea
#intersect(A,B) intersectia
#setdiff(A,B) diferenta

#Calculati probabilitatea ca extragand o carte dintr-un pachet cu 
#52 de carti de joc sa obtinem o valoare >=7 si culoare "Spade"
#Reprezentati intai cu evenimente
#Calculati probabilitatea

s['rank'==7]
s[s['rank']==7,]

#Problema
card <- cards()
A <- cardZc?rd['rank'] == '7' |
            card['rank'] == '8' |
            card['rank'] == '9' |
            card['rank'] == '10' |
            card['rank'] == 'J' |
            card['rank'] == 'Q' |
            card['rank'] == 'K' |
            card['rank'] == 'A',]

B <- card[card['suit'] == 'Spade',]
favorabile <- nrow(intersect(A, B))
totale <- nrow(card)
probabilitate <- favorabile / totale

#Tema:
# 1) Folosind pachetul prob creati obiectul moneda5 ce contine toate rezultatele posibile pe care le putem obtine
#la aruncarea succesiva de 5 ori a unei monede. Folosind selectia intr-un dataframe determinati urmatoarele
#probabilitati:
#a)Aparitia secventei HHTHH
#b)Aparitia secventei THHHT
#c)Numarul de aparitii "H" sa fie mai mare ca numarul de aparitii "T"

#Calcul de probabilitati conditionate

S <- rolldie(2,makespace=TRUE)
Prob(S,X1==4,given=(X1+X2==9))
S <- rolldie(3,makespace=TRUE)
Prob(S,X1==4,given=(X1+X2+X3==9))


#Probleme cu extrageri din urna
Urn <- rep(c("Red","Green","Blue"),c(5,3,8))
urnsamples(x=Urn,size=1)
urnsamples(x=Urn,size=2,replace=TRUE)
urnsamples(x=Urn,size=2,replace=FALSE)

#Tema:
#Calculati probabilitatea:
#a) Sa extrag cate o bila din fiecare culoare(cu revenire/fara revenire)
#b)Sa extrag mai multe bile rosii decat albastre
#c) Sa extrag doar bile verzi
#d) Sa extrag prima bila rosie si celelalte doua de aceeasi culoare
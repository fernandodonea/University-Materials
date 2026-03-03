#Repartitii de v.a.


#1.d+nume_repartitie=functie de masa(caz discret)/functia de densitate de probabilitate(caz continuu)
#primul argument reprezinta vectorul de valori in care vrem sa evaluam functia, iar pe urmatoarele pozitii
#sunt parametrii repartitiei, pusi in ordine
#dgeom(x,p)
#dbinom(x,n,p)
#Ce inseamna?
dbinom(3,5,0.4) #Probabilitatea sa reusesc de 3 ori din 5 incercari cu probabilitatea de succes de 0.4
# functia DBINOM modeleaza functia de masa
#P(X=3)

# binomiala modeleaza numarul de succese din n incercari independente si au aceeaasi probabilitate de succes


#schema lui poison nu are o repartitie asociata explicit


dbinom(0:5,5,0.4) #echivalent cu c(dbinom(0,5,0:4),dbinom(1,5,0:4),dbinom(2,5,0:4),dbinom(3,5,0:4),dbinom(4,5,0:4),dbinom(5,5,0:4))

# functia PLOT = deseneaza perechi de puncte
plot(0:10,dbinom(0:10,5,0.4), col="red")
lines(0:10,dbinom(0:10,5,0.4), col="red")



#plot de referinta
plot(0:10,dbinom(0:10,5,0.6),xlim=c(0,5),ylim=c(0,0.6),type="o",pch=19)
for(i in 1:5) 
  {
    points (0:10,dbinom(0:10,5,0.1*i),col=i+1,pch=19)
    lines (0:10,dbinom(0:10,5,0.1*i),col=i+1,pch=19)
  }

# functia LINES =uneste puncte deja desenate; mereu dupa plot, 
#nu face neaparat lini; face un "plot" peste un plot existent

#xlim= capatele pe care le vedem de pe axa OX
#ylim= capatele pe care le vedem de pe axa OY

#type="l" lines
#type="b" 
#type="b" both
#type="o" p



# Problema 1 : Se arunca o mondeda de 15 ori. Care este probabilitatea ca :
# a) Sa pice de 5 ori capul
dbinom(5,15,0.5)
#Calculata de "mana" combinari(15,5)*0.5^5 * 0.5^10
choose(15,5)*0.5^*0.5^10

#b) Sa pice de 15 ori capul
dbinom(15,15,0,5)

#c) Sa pice capul intre 5 si 10 cazuri
sum(dbinom(5:10,15,0.5))


plot(0:10,dbinom(0:10,5,0.9), col="red")
lines(0:10,dbinom(0:10,5,0.9), col="red")

plot(0:10,dbinom(0:10,5,0.1), col="red")
lines(0:10,dbinom(0:10,5,0.1), col="red")

plot(0:100,dbinom(0:100,100,0.4), col="red")
lines(0:100,dbinom(0:100,100,0.4), col="red")


#dexp(x,lambda)
dexp(3,1) #NU mai e o probabilitate
t <- seq(0.001,10,0.001)
plot(t,dexp(t,1),ylim=c(0,0.05))
plot(t,dexp(t,5))
lines(t,dexp(t,1/2), col="red")
lines(t,dexp(t,1),col="blue")

# p de la probability

#2. p+nume_repartitie=functia de repartitie
    ##primul argument reprezinta vectorul de valori in care vrem sa evaluam functia, iar pe urmatoarele pozitii
#sunt parametrii repartitiei, pusi in ordine
 #  pbinom(x,n,p)
   #P(X<=x)
   pbinom(3,5,0.4) #Probabilitatea sa obtinem cel mult 3 succese din 5 incercari cu probabilitatea de succes de 0.4
   t <- seq(0,8,0.001)
   plot(t,pbinom(t,5,0.5),pch=20,cex=0.5)
   for(i in 2:4)
   {
     points(t,pbinom(t, 5, 0.1*i),pch=20,cex=0.5,col=i)
   }
   
   plot(t,pexp(t,1))
   lines(t,pexp(t,1/2), col="red")
   lines(t,pexp(t,5),col="blue")
   
   
   #3. r+nume_repartitie=genereaza valori din acel tip de repartitie
 #  rbinom(nr,n,p)
   #nr-numarul de valori pe care le vrem generate
   
   rbinom(3,5,0.4) # genereaza 3 valori dintr-o v.a. repartizata binomial cu parametrii 5 si 0.4
   y <- rbinom(10^6,5,0.4) 
   hist(y) #histograma coincide cu functia de masa
   
   rexp(3,1) # genereaza 3 valori dintr-o v.a. repartizata exponential de parametru 1
   y1 <-rexp(10^6,1)
   hist(y1,freq=F)
   t <- seq(0.001,8,0.001)
   lines(t,dexp(t,1),col="magenta")
   #daca generez un esantion mic, potrivirea nu mai e la fel de spectaculoasa
   y2 <-rexp(100,1)
   hist(y2,freq=F)
   t <- seq(0.001,8,0.001)
   lines(t,dexp(t,1),col="magenta")
   
   
   #4. q+nume_repartitie = quantila
   #q de la functia quantila = imi intoarce fix inversa (cand func e bijectiva) si intoarce valori cand nu e
   qbinom(0.9,5,0.4)
   #pentru ce valoarea a lui x avem probabilitate mai mare de 0.2 din 5 incercari cu prob 0.4
   dbinom(0:5,5,0.4)
   
   #Reprezentari grafice de functii
   #Functia densitate de probabilitate a repartitiei normale
   t <- seq(-6,6,0.001)
   plot(t,dnorm(t,0,1))  #CLOPOTUL LUI GAUSS
   # aceasta repartitie este simetrica fata de medie
   
   plot(t,dexp(t,2),ylim=c(0,0.))
   #ATENTIE: IN R parametrii normalei sunt media si abaterea medie standard
   y <- rnorm(100,0,1)
   
   
   
   #THREE SIGMA RULE
   
   # orice normala, indiferent de parametrii, este centrat in medie
   # sigma = radical din dispersie
   
   # impact: suportul normalei este tot R-ul dar valorile sunt concentrate in [miu-3sigma, miu+3sigma]
   
   #RNORM simuleaza valori 
   
   
   poz <- y[y>0]
   prob_nr_poz <- length(poz)/10^2
   neg <- y[y<0]
   prob_nr_neg <- length(neg)/10^2
   
   y <- rnorm(1000000,0,1)
   
   # dintr-un interval de 1 milion de valori, cate se afla in intervalul [miu-3sigma, miu+3sigma]
   length(y[(y>-3)&(y<3)])
   
   10^6-length(y[(y>-3)&(y<3)]) # valori in afara intervalului 
  
   lines(t,dnorm(t,0,1))
   plot(t,dnorm(t,3,1),col="magenta",xlim=c(-8,8),ylim=c(0,1))
   lines(t,dnorm(t,3,4), col=2)
   lines(t,dnorm(t,3,0.5), col=3)
   lines(t,dnorm(t,3,2), col=5)
   lines(t,dnorm(t,3,0.5),col=1)
   #toate functiile de densitate sunt centrat in jurul aceleiasi valori si 
   # sunt mai aplatizate sau mai cotite in functie de al doilea parametru
   
   z <- rnorm(1000,2,1)
   length(z[z< -2])
   
   plot(t,dnorm(t,0,1),col="magenta",ylim=c(0,1.8))
   for (i in c(0.25,0.5,0.3,0.9,1.3,2)) lines(t,dnorm(t,0,i), col=i*20)
   # toate reprezentarile sunt normale, de medie 0
   # tind asimptotic spre axa OX (nu sunt niciodata zero)
   
   
   
   plot(t,dnorm(t,0,1),col="magenta",ylim=c(0,1.8))
   for (i in c(-2,-1,0,2)) lines(t,dnorm(t,i,1), col=i+3)
   #cea cu magenta este densitatea normalei standard
   # in c ( ) am pus media
   # media translateaza desenul la standa sau la dreapta
   
   
   
   
   
   
   
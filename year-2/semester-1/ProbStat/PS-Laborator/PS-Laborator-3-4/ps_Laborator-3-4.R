# PS Laborator 3-4


# ex 1
# Un pachet de cărți de joc cu 52 de cărți se amestecă și se extrag 5 cărți. Determinați:

n<-10^5
carti <- cards()
# cards() -> salveaza intr-un data frame
#-ev sunt dependente 


# a) Probabilitatea să obținem flush (5 cărți de același fel ex. toate cărțile sunt de inimă)

# ABORDARE CU PROBABILITATEA EMPIRICA


simulare_flush <- replicate(n,
                            {
                              
                              indici <- sample(1:52,5)
                              extragere <- carti[indici,]
                              
                              flush <-sum(extragere$suit[1] ==extragere$suit[2:5])==4
                              
                            })

flush_emp=sum(simulare)/n


# ABORDARE CU PROBABILITATE TEORETICA

flush_teor <- choose(4,1)*choose(13,5)/choose(52,5)


#TEMA
#eficientizare protorip de cod 
#sa dureze mult mai putin
#pachetul prob nu este foarte eficient





#b) Probabilitatea de a obține o pereche(ex. 2 ași)
p1<- choose(13,1)*choose(4,2)*choose(12,3)*choose(4,1)^3/choose(52,5)
p2<-choose(13,1)*choose(4,2)*choose(12,3)*choose(4,1)/choose(52,5)



n=10^6
carti <- cards()
simulare_pair <- replicate(n,
                            {
                              
                              indici <- sample(1:52,5)
                              extragere <- carti[indici,]
                              
                             s <-length(unique(extragere$rank))==4
                              
                            })

pair_emp=sum(simulare_pair)/n


# intermetzo cat face integrala din x^x de la 0 la 1
f<-function(x){
  x^x
}
#FUNCTIILE in R returenaza ultima prelucrare efectuata
y<-integrate(f,0,1)
y$value



# OBS: functia integrate stie sa integreze doar functii de o singura variabila
# daca insa avem o functie cu mai multe variabile, toate mai putin de una, trebuie fixate
# in apelul functiei integrate

f1 <- function (x,a){
  x^(a-1)*exp(-x)
}

integrate(f1,0,Inf,a=4)$value
  
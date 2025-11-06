# Tema Laborator ProbStat
# Donea Fernando-Emanuel
# grupa 243



# Calculam probabilitatea empirica si probabilitatea teoretica

# ex 1
# Un pachet de cărți de joc cu 52 de cărți se amestecă și se extrag 5 cărți. Determinați:





#a) Probabilitatea să obținem flush (5 cărți de același fel ex. toate cărțile sunt de inimă)
n <- 10^6
carti <- cards()
simulare_flush <- replicate(n,
                            {
                              
                              indici <- sample(1:52,5)
                              extragere <- carti[indici,]
                              
                              flush <- sum(unique(extragere$suit))==1
                              
                            })

flush_emp <- sum(simulare_flush)/n

flush_teor <- choose(4,1)*choose(13,5)/choose(52,5)


#b) Probabilitatea de a obține o pereche (ex. 2 ași)
n <- 10^5
carti <- cards()
simulare_pair <- replicate(n,
                           {
                             
                             indici <- sample(1:52,5)
                             extragere <- carti[indici,]
                             
                             pair <-length(unique(extragere$rank))==4
                             
                           })

pair_emp <- sum(simulare_pair)/n
pair_teor <- choose(13,1)*choose(4,2) * choose(12,3)*choose(4,1)^3 / choose(52,5)



#c) Probabilitatea de a obține două perechi
n <- 10^5
carti <- cards()
simulare_two_pair <- replicate(n,
                           {
                             
                             indici <- sample(1:52,5)
                             extragere <- carti[indici,]
                             
                             frecvente <- sort(table(extragere$rank), decreasing = T)
                             two_pair <- all( c(2,2,1)==frecvente[1:3] )
                             
                           })

two_pair_emp <- sum(simulare_two_pair)/n
two_pair_teor <- choose(13,2)*choose(4,2)^2*choose(11,1)*choose(4,1)/choose(52,5)


#d) Probabilitatea de a obține un triplet (ex. 3 dame)
n <- 10^5
carti <- cards()
simulare_three_oak <- replicate(n,
                               {
                                 
                                 indici <- sample(1:52,5)
                                 extragere <- carti[indici,]
                                 
                                 frecvente <- sort(table(extragere$rank), decreasing = T)
                                 three_oak <- all( c(3,1,1)==frecvente[1:3] )
                                 
                               })

three_oak_emp <- sum(simulare_three_oak)/n
three_oak_teor <- choose(13,1)*choose(4,3)*choose(12,2)*choose(4,1)^2/choose(52,5)


#e) Probabilitatea de a obține 4 cărți de același tip (ex. 4 dame)
n <- 10^5
carti <- cards()
simulare_four_oak <- replicate(n,
                                {
                                  
                                  indici <- sample(1:52,5)
                                  extragere <- carti[indici,]
                                  four_oak <- sum(unique(extragere$rank))==2
                                
                                })

four_oak_emp <- sum(simulare_four_oak)/n
four_oak_teor <- choose(13,1)*choose(4,4)*choose(12,1)*choose(4,1)/choose(52,5)

#f) Probabilitatea de a obține Black Jack cu primele 2 cărți( adică una din cărți este as
# iar cealaltă este fie un 10, un valet, o damă sau un popă)

n <- 10^5
carti <- cards()
simulare_black_jack <- replicate(n,
                               {
                                 
                                 indici <- sample(1:52,5)
                                 extragere <- carti[indici,]
                                 val_10 = c(10,'K','Q','J')
                                 black_jack <- (extragere$rank[1]=='A' &&  extragere$rank[2]%in%val_10) || 
                                   (extragere$rank[1]%in%val_10 && extragere$rank[2]=='A')
                                 
                               })

black_jack_emp <- sum(simulare_black_jack)/n
black_jack_teor <- choose(4,1)*choose(16,1)/choose(52,2)


#g)Probabilitatea ca nici primele 2 cărți și nici următoarele 2 cărți să nu formeze Black Jack
n <- 10^6
carti <- cards()
simulare_no_black_jack <- replicate(n,
                                 {
                                   
                                   indici <- sample(1:52,5)
                                   extragere <- carti[indici,]
                                   val_10 = c(10,'K','Q','J')
                                   
                                   bj1 <-(extragere$rank[1]=='A' &&  extragere$rank[2]%in%val_10) || 
                                     (extragere$rank[1]%in%val_10 && extragere$rank[2]=='A')
                                   
                                   bj2 <-(extragere$rank[3]=='A' &&  extragere$rank[4]%in%val_10) || 
                                     (extragere$rank[3]%in%val_10 && extragere$rank[4]=='A')
                                   
                                   no_black_jack <- !bj1 && !bj2
                                   
                                 })

no_black_jack_emp <- sum(simulare_no_black_jack)/n

no_black_jack_teor <- 1 - (
  2*choose(4,1)*choose(16,1)/choose(52,2) -
  choose(4,1)*choose(16,1)*choose(3,1)*choose(15,1)/(choose(52,2)*choose(50,2))
)






# ex 2
# Două cărți de joc sunt extrase aleator dintr-un pachet de 52 de cărți. Determinați:

n <- 10^6
carti <- cards()
simulare_doi_asi=replicate(n,{
  
                           
                           indici <-sample(1:52,2)
                           extragere <- carti[indici,]
                           
                           doi_asi <- extragere$rank[1]=='A' && extragere$rank[2]=='A'
})
doi_asi_emp <- sum(simulare_doi_asi)/n
doi_asi_teor <- choose(4,2)/choose(52,2)


#b) Probabilitatea ca cele două cărți să aibă aceeași valoare
n <- 10^5
carti <- cards()
simulare_aceeasi_val <- replicate(n,
                                 {
                                   
                                   indici <- sample(1:52,5)
                                   extragere <- carti[indici,]
                                   aceeasi_val <- extragere$rank[1]==extragere$rank[2]
  
                                   
                                 })

aceeasi_val_emp <- sum(simulare_aceeasi_val)/n
aceeasi_val_teor <- choose(13,1)*choose(4,2)/choose(52,2)

#c) Probabilitatea ca ambele să fie cărti mici(cuprinse ȋntre 2 și 9)
n <- 10^5
carti <- cards()
cm <- c(2:9)
simulare_carti_mici <- replicate(n,
                                  {
                                    
                                    indici <- sample(1:52,5)
                                    extragere <- carti[indici,]
                                    carti_mici <- extragere$rank[1] %in% cm && extragere$rank[2] %in% cm
                                  
                                  })

carti_mici_emp <- sum(simulare_carti_mici)/n
carti_mici_teor <- choose(32,2)/choose(52,2)

#d) Probabilitatea ca prima să aibă o valoare mai mare decȃt a doua
n <- 10^5
carti <- cards()

simulare_prima_mare <- replicate(n,
                                 {
                                   
                                   indici <- sample(1:52,5)
                                   extragere <- carti[indici,]
                                   prima_mare <- extragere$rank[1]>extragere$rank[2]
                                  
                                  
                                   
                                 })

prima_mare_emp <- sum(simulare_prima_mare)/n
prima_mare_teor <- (1-choose(13,1)*choose(4,2)/choose(52,2))/2



#ex 3
# Dintr-un pachet cu 52 de cărți de joc se extrag 13 cărți. Determinați probabilitatea ca:
#a) Un as și un popa de aceeași culoare să se regăsească ȋntre cărțile extrase
n <- 10^5
carti <- cards()

simulare_as_pop <- replicate(n,
                                 {
                                   
                                   indici <- sample(1:52,13)
                                   extragere <- carti[indici,]
                                   as_pop <- 'A' %in% extragere$rank && 'K' %in% extragere$rank
                                    #??
                                   
                                 })

as_pop_emp <- sum(simulare_as_pop)/n

a1 <- choose(4, 1) * choose(50, 11)
a2 <- choose(4, 2) * choose(48, 9)
a3 <- choose(4, 3) * choose(46, 7)
a4 <- choose(4, 4) * choose(44, 5)

as_pop_teor=(a1-a2+a3-a4)/choose(52,13)


# b) Toate cele 4 cărți de același fel pentru cel puțin una din cele 13 valori să se
# regăsească ȋntre cărțile extrase

n <- 10^5
carti <- cards()

simulare_careu_multiplu<- replicate(n,
                             {
                               
                               indici <- sample(1:52,13)
                               extragere <- carti[indici,]
                               careu <- 0
                               fr <- rep(0,13)
                               for ( i in extragere$rank)
                               {
                                   if(i>=2 && i<=9)
                                     fr[i] <- fr[i]+1
                                   else{
                                     if(i=='J')fr[10]<- fr[10]+1
                                     if(i=='Q')fr[11]<-fr[11]+1
                                     if(i=='K')fr[12]<- fr[12]+1
                                     if(i=='A')fr[13]<- fr[13]+1
                                   }
                               }
                               
                             })

careu_multiplu_emp <- sum(simulare_careu_multiplu)/n

un_careu <- choose(13,1)*choose(48,9)
doua_caree <- choose(13,2)*choose(44,5)
trei_caree <- choose(13,3)*choose(40,1)

careu_multiplu_teor <- (un_careu - doua_caree + trei_caree) / choose(52,13)

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


alegem_pereche <- choose(13,1)*choose(4,2)
alegem_3_distincte <- choose(12,3)*choose(4,1)^3

pair_teor <- alegem_pereche * alegem_3_distincte / choose(52,5)



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

alegem_2_perechi <- choose(13,2)*choose(4,2)^2
alegem_o_distincta <- choose(11,1)*choose(4,1)

two_pair_teor <- alegem_2_perechi * alegem_o_distincta / choose(52,5)



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


alegem_triplet <- choose(13,1)*choose(4,3)
alegem_2_distincte <- choose(12,2)*choose(4,1)^2

three_oak_teor <- alegem_triplet * alegem_2_distincte / choose(52,5)



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

alegem_careu <- choose(13,1)*choose(4,4)
alegem_o_distincta <- choose(12,1)*choose(4,1)

four_oak_teor <- alegem_careu * alegem_o_distincta / choose(52,5)



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
val_10 = c(10,'K','Q','J')
simulare_no_black_jack <- replicate(n,
                                 {
                                   
                                   indici <- sample(1:52,5)
                                   extragere <- carti[indici,]
                                   
                                   bj1 <-(extragere$rank[1]=='A' &&  extragere$rank[2]%in%val_10) || 
                                     (extragere$rank[1]%in%val_10 && extragere$rank[2]=='A')
                                   
                                   bj2 <-(extragere$rank[3]=='A' &&  extragere$rank[4]%in%val_10) || 
                                     (extragere$rank[3]%in%val_10 && extragere$rank[4]=='A')
                                   
                                   no_black_jack <- !bj1 && !bj2
                                   
                                 })

no_black_jack_emp <- sum(simulare_no_black_jack)/n

# A = primele 2 bj
# B = urm 2 bj

# P( non A intersectat cu non B) = 1 - P(A U B)
# P (A U B) = P(A) + P(B) - P(A inters B)

alegem_bj <- choose(4,1)*choose(16,1)/choose(52,2) # P(A)/P(B)
alegem_a_doua_bj <- choose(3,1)*choose(15,1)/choose(50,2) # P(A inter B)

alegem_ambele_bj <- alegem_bj * alegem_a_doua_bj

no_black_jack_teor <- 1 - (2*alegem_bj - alegem_ambele_bj))









# ex 2
# Două cărți de joc sunt extrase aleator dintr-un pachet de 52 de cărți. Determinați:

#a) Probabilitatea ca ambele să fie as
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
                                    carti_mici <- (extragere$rank[1] %in% cm) && (extragere$rank[2] %in% cm)
                                  
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

aceeasi_val_teor <- choose(13,1)*choose(4,2)/choose(52,2)
prima_mare_teor <- (1-aceeasi_val_teor)/2









#ex 3
# Dintr-un pachet cu 52 de cărți de joc se extrag 13 cărți. Determinați probabilitatea ca:

#a) Un as și un popa de aceeași culoare să se regăsească ȋntre cărțile extrase
n <- 10^6
carti <- cards()

simulare_as_pop <- replicate(n,
                                 {
                                   
                                   indici <- sample(1:52,13)
                                   extragere <- carti[indici,]
                                   
                                   fr_as=rep(0,4)
                                   fr_pop=rep(0,4)
                                   # 1 - trefla, 2 - diamant, 3-inima, 4-frunza
                                   
                                   
                                   #adaugam in vectori de frecventa asii si popii
                                   for( i in 1:13 )
                                   {
                                     if(extragere$rank[i] =='A')
                                     {
                                       if(extragere$suit[i]=='Club')fr_as[1]<-1;
                                       if(extragere$suit[i]=='Diamond')fr_as[2]<-1;
                                       if(extragere$suit[i]=='Heart')fr_as[3]<-1;
                                       if(extragere$suit[i]=='Spade')fr_as[4]<-1;
                                       
                                     }
                                     if(extragere$rank[i] =='K')
                                     {
                                       if(extragere$suit[i]=='Club')fr_pop[1] <-1;
                                       if(extragere$suit[i]=='Diamond')fr_pop[2]<-1;
                                       if(extragere$suit[i]=='Heart')fr_pop[3]<-1;
                                       if(extragere$suit[i]=='Spade')fr_pop[4]<-1;
                                       
                                     }
                                   }
                                   
                                   as_pop <- FALSE
                                   for(i in 1:4)
                                   {
                                     if(fr_as[i]==1 && fr_pop[i]==1) as_pop <-TRUE
                                     
                                   }
                                   returnValue(as_pop)
                                  
                                   
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
                               
                               # vector de freceventa pentru fiecare rank
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
                               
                               for( i in 1:13)
                               {
                                 if(fr[i]==4) careu <- careu+1
                               }
                               
                               if(careu>0) returnValue(True)
                               else returnValue(False)
                               
                             })

careu_multiplu_emp <- sum(simulare_careu_multiplu)/n


un_careu <- choose(13,1)*choose(48,9)
doua_caree <- choose(13,2)*choose(44,5)
trei_caree <- choose(13,3)*choose(40,1)

# principiul includerii si excluderii =>
careu_multiplu_teor <- (un_careu - doua_caree + trei_caree) / choose(52,13)









# ex 4

# Dintr-un pachet cu 52 de cărți de joc se extrag 5 cărți. Determinați probabilitatea ca
#acestea să conțină cȃte o carte din fiecare culoare(prin culoare ne referim la simbol).

n <- 10^5
carti <- cards()
simulare_all_suits <- replicate(n,
                                 {
                                   
                                   indici <- sample(1:52,5)
                                   extragere <- carti[indici,]
                                   all_suits <- length(unique(extragere$suit))==4
                                   
                                 })

all_suits_emp <- sum(simulare_all_suits)/n


alegem_simbol_2_ori <- choose(13,2)*choose(4,1)
alegem_simbol_o_data <- choose(13,1)

all_suits_teor <- alegem_simbol_2_ori* alegem_simbol_o_data^3 /choose(52,5)









#ex 5
# Dintr-un pachet cu 52 de cărți de joc se extrag 5 cărți. Determinați probabilitatea ca:

#a) Toate cărțile să aibă valori diferite

n <- 10^6
carti <- cards()
simulare_all_rank_dif <- replicate(n,
                                {
                                  
                                  indici <- sample(1:52,5)
                                  extragere <- carti[indici,]
                                  all_rank_dif <- length(unique(extragere$rank))==5
                                  
                                })

all_rank_dif_emp <- sum(simulare_all_rank_dif)/n


all_rank_dif_teor <- choose(13,5)*choose(4,1)^5 / choose(52,5)



#b) Toate cărțile să aibă culori diferite (prin culoare ne referim la simbol)
# nu e posibil???
# 4 culori disp
# extragem 5 carti
# doua varti vor avea aceeasi culoare 









# ex 6
#Se ȋmpart cele 52 de cărți de joc către un număr de jucatori. 

#a) Care este probabilitatea ca a paisprezecea carte să fie un as? 
n <- 10^6
carti <- cards()
simulare_as_14 <- replicate(n,
                                   {
                                     
                                     indici <- sample(1:52,14)
                                     extragere <- carti[indici,]
                                     as_14 <- extragere$rank[14]=='A'
                                     
                                     
                                   })

as_14_emp <- sum(simulare_as_14)/n
as_14_teor <- choose(4,1)/choose(52,1)



#b) Cu ce probabilitate primul as apare la a paisprezecea carte?
n <- 10^6
carti <- cards()
simulare_primul_as_14 <- replicate(n,
                                   {
                                     indici=sample(1:52,14)
                                     extragere <- carti[indici,]
                                     primul_as_14 <- !( 'A'%in% extragere$rank[1:13]) && extragere$rank[14]=='A' 
                                     
                                   })
primul_as_14_emp <- sum(simulare_primul_as_14)/n

alegem_non_asi <- choose(48,13)/choose(52,13)
alegem_as <- choose(4,1)/choose(39,1)
primul_as_14_teor <- alegem_non_asi*alegem_as









#ex 7

# Dintr-un pachet cu 52 de cărți de joc se extrag 5 cărți. Determinați probabilitatea de a
#obține full house(adică 3 cărți de același fel și o pereche).

n <- 10^6
carti <- cards()

simulare_fullhouse <- replicate (n,
                                 {
                                   indici <- sample(1:52,5)
                                   extragere <- carti[indici,]
                                   
                                   frecvente <- sort(table(extragere$rank), decreasing = T)
                                   fullhouse <- all( c(3,2)==frecvente[1:2] )
                                  
                              
                                 })

fullhouse_emp <- sum(simulare_fullhouse)/n

fullhouse_teor <- choose(13,1)*choose(4,3) * choose(12,1)*choose(4,2)/choose(52,5)









#ex 20

# Un zar se aruncă de 4 ori. Cu ce probabilitate valoarea 5 apare cel puțin o dată?

n=10^5

simulare_cel_putin_un_cinci = replicate(n,
                                        {
                                          indici<- sample(1:6,4, replace = TRUE)
                                          cel_putin_un_cinci <- 5 %in% indici
                                        })
zar_cel_putin_un_cinci_emp <- sum(simulare_cel_putin_un_cinci)/n

zar_cel_putin_un_cinci_teor <-1-(5/6)^4









#ex 21

# Se aruncă două zaruri, unul după altul. Care este probabilitatea ca al doilea să arate un
# rezultat mai mare decȃt primul?

n=10^6

simulare_zar_primul_mic = replicate(n,
                                        {
                                          indici<- sample(1:6,2, replace = TRUE)
                                          zar_primul_mic <- indici[1]<indici[2]
                                        })
zar_primul_mic_emp <- sum(simulare_zar_primul_mic)/n

zar_primul_mic_teor <-(1-6/36)/2






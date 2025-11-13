data Fruct
  = Mar String Bool
  | Portocala String Int

--tipuri algebrice 
    --tip suma  (ideea de sau)
        -- Mar sau Portocala
    --tip produs (ideea de si)
        -- String si Bool pentru Mar
        -- String si Int pentru Portocala

-- "fruct"= constructor de tip
-- "Mar", "Portocala" = constructori de date


ionatanFaraVierme = Mar "Ionatan" False
goldenCuVierme = Mar "Golden Delicious" True
portocalaSicilia10 = Portocala "Sanguinello" 10
cosFructe = [Mar "Ionatan" False,
                Portocala "Sanguinello" 10,
                Portocala "Valencia" 22,
                Mar "Golden Delicious" True,
                Portocala "Sanguinello" 15,
                Portocala "Moro" 12,
                Portocala "Tarocco" 3,
                Portocala "Moro" 12,
                Portocala "Valencia" 2,
                Mar "Golden Delicious" False,
                Mar "Golden" False,
                Mar "Golden" True]

--ex 1 
--a)

--verifica daca o portocala e de Sicilia
ePortocalaDeSicilia :: Fruct -> Bool
ePortocalaDeSicilia (Mar _ _) = False
ePortocalaDeSicilia (Portocala soi _) = 
    soi == "Tarocco" || soi == "Moro" || soi == "Sanguinello"


-- ePortocalaDeSicilia (Portocala "Moro" 12)
-- ePortocalaDeSicilia (Mar "Ionatan" True)



--b)
--calculează numărul total de felii ale portocalelor de Sicilia dintr-o listă de fructe

numarFelii:: Fruct -> Int
numarFelii (Mar _ _) = 0
numarFelii (Portocala soi felii) = felii

nrFeliiSicilia :: [Fruct] -> Int
nrFeliiSicilia  x =  foldr (\a acc -> if ePortocalaDeSicilia a then acc+ numarFelii a else acc) 0 x

-- nrFeliiSicilia cosFructe ==52


--c) alculează numărul de mere care au viermi dintr-o listă de fructe.

numarViermi :: Fruct -> Int
numarViermi (Portocala _ _) = 0
numarViermi (Mar _ viermi)
    | viermi==True =1
    | otherwise =0


nrMereViermi :: [Fruct] -> Int
nrMereViermi x = sum (map numarViermi x)


-- tipul maybe
-- tip parametric, mai are nevoie de un inca un tip 
-- constructorii de date:
    -- Nothing
    -- Just a
--folosit pentru tratarea erorilor
--exemplu functie care returneaza head-ul unei liste







--ex 2

type NumeA = String
type Rasa = String
data Animal = Pisica NumeA | Caine NumeA Rasa
    deriving Show --ca sa poti afisa tipul 


--a)
-- întoarce "Meow!" pentru pisică și "Woof!" pentru câine.
vorbeste :: Animal -> String
vorbeste (Pisica _) = "Meow!"
vorbeste (Caine _ _) = "Woof!"

-- vorbeste (Pisica "buna")

--b)
--întoarce rasa unui câine dat ca parametru sau Nothing dacă parametrul este o pisică.

-- data Maybe a = Nothing | Just a

rasa :: Animal -> Maybe String
rasa  (Caine _ r) = Just r
rasa (Pisica _) = Nothing

-- rasa (Caine "Gigel" "Bishon")
-- rasa (Pisica "Buna")



--ex 3

data Linie = L [Int]
   deriving Show --ca sa poti afisa tipul respectiv; foloseste clasa SHOW
data Matrice = M [Linie]
   deriving Show

--a) Scrieți o funcție care verifică dacă suma elementelor de pe fiecare linie 
--este egală cu o valoare dată n. Rezolvați cerința folosind foldr.


sumaLinie :: Linie->Int
sumaLinie(L l)= sum l

verifica :: Matrice -> Int -> Bool
verifica (M linii) n = foldr (\linie acc -> (sumaLinie linie == n) && acc) True linii


-- verifica (M[L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]]) 10
-- verifica (M[L[2,20,3], L[4,21], L[2,3,6,8,6], L[8,5,3,9]]) 25


--b) Scrieți o funcție doarPozN care are ca parametri un element de tip Matrice și un număr întreg n, 
-- și care verifică dacă toate liniile de lungime n din matrice au numai elemente strict pozitive.


doarPozitive :: Linie -> Bool
doarPozitive (L x) = foldr (&&) True (map (>0) x)



functiIdk :: Int -> Linie -> Bool
functiIdk n (L x)
    | length x == n = doarPozitive (L x)
    | otherwise = True

doarPozN :: Matrice -> Int -> Bool
doarPozN (M linii) n = foldr (&&) True (map (functiIdk n) linii)

-- doarPozN (M [L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]]) 3 == True



--c) 
-- Definiți predicatul corect care verifică dacă toate liniile dintr-o matrice au aceeași lungime.

aceeasiLungime :: Linie -> Linie -> Bool
aceeasiLungime (L x) (L y) = length x == length y
-- aceeasiLungime  (L [1,2,3]) (L [1,2,6])

corect :: Matrice -> Bool
corect (M []) = True
corect (M linii) = foldr (\linie acc  -> (aceeasiLungime (head linii) linie) && acc) True linii

-- corect (M[L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]]) == False
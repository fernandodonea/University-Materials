-- PF Laborator 10
import Data.List (nub)
import Data.Maybe (fromJust)

--------------------- Logica propozițională ----------------------



--tip algebric pentru "formule"
type Nume = String
data Prop
  = Var Nume
  | F --cazuri de baza 
  | T
  | Not Prop
  | Prop :|: Prop
  | Prop :&: Prop
  | Prop :->: Prop  --ex 8
  | Prop :<->: Prop  --ex 8
  deriving Eq
infixr 2 :|: --infixr asociativa si la stanga si la dreapta
infixr 3 :&: -- & are prioritate mai mare


--ex 1

--a)
pa :: Prop
pa = (Var "P" :|: Var "Q") :&: (Var "P" :&: Var "Q")

--b)
pb :: Prop
pb = (Var "P" :|: Var "Q") :&: (Not( Var "P") :&: Not (Var "Q"))

--c) 
pc :: Prop
pc = (Var "P" :&: (Var "Q" :|: Var "R")) :&: ((Not (Var "P") :|: Not (Var "Q")) :|: ( Not (Var "P") :|: Not (Var "Q")) )



--ex 2
-- Faceți tipul Prop instanță a clasei de tipuri Show, 
-- înlocuind conectorii Not, :|: și :&:
--  cu ~, | și & și folosind direct numele variabilelor în loc de construcția Var nume.


instance Show Prop where
    show (Var n) = n
    show (Not p) = "(~" ++ show p ++ ")"
    show (p1 :|: p2) = "(" ++ show p1 ++ "|" ++ show p2 ++ ")"
    show (p1 :&: p2) = "(" ++ show p1 ++ "&" ++ show p2 ++ ")"
    show (p1 :->: p2)= "(" ++ show p1 ++ "->" ++ show p2 ++")" --ex 8
    show (p1 :<->: p2)= "(" ++ show p1 ++ "<->" ++ show p2 ++")" -- ex 8


test_ShowProp :: Bool
test_ShowProp =
    show (Not (Var "P") :&: Var "Q") == "((~P)&Q)"




--------Evaluarea expresiilor logice------


type Env = [(Nume, Bool)] -- env = evaluarea 
-- nume= alias pentru tipul string
-- asociaza fiecarui nume o valoare de adevar





-- ex 3
-- Definiți o funcție eval care, dată fiind o expresie logică 
-- și un mediu de evaluare, calculează valoarea de adevăr a expresiei.


--lookup clasic-> daca gasea => Just
--         -> daca nu gasea => Nothing

impureLookup :: Eq a => a -> [(a,b)] -> b
impureLookup a = fromJust . lookup a

--FromJust => scoate valoarea din Just a sau eroare altfel




implic :: Bool->Bool->Bool
implic a b
    | a==True && b==False = False
    | otherwise = False

echiv :: Bool->Bool->Bool
echiv a b
    | a==b = True
    | otherwise = False


eval :: Prop -> Env -> Bool
eval F _ = False
eval T _ = True
eval (Var n) env = impureLookup n env
eval (Not p) env = not (eval p env)
eval (p1 :|: p2) env = eval p1 env || eval p2 env
eval (p1 :&: p2) env = eval p1 env && eval p2 env
evaln (p1 :->: q) env = implic (eval p1 env) (eval q env)
evaln (p1 :<->: q) env =  (eval p1 env) `echiv` (eval q env)



test_eval = eval  (Var "P" :|: Var "Q") [("P", True), ("Q", False)] == True



------------------------- Satisfiabilitate ------------------------

-- ex 4
-- Definiți o funcție variabile care colectează lista tuturor variabilelor dintr-o formulă. 
-- Hint: folosiți funcția nub.

-- nub :: Eq a => [a] -> [a]
-- elimina duplicatele dintr-o lista

variabile :: Prop -> [Nume]
variabile F = []
variabile T = []
variabile (Var n) = [n]
variabile (Not p) = variabile p
variabile (p1 :|: p2) = nub (variabile p1 ++ variabile p2)
variabile (p1 :&: p2) = nub (variabile p1 ++ variabile p2)
variabile (p1 :->: p2) = nub (variabile p1 ++ variabile p2)
variabile (p1 :<->: p2) = nub (variabile p1 ++ variabile p2)



test_variabile =
  variabile (Not (Var "P") :&: Var "Q") == ["P", "Q"]





-- ex 5
-- Dată fiind o listă de nume, definiți toate atribuirile
--  de valori de adevăr posibile pentru ea.

--alipim in fata varianta cu true folosind map apoi din nou map cu false

--envs
--primeste n variabile => 2^n

envs :: [Nume] -> [Env]
envs [] = [[]]
envs (x:xs) = map ((x, False):) (envs xs) ++ map ((x, True):) (envs xs)





--ex 6
--Definiți o funcție satisfiabila care, dată fiind o propoziție, verifică dacă aceasta este satisfiabilă.
-- Hint: puteți folosi rezultatele de la exercițiile 4 și 5.


--satisfabila => exista cel putin o valoarea care o face True

satisfiabila :: Prop -> Bool
satisfiabila x = any (\acc -> eval x acc) (envs (variabile x))
--satisfiabila x = any  (eval x)  (envs (variabile x))



test_satisfiabila1 = satisfiabila (Not (Var "P") :&: Var "Q") == True
test_satisfiabila2 = satisfiabila (Not (Var "P") :&: Var "P") == False
    



-- ex 7

--O propoziție este validă dacă se evaluează la True pentru orice interpretare a variabilelor. O formulare echivalentă este aceea că o propoziție este validă dacă negația ei este nesatisfiabilă.
-- Definiți o funcție valida care verifică dacă o propoziție este validă.


--valida => orice valoare
valida :: Prop -> Bool
valida x = all (\acc -> eval x acc) (envs (variabile x))

-- valid x = not (satisfiabila (Not x) )


test_valida1 = valida (Not (Var "P") :&: Var "Q") == False
test_valida2 = valida (Not (Var "P") :|: Var "P") == True




-- ex 9
-- Două propoziții sunt echivalente dacă au mereu aceeași valoare de adevăr, indiferent de valorile variabilelor propoziționale. Scrieți o funcție care verifică dacă două propoziții sunt echivalente.

echivalenta :: Prop -> Prop -> Bool
echivalenta a b = valida ((a :->: b) :&: (b :->: a) )

-- pt ex 9 => daca vrem mai simplu folosind functia valida 
-- valid de echivalenta dintre v1 si v2
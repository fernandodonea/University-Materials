
{-
class Functor f where
fmap : : ( a -> b ) -> f a -> f b
-}



---------------------- Functori ------------------------

-- Functori = tipuri de date pe care putem mapa functii

-- fmap = o functie din clasa functor


--ex 1
-- Scrieți instanțe ale clasei Functor pentru tipurile de date descrise mai jos.

-- definim instante ale clasei functor pentru tipuri definite de noi

newtype Identity a = Identity a
instance Functor Identity where 
    fmap f (Identity a) = Identity (f a)

--exemplu 


data Pair a = Pair a a deriving Show
instance Functor Pair where 
    fmap f(Pair x y)= Pair (f x) (f y)

-- fmap (+1) (Pair 1 2) 

--tipul Identity si Pair depind de un singur parametru de tip

data Constant a b = Constant b --tipul a este ignorat 
instance Functor (Constant a) where 
    fmap f (Constant b) = Constant (f b)



data Two a b = Two a b
instance Functor (Two a) where -- parametrul de tip b este cel care se modifica
    fmap f (Two a b) = Two a (f b)



data Three a b c = Three a b c
instance Functor (Three a b) where 
    fmap f (Three a b c) = Three a b (f c)

data Three' a b = Three' a b b
instance Functor (Three' a) where
    fmap f (Three' a b1 b2) = Three' a (f b1) (f b2)

data Four a b c d = Four a b c d
instance Functor (Four a b c) where 
    fmap f (Four a b c d) = Four a b c (f d)

data Four'' a b = Four'' a a a b
instance Functor (Four'' a) where 
    fmap f (Four'' a1 a2 a3 b) = Four'' a1 a2 a3 (f b)

data Quant a b = Finance | Desk a | Bloor b -- trei constructori de tip
instance Functor (Quant a) where -- parametrul de tip b este cel care se modifica
    fmap f Finance = Finance
    fmap f (Desk a) = Desk a
    fmap f (Bloor b) = Bloor (f b)




-- Hint: e posibil să fie nevoie să adăugați unele constrângeri la definirea instanțelor.

data LiftItOut f a = LiftItOut (f a)
instance Functor f => Functor (LiftItOut f) where -- "instance Functor f =>" acum f e functor prin constrangere
    fmap functie (LiftItOut fa) = LiftItOut (fmap functie fa)
-- aici folosim fmap-ul lui f pentru a aplica functia pe a


data Parappa f g a = DaWrappa (f a) (g a)
instance (Functor f, Functor g) => Functor (Parappa f g) where
    fmap functie (DaWrappa fa ga)= DaWrappa (fmap functie fa) (fmap functie ga)
-- aici folosim fmap-ul lui f si g pentru a aplica functia pe a


data IgnoreOne f g a b = IgnoringSomething (f a) (g b)
instance (Functor g) => Functor (IgnoreOne f g a) where -- nu conteaza f, noua ne trebuie g a (ne intereseaza doar alea care depind de b)
    fmap functie (IgnoringSomething fa gb)= IgnoringSomething fa (fmap functie gb)


data Notorious g o a t = Notorious (g o) (g a) (g t)
instance (Functor g) => Functor (Notorious g o a) where  -- g o a raman nemodificate
    fmap functie (Notorious fo fa ft) = Notorious fo fa (fmap functie ft)

--Un arbore ternar basically
--NoGoat => multimea vida
--OneGoat => o frunza
--MoreGoats => subarbore
data GoatLord a = NoGoat | OneGoat a | MoreGoats (GoatLord a) (GoatLord a) (GoatLord a)
instance Functor GoatLord where 
    fmap functie NoGoat = NoGoat
    fmap functie (OneGoat a) = OneGoat (functie a)
    fmap functie (MoreGoats x y z) = MoreGoats (fmap functie x) (fmap functie y) (fmap functie z)


data TalkToMe a = Halt | Print String a | Read (String -> a)
instance Functor TalkToMe where 
    fmap f Halt = Halt
    fmap f (Print str a) = Print str (f a)
    fmap f (Read g) = Read (f . g) 
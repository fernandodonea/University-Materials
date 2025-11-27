
--- PF Laborator 8




-------------------- FIGURI GEOMETRICE --------------------

data Geo a = Square a | Rectangle a a | Circle a
    deriving Show

class GeoOps g where
  perimeter :: (Floating a) => g a -> a
  area :: (Floating a) =>  g a -> a

--class = un fel de interfata ca in OOP
-- g = tipul colectiei
-- dupa definirea "prototipurilor" putem instantia pentru tipuri de date diferite



--ex 6

--Instanțiați clasa GeoOps pentru tipul de date Geo. 
-- Hint: pentru valoarea pi puteți folosi funcția cu același nume (pi).

instance GeoOps Geo where
    perimeter (Square a) = 4 * a
    perimeter (Rectangle a b) = 2 * (a + b)
    perimeter (Circle r) = 2 * pi * r

    area (Square a) = a * a
    area (Rectangle a b) = a * b
    area (Circle r) = pi * r * r


cerc = Circle 3
arieCerc = area cerc







--ex 7
--Instanțiați clasa Eq pentru tipul de date Geo, 
-- astfel încât două figuri geometrice să fie egale dacă au perimetrul egal.


-- eq clasa care defineste egalitatea
-- trebuie sa implementam operatorul 
instance (Floating a, Eq a) => Eq (Geo a) where
    g1 == g2 = perimeter g1 == perimeter g2








------------------------ PUNCTE PUNCTE -----------------------


data Punct = Pt [Int]

-- ex 4
-- Scrieți o instanță a clasei Show pentru tipul de date Punct,
--  astfel încât lista coordonatelor să fie afișată ca tuplu.


-- Pt [1,2,3]
-- (1, 2, 3)

-- Pt []
-- ()


functieString :: [Int]-> String
functieString [] = ""
functieString [x] = show x -- functia show converteste in string
functieString (x:xs) = show x ++ ", " ++ functieString xs

instance Show Punct where
    show (Pt coordonate) = "(" ++ functieString coordonate ++ ")"






data Arb = Vid | F Int | N Arb Arb
          deriving Show

class ToFromArb a where
    toArb :: a -> Arb
    fromArb :: Arb -> a


-- ex 5
-- Scrieți o instanță a clasei ToFromArb pentru tipul de date Punct
-- astfel încât lista coordonatelor punctului să coincidă cu frontiera arborelui.


-- toArb (Pt [1,2,3])
-- N (F 1) (N (F 2) (N (F 3) Vid))
-- fromArb $ N (F 1) (N (F 2) (N (F 3) Vid)) :: Punct
--  (1,2,3)


---     N
---   /   \
--- F1     N
---      /  \
--      F2   N
--          / \
--        F3  VID


-- din lab7 functia values => intoarce lista valorilor arborelui
valoriArbore :: Arb -> [Int]
valoriArbore Vid =[]
valoriArbore (N left right) = valoriArbore left ++ valoriArbore right
valoriArbore (F x) = [x]


instance ToFromArb Punct where
    toArb (Pt []) = Vid
    toArb (Pt coordonate) = foldr (\x acc -> N (F x) acc) Vid coordonate

    fromArb arbore = Pt (valoriArbore arbore)










--------------------- Clasa Collection ---------------------


-- ex 1
-- Adăugați definiții implicite (folosind celelalte funcții din clasă) 
-- pentru keys, values și fromList.

class Collection c where
  empty :: c key value
  singleton :: key -> value -> c key value
  insert
      :: Ord key
      => key -> value -> c key value -> c key value
  lookup :: Ord key => key -> c key value -> Maybe value
  delete :: Ord key => key -> c key value -> c key value
  keys :: c key value -> [key]
  values :: c key value -> [value]
  toList :: c key value -> [(key, value)]
  fromList :: Ord key => [(key,value)] -> c key value

  keys = map fst . toList
  values = map snd . toList
  fromList = foldr (\(k,v) acc -> insert k v acc) empty
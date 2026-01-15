
{- 
class Functor f where 
     fmap :: (a -> b) -> f a -> f b 
class Functor f => Applicative f where
    pure :: a -> f a
    (<*>) :: f (a -> b) -> f a -> f b

    = 

Just length <*> Just "world"

Just (++" world") <*> Just "hello,"
pure (+) <*> Just 3 <*> Just 5
pure (+) <*> Just 3 <*> Nothing
(++) <$> ["ha","heh"] <*> ["?","!"] 
-- inainte $ era operatorul de aplicare de functii
--acum acesta este operatorul de fmap 
-}



--ex 1
--Se dă tipul de date

data List a = Nil --nil= lista vida
            | Cons a (List a)
        deriving (Eq, Show)

--Scrieți instanțe ale claselor Functor și Applicative pentru constructorul de tip List.

append :: List a -> List a -> List a
append Nil ys = ys
append (Cons x xs) ys = Cons x (append xs ys)

instance Functor List where
    fmap _ Nil = Nil
    fmap f (Cons x xs) = Cons (f x) (fmap f xs)
    
instance Applicative List where
    pure x = Cons x Nil -- luam numarul x si il facem lista
    Nil <*> _ = Nil 
    (Cons f fs) <*> lista = append (fmap f lista) (fs <*> lista)
    -- lista de functii  [f, ......]



f = Cons (+1) (Cons (*2) Nil) --lista de functii
v = Cons 1 (Cons 2 Nil) --lista definita de noi
test1 = (f <*> v) == Cons 2 (Cons 3 (Cons 2 (Cons 4 Nil)))







--ex 2
--Se dă tipul de date

data Dog = Dog {
        name :: String
        , age :: Int
        , weight :: Int
        } deriving (Eq, Show)

-- a) Scrieți funcțiile noEmpty și noNegative care validează un string, respectiv un număr întreg.


noEmpty :: String -> Maybe String 
noEmpty "" = Nothing
noEmpty s = Just s

noNegative :: Int -> Maybe Int
noNegative a 
    | a>0 =Just a
    | otherwise=Nothing


test21 = noEmpty "abc" == Just "abc"
test22 = noNegative (-5) == Nothing 
test23 = noNegative 5 == Just 5 





--b) Scrieți o funcție care construiește un element de tip Dog 
--verificând numele, vârsta și greutatea, folosind funcțiile definite pentru a).



dogFromString :: String -> Int -> Int -> Maybe Dog
dogFromString nume varsta greutate
    | noEmpty nume==Nothing = Nothing
    | noNegative varsta==Nothing = Nothing
    | noNegative greutate==Nothing = Nothing
    | otherwise = Just(Dog {name=nume,age=varsta,weight=greutate})



test24 = dogFromString "Toto" 5 11 == Just (Dog {name = "Toto", age = 5, 
                                                   weight = 11})



--c) Scrieți funcția de la b) folosind fmap și <*>.


--      fmap :: (a -> b) -> f a -> f b 

--        a               b           
-- Dog: String -> (Int -> Int -> Dog)

--                  f
-- noEmpty nume:: Maybe String

--               f a      
--             Maybe String          
-- fmap Dog (noEmpty nume):: Maybe (Int -> (Int->Dog))

--   f      a          b
-- Maybe (Int -> (Int -> Dog))



--     (<*>) :: f (a -> b) -> f a -> f b

-- noNegative varsta:: Maybe Int   - f a


--  fmap Dog (noEmpty nume) <*> noNegative varsta :: Maybe (Int->Dog)

--NoNegative greutate :: Maybe Int
--  f      a      b
-- Maybe ( Int -> Dog)

--       f(a->b)
--  ( fmap Dog (noEmpty nume) <*> noNegative varsta ) <*> NoNegative greutate :: Maybe Dog
            -- Maybe (Int->Dog)



dogFromString' :: String -> Int -> Int -> Maybe Dog
dogFromString' nume varsta greutate =
    fmap Dog (noEmpty nume) <*> noNegative varsta <*> noNegative greutate





-- ex 3 
-- Se dau următoarele tipuri de date:
newtype Name = Name String deriving (Eq, Show)
newtype Address = Address String deriving (Eq, Show)
 
data Person = Person Name Address
    deriving (Eq, Show)

-- a) Implementați o funcție validateLength care validează lungimea unui șir de caractere 
-- – să fie mai mică decât numărul dat ca parametru.

validateLength :: Int -> String -> Maybe String
validateLength n s
    | length(s)<n = Just s
    | otherwise = Nothing   
 
test31 = validateLength 5 "abc" == Just "abc"



-- b) Implementați funcțiile mkName și mkAddress care transformă un șir de caractere 
-- într-un element din tipul de date asociat, validând stringul cu funcția validateLength 
-- (numele trebuie să aibă maxim 25 caractere, iar adresa maxim 100).

mkName :: String -> Maybe Name
mkName s 
    | (validateLength 26 s)==Nothing = Nothing
    | otherwise= Just (Name s)
 
mkAddress :: String -> Maybe Address
mkAddress s 
    | (validateLength 101 s)==Nothing = Nothing
    | otherwise= Just (Address s)

test32 = mkName "Popescu" ==  Just (Name "Popescu")
test33 = mkAddress "Str Academiei" ==  Just (Address "Str Academiei")


-- c) Implementați funcția mkPerson care primește ca argumente două șiruri de caractere 
--și formează un element de tip Person dacă sunt validate condițiile,
-- folosind funcțiile implementate mai sus.


mkPerson :: String -> String -> Maybe Person
mkPerson nume adresa 
    | mkName nume ==Nothing =Nothing
    | mkAddress adresa== Nothing = Nothing
    | otherwise = Just (Person (Name nume) (Address adresa))

test34 = mkPerson "Popescu" "Str Academiei" == Just (Person (Name "Popescu")
                                                    (Address "Str Academiei"))

--d) Implementați funcțiile de la b) și c) folosind fmap și <*>.

--      fmap :: (a -> b) -> f a -> f b 

--                a           b
-- Person :: String -> (String-> Person)

--                    f
--mkAdress nume :: Maybe string









--     (<*>) :: f (a -> b) -> f a -> f b



mkPerso' :: String -> String -> Maybe Person
mkPerso' nume adresa =
    fmap Person (mkName nume) <*> mkAddress adresa
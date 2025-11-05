
-- Programare Functionala - Laborator 4
--30 oct 2025



------------------LISTE------------------------


-- ex 1

a = [ x^2 |x <- [1..10], x `rem` 3 == 2 ] 
--x rem y  => restul impartii lui x la y (pozitiv)
--R: 2^2+3^2+8^2


b = [ (x,y) | x <- [1..5], y <- [x..(x+2)] ]
-- R: (1,1),(1,2),(1,3), (2,2), (2,3), (2,4), ..., (5,5),(5,6),(5,7)


c =[ (x,y) | x <- [1..3], let k = x^2, y <- [1..k] ]
-- R: (1,1),(2,1),(2,2),(2,3),(2,4),...(3,8),(3,9)


d =[ x | x <- "Facultatea de Matematica si Informatica", x `elem` ['A'..'Z'] ]
--elem x lista -> True daca se afla elementul x in lista
--R: "FMI"


e =[ [x..y] | x <- [1..5], y <- [1..5], x < y ]
--R:[1,2],[1,2,3],[1,2,3,4],[2,3,4,5],[2,3],[2,3,4],[2,3,4,5],[3,4],[3,4,5],[4,5]




--ex 2
--lista divizorilor
factori :: Int -> [Int]
factori x = [ y | y<-[1..x], x `mod` y == 0 ]




--ex 3
--verificare prim
prim :: Int -> Bool
prim x =  [1, x] == factori x




--ex 4
--numere prime din intervalul [2..n]
numerePrime :: Int -> [Int]
numerePrime n = [x | x<-[2..n], prim x]





------------------FUNCTIA ZIP-----------------------

-- zip L1 L2 => ia doua liste si returneaza corespondentul de perechi (L1[i],L2[i]) din fiecare lista
a1=[(x,y)| x <- [1..5], y <- [1..3]]
a2= zip [1..5] [1..3]


--ex 5
--zip generalizat pe 3 liste

myzip3 :: [a] -> [b] -> [c] -> [(a,b,c)]
myzip3 [] _ _ = []
myzip3 _ [] _ = []
myzip3 _ _ [] = []
myzip3 (x:xs) (y:ys) (z:zs) = (x,y,z) : myzip3 xs ys zs

-- "_" wildcard in pattern => se potriveste orice valoare in acea pozitie 





------------------ LAMBDA EXPRESII ------------------

--sau functii anonime
-- sintaxa: \argumente -> expresie

f:: Int->Int
f x = x+2


aplica2 :: (a -> a) -> a -> a
aplica2 f x = f (f x)
-- aplica2 f = f . f  ( "." operator de compunere a functiilor)
-- aplica2 = \f x -> f (f x)
-- aplica2 f = \x -> f (f x)




------------------- MAP ---------------------

-- map :: (a -> b) -> [a] -> [b]
-- map f xs = [f x | x <- xs]

-- map f L => aplica functia "F" tuturor elementelor din lista "L"

--exemplu1:
-- map (* 3) [1,3,4]
-- R: [3,9,12]

--exemplu2:
-- map ($ 3 ) [ ( 4 +) , (10 * ) , ( ^ 2) , sqrt ]
-- R:[7.0,30.0,9.0,1.7320508075688772]

aMap = map (\x -> 2 * x) [1..10]
-- functie lambda x=2*x aplicata elementelor de la 1 la 10

bMap = map (1 `elem`) [[2,3], [1,2]]
-- verificam daca 1 se regaseste in [2,3], [1,2]

cMap = map (`elem` [2,3]) [1,3,4,5]
-- verificam daca in lista [2,3] se regasesc [1,3,4,5]



------------------ FILTER ------------------------


-- filter :: (a -> Bool) -> [a] -> [a]
-- filter p xs = [x | x <- xs, p x]


--  filter P L => returneaza lista elementelor din lista "L" care indeplinesc proprietatea
-- (predicatul) "P" 

--exemplu1: 
-- filter (>2) [3,1,4,2,5]
--R:[3,4,5]

--exemplu2:
-- filter odd [3,1,4,2,5]
--R:[3,1,5]



---ex 6
--functie care se returneze primul element dintr-o pereche
first::(a,b)->a
first (a,b)=a


firstEl :: [(a,b)]->[a]
firstEl = map fst --aplica functia "first" tuturor elementelor din lista 


-- firstEl [('a',3),('b',2), ('c',1)]




--ex 7
--suma elementelor din fiecare lista
sumList:: [[Int]] -> [Int]
sumList = map sum 

--sumList [[1,3], [2,4,5], [], [1,3,5,6]]




--ex 8
--elementele pare div 2 iar elementele impare * 2


functiePrel2 :: Int -> Int
functiePrel2 x =
    if even x then x `div` 2
    else x*2

prel2 :: [Int] -> [Int]
prel2 = map functiePrel2

--prel2 [2,4,5,6]



--ex 9
-- intoarce lista sirurilor de caractere care contin un anumit caracter
elem2 :: Char -> [String] -> [String]
elem2 a= filter (elem a) 



--elem2 'a' ["ana","mere","gicu","buna"]




--ex 10
patrateElemImpare :: [Int]->[Int]
patrateElemImpare x = map (^2) ( filter odd x)

--patrateImpare [1,2,3,69,420]


--ex 11
indexImpar :: (Int, Int) -> Bool
indexImpar (a, b) 
    | odd a = True
    | otherwise = False

perechePatrat :: (Int, Int) -> Int
perechePatrat (a,b)=b*b


patratePozImpare :: [Int] -> [Int]
patratePozImpare l = map perechePatrat (filter indexImpar (zip [1..] l))



--ex 12

numaiVocale :: [String]->[String]
numaiVocale = map (filter  ( `elem` "AEIOUaeiou")) 



--ex 10

-- mymap :: (a -> b) -> [a] -> [b]
-- mymap f xs = [f x | x <- xs]

mymap :: (a -> b) -> [a] -> [b]
mymap _ [] = []
mymap f (x:xs) = f x : mymap f xs


-- myfilter :: (a -> Bool) -> [a] -> [a]
-- myfilter p xs = [x | x <- xs, p x]

myfilter :: (a -> Bool) -> [a] -> [a]
myfilter _ [] = []
myfilter p (x:xs)
  | p x==True = x : myfilter p xs
  | otherwise = myfilter p xs

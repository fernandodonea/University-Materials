
-- PF Laborator 5
--6 nov 2025


--ex 1
--suma patratatelor elementelor impare
indiciImp::(Int, Int) -> Bool
indiciImp (a,b)
    | odd a=True
    | otherwise = False

patrat :: (Int, Int) -> Int
patrat (a,b)=b^2

sumPatratImpar :: [Int]->Int
sumPatratImpar l = sum(map patrat (filter indiciImp (zip [1..] l)))


--ex 2
--verif TOATE elem dintr-o lista sunt True folosind foldr
-- TOATE => &&
allTrue :: [Bool] -> Bool
allTrue xs = foldr (&&) True xs


--ex 3
--verifica daca toate elem dintr-o lista de intregi verifica o proprietate
allVerifies :: (Int -> Bool) -> [Int] -> Bool
allVerifies func l= foldr (&&) True (map func l)

--ex 4
--verifica daca exista un elem dintr-o lista de intregi care verifica o proprietate
anyVerifies :: (Int -> Bool) -> [Int] -> Bool
anyVerifies func l= foldr (||) False (map func l)




--ex 5
--redefinrea functiei map si filter folosind foldr

mapFoldr :: (a -> b) -> [a] -> [b]
mapFoldr f lista= foldr (\x l -> f x : l) [] lista

-- "(\x l -> f x : l)"" -> functia
-- variabila "x" din lista, "l"=rezultatul
--aplicam functia "f" lui "x" si adaugam la inceputul listei "l"

--"[]"" =primul element, lista goala

-- "lista" = lista primita ca parametru in map

filterFoldr :: (a -> Bool) -> [a] -> [a]
filterFoldr p lista = foldr (\x l -> if p x then x : l else l) [] lista


--ex 6
--transforma lista de intregi in numar
-- listToInt [2,3,4,5] = 2345
listToInt :: [Integer] -> Integer
listToInt l = foldl (\acc x -> acc*10+x) 0 l


--ex 7
--a)
-- functie care elemina caracterul 'a' din string
rmChar :: Char -> String -> String
rmChar a = foldl (\acc x -> if a /= x then acc ++ [x] else acc) [] 

--rmChar 'a' "idk"
--((([] + i) +d) +k

--b)
--functie care elimina toate carecterele din al doilea string care se afla in primul string
rmCharsRec :: String -> String -> String
rmCharsRec [] l = l
rmCharsRec (x:xs) l = rmCharsRec xs (rmChar x l)


--c) ex b dar folosind FOLDR
rmCharsFold :: String -> String -> String
rmCharsFold chars l = foldr rmChar l chars



--ex 8
--lista in ordine inversa
myReverse :: [Int] -> [Int]
myReverse lista = foldr (\x acc -> [x]++acc) [] lista


--ex 9
-- verif daca un elem apartine unei liste de intregi
myElem :: Int -> [Int] -> Bool
myElem a lista = foldr (||) False (map (==a) lista )


--ex 10
myUnzip :: [(a, b)] -> ([a], [b])
myUnzip liste = foldr (\(x,y) (xs, ys) -> (x:xs,y:ys)) ([],[]) liste

--ex 11
myUnion :: [Int]->[Int]->[Int]
myUnion x y = foldr (\x acc -> if x `elem` acc then acc else x:acc) y x

--ex 12
myIntersect :: [Int]->[Int]->[Int]
myIntersect x y = foldr (\x acc -> if x `elem` y then x:acc else acc) [] x


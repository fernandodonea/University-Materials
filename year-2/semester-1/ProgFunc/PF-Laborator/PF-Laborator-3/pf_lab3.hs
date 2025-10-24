import Data.Char (digitToInt, isDigit)

--PF Laborator 3 
-- 23 oct 2025


--ex 1

--a) lungime lista para
verifL :: [Int] -> Bool
verifL v= even (length v)


--b)ultimele n elemente
takefinal :: [Int] -> Int -> [Int]
takefinal v n =
    if length v > n
        then drop n v
    else v

--pentru char 
takefinalChar :: [Char] -> Int -> [Char]
takefinalChar v n =
    if length v > n
        then drop n v
    else v
    


--c) sterge el de pe pozitia n
remove:: [Int] -> Int -> [Int]
remove v n =
    if length v > n
        then take n v ++ drop (n+1) v
    else v
-- take n v -> returneaza prefixul de lungime n din v 
-- drop n v -> returneaza sufixul din v dupa primele n elemente




--ex 2

--a)n elemente egale cu v
myreplicate :: Int -> Int -> [Int]
myreplicate n v=
    if n>0 then v : replicate (n-1) v
    else []
-- replicate n x => returneaza lista de lungime n, toate elem avand valoarea x

--b)suma imparre
sumImp :: [Int] -> Int
sumImp [] =0
sumImp (v:vsf)
    | odd v = v + sumImp vsf
    | otherwise =0+sumImp vsf


--c)
totalLen :: [String] -> Int
totalLen []=0
totalLen(v:vs)
    | head v=='A' = length v +totalLen vs 
    | otherwise = 0 + totalLen vs
-- head lista => returneaza primul element dintr-o lista
-- string = lista de caractere


vocaleInSir :: String -> Int
vocaleInSir ""=0
vocaleInSir (s:xs)
    | s `elem` "aeiouAEIOU" = 1+ vocaleInSir xs
    | otherwise = vocaleInSir xs

-- x `elem` lista => verifica daca elementul x se afla in lista =>True




-- nrVocale ["sos", "civic", "palton", "desen", "aerisirea"] == 9
--ex 3
nrVocale :: [String] -> Int
nrVocale [] =0
nrVocale(v:vs)
    |  v == reverse v = vocaleInSir v + nrVocale vs
    | otherwise = nrVocale vs



--ex 4
f :: Int -> [Int] -> [Int]
f n []=[]
f n (v:vs)
    | even v = [v,n] ++f n vs 
    | otherwise = [v] ++ f n vs 





semiPareComp :: [Int] -> [Int]
semiPareComp l = [ x `div` 2 | x <- l, even x ]


--ex 5
divizori n = [ d | d <- [1..n], n `mod` d ==0 ]



--ex 6
listadiv :: [Int] -> [[Int]]
listadiv = map divizori
-- map => aplica functia fiecarui element dintr-o lista



--ex 7
--a)
inIntervalRec::Int->Int->[Int]->[Int]
inIntervalRec a b []=[]
inIntervalRec a b (x:xs) 
    | ((a<=x) && (b>=x)) = [x] ++ inIntervalRec a b xs  
    | otherwise = inIntervalRec a b xs

--b)

inIntervalComp::Int->Int->[Int]->[Int]
inIntervalComp a b v=[x | x<-v, x>=a && x<=b]



--ex 8
--a)
pozitiveRec :: [Int] -> Int
pozitiveRec []=0
pozitiveRec (v:vs)
    | v>0 = 1 + pozitiveRec vs
    | otherwise =pozitiveRec vs

--b)
pozitiveComp :: [Int] -> Int
pozitiveComp  v = length (filter (>0) v)
--filter => aplicata unei liste, returneaza o lista cu elemente care satisfac conditia


--ex 9 
pozitiiImpareRec :: Int->[Int] -> [Int]
pozitiiImpareRec n [] =[]
pozitiiImpareRec n (v:vs)
    | odd v = [n] ++ pozitiiImpareRec (n+1) vs
    | otherwise = [] ++ pozitiiImpareRec (n+1) vs


pozitiiImpareComp ::[Int]->[Int]
pozitiiImpareComp v = [i | (i,a)<-zip[1..] v , odd a]
-- zip lista1 lista2 -> returneaza o lista de perechi din ambele liste 
-- exemplu: zip [1,2] ['a','b'] => [(1,'a'),(2,'b')] 


--ex 10
multDigitsRec:: String -> Int
multDigitsRec [] = 1
multDigitsRec (x:xs)
    | isDigit(x) = digitToInt x * multDigitsRec xs
    | otherwise= multDigitsRec xs

--isDigit, digitToInt -> libraria Data.Char 

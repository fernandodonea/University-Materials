--PF Laborator 7
--20 nov 2025


data Expr = Const Int -- integer constant
          | Expr :+: Expr -- addition
          | Expr :*: Expr -- multiplication
           deriving Eq
-- :*: si :+: constructori de date 


data Operation = Add | Mult deriving (Eq, Show)

data Tree = Lf Int -- leaf
          | Node Operation Tree Tree -- branch
           deriving (Eq, Show)

instance Show Expr where
  show (Const x) = show x
  show (e1 :+: e2) = "(" ++ show e1 ++ " + "++ show e2 ++ ")"
  show (e1 :*: e2) = "(" ++ show e1 ++ " * "++ show e2 ++ ")"


-- in frunze avem constantele intregi







--ex 1
--Scrieți o funcție evalExp :: Expr -> Int 
--care evaluează o expresie determinând valoarea acesteia.

exp1 = ((Const 2 :*: Const 3) :+: (Const 0 :*: Const 5))
exp2 = (Const 2 :*: (Const 3 :+: Const 4))
exp3 = (Const 4 :+: (Const 3 :*: Const 3))
exp4 = (((Const 1 :*: Const 2) :*: (Const 3 :+: Const 1)) :*: Const 2)


test11 = evalExp exp1 == 6
test12 = evalExp exp2 == 14
test13 = evalExp exp3 == 13
test14 = evalExp exp4 == 16




evalExp :: Expr -> Int
evalExp (Const x) = x
evalExp (a :+: b) = evalExp a + evalExp b
evalExp (a :*: b) = evalExp a * evalExp b














--ex 2
-- Scrieți o funcție evalArb :: Tree -> Int 
--care evaluează o expresie modelată sub formă de arbore, determinând valoarea acesteia.



arb1 = Node Add (Node Mult (Lf 2) (Lf 3)) (Node Mult (Lf 0)(Lf 5))
--       Add
--      /     \
--    Mult     Mult
--   /  \     /  \
--  2    3   0    5

arb2 = Node Mult (Lf 2) (Node Add (Lf 3)(Lf 4))
--       Mutl
--      /  \
--     2     Add
--          /  \
--         3    4

--(2*(3+4))

arb3 = Node Add (Lf 4) (Node Mult (Lf 3)(Lf 3))
arb4 = Node Mult (Node Mult (Node Mult (Lf 1) (Lf 2)) (Node Add (Lf 3)(Lf 1))) (Lf 2)



test21 = evalArb arb1 == 6
test22 = evalArb arb2 == 14
test23 = evalArb arb3 == 13
test24 = evalArb arb4 == 16



evalArb :: Tree -> Int
evalArb (Lf x) = x
evalArb (Node op nod1 nod2) 
    | op==Add = evalArb nod1 + evalArb nod2
    | op==Mult = evalArb nod1 * evalArb nod2











--ex 3
-- Scrieți o funcție expToArb :: Expr -> Tree 
--care transformă o expresie în arborele corespunzător.


--((2 * 3) + (0 * 5))

--
--
--          Add
--       /         \
--     Mult        Mult
--    /   \         /   \
--   2     3       0     5

expToArb :: Expr -> Tree
expToArb (Const x)= (Lf x)
expToArb (a :+: b) = Node Add (expToArb a) (expToArb b)  
expToArb (a :*: b) = Node Mult (expToArb a) (expToArb b)  





data IntSearchTree value
  = Empty
  | BNode
      (IntSearchTree value)     -- elemente cu cheia mai mica
      Int                       -- cheia elementului
      (Maybe value)             -- valoarea elementului    
      (IntSearchTree value)     -- elemente cu cheia mai mare

-- in cheile mai mici in stanga si cheile mai mari in dreapta
-- simulam stegerea cu Nothing prin Maybe



--ex 4
-- Scrieți o funcție lookup' de căutare a unui element într-un arbore.


abc :: IntSearchTree String
abc = 
    BNode 
        --subarbore stang
        (BNode 
            (BNode Empty 1 (Just "unu") Empty) --frunza
            3 --cheie
            (Just "trei")--valoare 
            (BNode Empty 4 (Just "patru") Empty)
        ) -- frunza


        5 --cheie radacnia 
        (Just "cinci")--val radacina


        --subarbore drept
        (BNode 
            (BNode Empty 6 Nothing Empty) --frunza cu val 6
            8 --cheie
            (Just "opt")--valoare 8
            (BNode Empty 9 (Just "noua") Empty) -- frunza cu val 9
        )

--       5
--     /   \
--   3      8
--  / \    / \
-- 1  4   6   9


lookup' :: Int -> IntSearchTree value -> Maybe value
lookup' x Empty = Nothing
lookup' x (BNode st cheie valoare dr)
    | x == cheie = valoare
    | x < cheie = lookup' x st
    | x > cheie = lookup' x dr

--lookup' 4 abc => Just 4


--ex 5
-- Scrieți o funcție care întoarce lista cheilor nodurilor dintr-un arbore de căutare.

keys ::  IntSearchTree value -> [Int]
keys Empty = []
keys (BNode st cheie valoare dr) = keys st ++ [cheie] ++ keys dr




--ex 6
--Scrieți o funcție care întoarce lista valorilor nodurilor dintr-un arbore de căutare.
values :: IntSearchTree value -> [value]
values Empty =[]
values (BNode st cheie Nothing dr)= values st ++ values dr
values (BNode st cheie (Just valoare) dr)= values st ++ [valoare] ++ values dr








--ex 7
-- Scrieți o funcție de adăugare a unui element într-un arbore de căutare.
insert :: Int -> value -> IntSearchTree value -> IntSearchTree value
insert x val Empty = BNode Empty x (Just val) Empty -- inseram rad
insert x val (BNode st cheie valoare dr)
    |x == cheie  = BNode st cheie (Just val) dr  --
    |x < cheie  = BNode (insert x val st) cheie valoare dr
    |x > cheie  = BNode st cheie valoare (insert x val dr)

-- insert 100 "suta" abc







--ex 8
delete :: Int -> IntSearchTree value -> IntSearchTree value
delete x (BNode st cheie valoare dr)
    |x == cheie  = BNode st cheie Nothing dr  --stergem nodul propriu zis
    |x < cheie  = BNode (delete x  st) cheie valoare dr
    |x > cheie  = BNode st cheie valoare (delete x dr)

-- delete 4 abc





--ex 9
-- Scrieți o funcție care întoarce lista 
-- elementelor dintr-un arbore de căutare. Hint: atenție la Maybe!
toList :: IntSearchTree value -> [(Int, value)]
toList Empty = []
toList (BNode st cheie Nothing dr) = toList st ++ toList dr -- in caz ca nu are valoare
toList (BNode st cheie (Just valoare) dr)= toList st ++ [(cheie, valoare)] ++ toList dr


-- toList abc







--ex 10
-- Scrieți o funcție care să construiască un arbore dintr-o listă de perechi cheie-valoare.

fromList :: [(Int, value)] -> IntSearchTree value 
fromList ((cheie, valoare):xs) = insert cheie valoare (fromList xs)

--fromList [(5,"cinci"), (3,"trei"), (8,"opt"), (1,"unu")]




--ex 11
-- Scrieți o funcție care să producă o reprezentare liniară (șir de caractere) a structurii arborescente de chei (ignorând valorile). 
-- De exemplu, arborele cu rădăcina cu cheia 2, 
-- copilul stâng cu cheia 1 și copilul drept cu cheia 3 
-- ar putea fi reprezentat ca "(1) 2 (3)". Puteți alege și alte reprezentări.


printTree :: IntSearchTree value -> String
printTree Empty = ""
printTree (BNode st cheie valoare dr) = "(" ++ printTree st ++ ")" ++ show cheie ++ "(" ++ printTree dr ++ ")"






-- EXTRA

-- Scrieți o funcție care primește ca parametru un arbore binar de căutare
--  și întoarce arborele echilibrat.



-- to list facuta bine nu e greu sa facem arborele echilibrat
-- arbore binar echilibrat = diferenta de inaltime dintre subarborele stang si cel drept e cel mult 1
-- dintr-o lista de pereche valoare trebuie sa contruim un arbore echilibrat
--vrem ca lista sa fie ordonata
--parcurgem in inordine arborele si obtinem o lista ordonata
-- vrem radacina sa fie elementul din mijloc
-- pe baza listei ordonate, impart lista in jumatate si construim recursiv arborele





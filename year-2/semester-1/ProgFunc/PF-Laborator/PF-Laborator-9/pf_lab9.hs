
data Tree = Empty  -- arbore vid
  | Node Int Tree Tree Tree -- arbore cu valoare de tip Int in radacina
                            -- si 3 fii
  
extree :: Tree
extree = Node 4 (Node 5 Empty Empty Empty) 
                (Node 3 Empty Empty (Node 1 Empty Empty Empty)) Empty

--         4
--     /   |   \
--   5     3   vid
--       / |  \
--    vid vid  1





class ArbInfo t where
  level :: t -> Int -- intoarce inaltimea arborelui; 
                    -- consideram ca un arbore vid are inaltimea 0
  sumval :: t -> Int -- intoarce suma valorilor din arbore
  nrFrunze :: t -> Int -- intoarce nr de frunze al arborelui

-- level extree
-- 3
-- sumval extree
-- 13
-- nrFrunze extree
-- 2



--ex 1
-- Instanțiați clasa următoare pentru tipul Tree.

instance ArbInfo Tree where
    level Empty = 0 
    level (Node _ left mid right) = 1 + max (max (level left) (level right)) (level mid)

    sumval Empty = 0
    sumval (Node val left mid right) = val + sumval left + sumval mid + sumval right

    nrFrunze Empty = 0
    nrFrunze (Node _ left mid right) = 1 + nrFrunze left + nrFrunze right + nrFrunze mid













class Scalar a where
  zero :: a 
  one :: a 
  adds :: a -> a -> a
  mult :: a -> a -> a
  negates :: a -> a
  recips :: a -> a

-- ex 2
-- Instanțiați clasa Scalar folosindu-vă de tipuri primitive (hint: nu uitați, trebuie să fie corpuri comutative).
-- Apoi, considerați clasa de mai jos a vectorilor.



-- OBS: Int nu merge deoarece Z nu este corp 
-- Int este inel ca nu au inversa pentru inmultire

instance Scalar Double where 
    zero = 0.0
    one = 1.0

    adds x y = x + y
    mult x y = x * y
    negates x = mult x (-1.0)
    recips x = 1.0 / x -- inversa pentru inmultire cum ar veni duhhh e corp nu inel








-- ex 3
-- Scrieți două instanțe ale clasei Vector pentru a 
-- reprezenta vectori bidimensionali și tridimensionali.

class (Scalar a) => Vector v a where
  zerov :: v a
  onev :: v a
  addv :: v a -> v a -> v a -- adunare vector
  smult :: a -> v a -> v a  -- inmultire cu scalare
  negatev :: v a -> v a -- negare vector



--vector bidimensional

data Vector2 a = V2 a a deriving Show --V2 onstructor de date 
                                            --deriving ca sa putem afisa

instance Scalar a => Vector Vector2 a where  -- constrangere sa fie scalar
    zerov = V2 zero zero
    onev = V2 one one
    addv (V2 x1 y1) (V2 x2 y2) = V2 (adds x1 x2) (adds y1 y2)
    smult a (V2 x y) = V2 (mult a x) (mult a y)
    negatev (V2 x y) = smult (negates one) (V2 x y)


-- exemplu 
a2= V2 2.0 3.0
b2= V2 4.0 5.0

-- addv a b
-- smult 2.0 a
-- negatev a




-- vector tridimensional
data Vector3 a = V3 a a a deriving (Show, Eq) --V3 onstructor de date
    
instance Scalar a => Vector Vector3 a where 
    zerov = V3 zero zero zero
    onev = V3 one one one

    addv (V3 x1 y1 z1) (V3 x2 y2 z2) = V3 (adds x1 x2) (adds y1 y2) (adds z1 z2)

    smult a (V3 x y z) = V3 (mult a x) (mult a y) (mult a z)

    negatev v = smult (negates one) v


a3 = V3 1.0 2.0 3.0
b3 = V3 4.0 5.0 6.0
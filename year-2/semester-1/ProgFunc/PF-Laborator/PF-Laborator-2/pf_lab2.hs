import Data.List


-- [1..myInt]-> contine elementele de la 1 la myInt
myInt=2323
maxim :: Integer -> Integer -> Integer
maxim x y = if (x > y) then x  else y


maxim2 :: Integer -> Integer -> Integer
maxim2 x y =
    if (x > y)
        then x
        else y

maxim3 :: Integer -> Integer -> Integer -> Integer
maxim3 x y z = maxim2 x (maxim2 y z)

maxim32 :: Integer -> Integer -> Integer -> Integer
maxim32 x y z =
    if x>y
        then if x>z
            then x
            else z
        else if y>z
            then y
            else z



    
        


maxim4 :: Integer -> Integer -> Integer -> Integer -> Integer
maxim4 w x y z =
    let
        a = maxim w x
        b = maxim y z
        c = maxim a b
    in
        c

maxim4verif :: Integer -> Integer -> Integer -> Integer -> Bool
maxim4verif a b c d =
    let
        x = maxim4 a b c d
    in
        x >= a && x >= b && x >= c && x >= d


--ex 6
--a
patrate :: Integer -> Integer -> Integer
patrate a b =
    let 
        c = a*a
    in 
        c + b*b

--b
paritate :: Integer -> String
paritate x = 
    if mod x 2==1 
        then "impar"
        else "par"


--c 
factorial :: Integer -> Integer 
factorial 0 = 1
factorial 1 = 1
factorial n = factorial (n-1)*n

--d 
primmare :: Integer -> Integer -> Bool
primmare x y =
    x>2*y

--e 
maxlist :: [Integer] -> Integer
maxlist [x] = x
maxlist (x:y)= max x (maxlist y)





--ex 7
poly :: Integer -> Integer -> Integer -> Integer -> Integer
poly a b c x =
    a*x*x+b*x+c
--ex 8
eeny :: Integer -> String
eeny x = 
    if even x
        then "eeny"
        else "meeny"

--ex 9

fizzbuzz :: Integer -> String
fizzbuzz x 
    | mod x 3 ==0 && mod x 5==0 ="FIZZBUZZZ"
    | mod x 3==0 = "FIZZ"
    | mod x 5==0 ="BUZZ"
    | otherwise =""

-- ex 10
triboulet :: Integer -> Integer
triboulet 1=1
triboulet 2=1
triboulet 3=1
triboulet n= triboulet(n-1)+triboulet(n-2)+triboulet(n-3)


--ex 11
binomial :: Integer -> Integer -> Integer
binomial _ 0 = 1
binomial 0 _ = 0
binomial n k = binomial (n-1) k + binomial (n-1) k-1

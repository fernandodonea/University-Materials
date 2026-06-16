module Reduction where

import Syntax ( Expr(..), Variable )
import Substitution ( substitute )
import Equivalence ( alphaEquiv )
import Parser (parseFirst, pexpr)

{-| Applies a beta reduction to the leftmost-outermost redex (if present).

Examples:

>>> testBetaRed "(\\x -> x) x"
Right (Just x)

>>> testBetaRed "x x"
Right Nothing

>>> testBetaRed "x (\\x -> x) y"
Right Nothing

>>> testBetaRed "x ((\\x -> x) y)"
Right (Just (x y))

>>> testBetaRed "(\\x -> x) x y"
Right (Just (x y))

>>> testBetaRed "(\\x -> (\\x -> y) x) y"
Right (Just ((\ x -> y) y))

>>> testBetaRed "y (\\x -> (\\x -> y) x)"
Right (Just (y (\ x -> y)))

>>> testBetaRed "(\\x -> y) ((\\z -> z z) (\\w -> w))"
Right (Just y)

>>> testBetaRed "(\\x y -> y) ((\\x -> x x) (\\x -> x x)) (\\z -> z)"
Right (Just ((\ y -> y) (\ z -> z)))

>>> testBetaRed "(\\ y -> y) (\\ z -> z)"
Right (Just (\ z -> z))
-}
betaRed :: Expr -> Maybe Expr
betaRed = undefined

{-| Repeats applying 'betaRed' until reaching a normal form

Examples:

>>> testBetaNormalForm "(\\x -> (\\x -> y) x) y"
Right y

>>> testBetaNormalForm "(\\x -> y) ((\\z -> z z) (\\w -> w))"
Right y

>>> testBetaNormalForm "(\\x y -> y) ((\\x -> x x) (\\x -> x x)) (\\z -> z)"
Right (\ z -> z)

>>> testBetaNormalForm "(\\x -> x y x) (\\z -> z)"
Right (y (\ z -> z))

>>> testBetaNormalForm "(\\x y -> x) y z"
Right y

>>> testBetaNormalForm "(\\z x y -> z y) (v y)"
Right (\ x -> (\ y_1 -> ((v y) y_1)))

>>> testBetaNormalForm "(\\s -> s s) (\\q -> q) (\\q -> q)"
Right (\ q -> q)

3 * 3  = 9
>>> testBetaNormalForm "(\\mul c3 -> mul c3 c3) (\\n m s -> n (m s)) (\\s z -> s (s (s z)))"
Right (\ s -> (\ z -> (s (s (s (s (s (s (s (s (s z)))))))))))
-}
betaNormalForm :: Expr -> Expr
betaNormalForm e = maybe e betaNormalForm (betaRed e)

testBetaRed :: String -> Either String (Maybe Expr)
testBetaRed s = betaRed <$> parseFirst pexpr s

testBetaNormalForm :: String -> Either String Expr
testBetaNormalForm s = betaNormalForm <$> parseFirst pexpr s

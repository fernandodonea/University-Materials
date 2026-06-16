module WeakPre where

import Syntax (Stmt(..), BExpr(..), AExpr, subst, implies, HoareTriple (..))
import Parser ( Parser, parseFirst, hoare )
import Data.Maybe (fromJust)

data Condition = Condition { condition :: BExpr, goals :: Maybe BExpr }
unit :: BExpr -> Condition
unit c = Condition c Nothing

{- | The weakest precondition of a statement with respect to a postcondition. -}
wlp :: Stmt -> Condition -> Condition
wlp SSkip post = post
wlp _ _ = error "not implemented"

{- | The verification condition of a Hoare triple. -}
verificationCondition :: HoareTriple -> BExpr
verificationCondition (HoareTriple pre stmt post) =
    fromJust (Just (pre `implies` condition preStmt) <> goals preStmt)
  where
    preStmt = wlp stmt (unit post)

{- tests

>>> testvc "{true} skip {true}"
! (true) || true

>>> testvc "{true} x := 0 {x == 0}"
! (true) || 0 == 0

>>> testvc "{true} x := 0; x := x + 1 {x == 1}"
! (true) || 0 + 1 == 1

>>> testvc "{!(x <= 0)} y := 0 - x {y <= 0 && ! (y == 0) && ! (y == x)}"
! (! (x <= 0)) || 0 - x <= 0 && ! (0 - x == 0) && ! (0 - x == x)

>>> testvc "{true} if x <= 0 then x := 0 else x := 1 {x == 0 || x == 1}"
! (true) || x <= 0 && (0 == 0 || 0 == 1) || ! (x <= 0) && (1 == 0 || 1 == 1)

>>> testvc "{true} if x <= y then m := y else m := x {(m == x || m == y) && x <= m && y <= m}"
! (true) || x <= y && (y == x || y == y) && x <= y && y <= y || ! (x <= y) && (x == x || x == y) && x <= x && y <= x

>>> testvc "{true} while true do skip invariant true {ultimateQuestionOfLife == 42}"
(! (true) || true) && (! (true && true) || true) && (! (true && ! (true)) || ultimateQuestionOfLife == 42)

>>> testvc "{true} s := 0;\ni := 0;\nwhile i <= n do (\n    s := s + i;\n    i := i + 1\n) invariant i <= n + 1 && 2 * s == i * (i - 1) {2 * s == n * (n + 1)}"
(! (true) || 0 <= n + 1 && 2 * 0 == 0 * (0 - 1)) && (! (i <= n + 1 && 2 * s == i * (i - 1) && i <= n) || i + 1 <= n + 1 && 2 * (s + i) == (i + 1) * (i + 1 - 1)) && (! (i <= n + 1 && 2 * s == i * (i - 1) && ! (i <= n)) || 2 * s == n * (n + 1))

-}

testvc :: String -> BExpr
testvc = test verificationCondition hoare

test :: Show c => (c -> d) -> Parser c -> String -> d
test f p s = f c
  where
    c = case parseFirst p s of
      Right c -> c
      Left err -> error ("parse error: " ++ err)

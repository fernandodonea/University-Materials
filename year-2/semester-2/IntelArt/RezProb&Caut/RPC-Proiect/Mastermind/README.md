# 3.1 Mastermind 
Mastermind este un joc în doi în care unul din jucători creează un cod din 5 piese ordonate — piesele pot fi
de 10 culori, să zicem că le numerotăm de la 0 la 9 pentru simplitudine. Codul poate conține oricâte piese
de aceeași culoare.

Noi trebuie să ghicim această cheie într-un număr minim posibil de încercări. La fiecare încercare, ni se
spune câte dintre piese sunt puse corect, și câte piese sunt de culoare corectă care sunt pe poziție incorectă.

Cerințe:

1. Găsiți și implementați o funcție de fitness cât mai potrivită pentru această cerință, și justificați alegerea
făcută. (1p) Hint: puteți face și “un-fitness”, unde fitness mai mic înseamnă cromozom mai bun.

2. Implementați, folosind algoritmi genetici, un joc complet de Mastermind. Codul adversarului va fi
randomizat. (2p)
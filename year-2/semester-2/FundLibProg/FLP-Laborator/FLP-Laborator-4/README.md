# Unificare

Implementați funcția 'unifyStep' în fișierul [`Unification.hs`](Unification.hs), folosindu-vă de ideile prezentate la curs.

Dacă implementați funcția corect, ar trebui ca rezultatele să fie asemănătoare cu cele din testele incluse ca exemple.

#### *Notă asupra implementării de referință*:

Semnalăm o diferență față de algoritmul din curs: regula de eliminare este implementată doar pentru `x = x`, unde `x` este variabilă.  Se poate observa ușor că această implementare e suficientă, chiar dacă poate nu e la fel de eficientă din punct de vedere al numărului de pași executați.

#### *Constrângere*:

Implementarea trebuie să folosească o noțiune abstractă de substituție ale cărei caracteristici sunt descrise de clasa Haskell `SubstitutionLike`.

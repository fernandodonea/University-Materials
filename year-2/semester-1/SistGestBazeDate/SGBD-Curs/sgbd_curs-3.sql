select *
from employees
where employee_id=197;

-- datele nu se salveaza pe dispozitivul local, ci mereu pes erver
-- de ex sysdate - data serverului

--blocuri PL/SQL


/*
Fie 
A1 3000
A2 3700
A3 3000

User1 mareste salariul la A1 500

User7 mareste salariul lui A1 100

-> nu se poate 





Cum pot controla ca cererea mea sa nu fie dependenta de altcineva?

Dupa ce dam run la o comanda, acesta este puza intr-o coada de executie pe server.
Daca sunt 2 sesiuni care scriu in acelasi loc, a doua sesiune trebuie sa astepte dupa prima.
- cand cineva scrie intr-un tabel se creeaza un "block" la nivel de linie



Cum se salveaza un Update? 
La nivel de administrare exista niste fisiere speciale.
Cand cererile nu sunt salvate, sunt salvate cererile respective. 
Scrie in baza de date DOAR atunci cand dai COMMIT;


Clasificarea Comenzilor
- LMD -> limbaj de manipulare a datelor: INSERT, SELECT -> pot fi anulate
- LDD -> limbaj de definire a datelor: CREATE -> SE SALVEAZA AUTOMAT
- LCD -> limbaj de control a datelor: COMMIT, ROLLBACK, SAVEPOINT



CHECK 
- o constrangere

SAVEPOINT 
- este un punct intermediar
- faci 100 de inserturi, si dupa observi ca a87-a fost gresita; daca dai rollback se sterg toate 100
- in contextul sesiunii tale
- doar in contextul unei tranzactii

*/

begin
    select *
    from employees
    where employee_id=197;
end;
---------------------------------------------------------------------------------
/*
TRANZACTIE
- succesiune de comenzi LDD(orice LDD include si un LCD) intre 2 comenzi LCD


    exercitiu
    
INSERT  1
ALTER   2
CREATE  3
UPDATE  }
DELETE  }  4
INSERT  }
COMMIT }
DROP    5

cate tranzactii se executa aici? R:5
- orice operatie care modifica structura unui tabel ar trebui sa se propage cat mai repede
*/
select salary
from employees;

update employees
set salary=salary+50;

rollback;

---------------------------------------------------------------------------------

--exemplu de comanda SQL care nu merge in PL/SQL

--OBS: nu pot exista 2 obiecte cu acelasi nume


BEGIN
    create table test1(id number);
END;

/*
partea de SQL este evaluata independent

blocurile vor sa se execute in intregime sau deloc

begin
    comanda1
    comanda2
    comanda3 ->LMD
    ...
    comanda47 -> contine un LDD -> deci se va face commit la comenzile de sus
    ...
    comanda100
end

-atat timp cat partea de SQL poate aduce modificari permanente in timp ce alte
comenzi sunt in pending -> eroare
*/


BEGIN
   execute imediate 'create table test1(id number)';--execute imediate -> un alt fir de executie independent, directiva de PL/SQL
   
   update employees
   set salary=-2;
END;

--------------------------------------------------------------------------------------------------------------------------------------


--in blocul PLSQL cand folosim SELECT trebuie sa salvam intr-o variabila folosind clauza INTO
DECLARE 
    x varchar2(50);
begin
    select last_name INTO x
    from employees
    where employee_id>197;
end;

--atunci cand cererea intoarce mai multe linii folosim o structura cu dimensiunea nelimitata
--numita TABEL IMBRICAT

DECLARE 
    y employee.last_name(type); -????
begin
    select last_name INTO x
    from employees
    where employee_id<197;
end;

--cand avem mai multe linii de obiecte -> TABLOURI


-------RECAP SQL------------
----BD SERIE 1 exercitii----

--ex 1--

select
    p.nume, m.nume
from pacient p
join consultatie c on p.ID_PACIENT = c.ID_PACIENT
join prescriptie pr on c.ID_CONSULTATIE = pr.ID_CONSULTATIE
join medicament m on pr.ID_MEDICAMENT = m.ID_MEDICAMENT
where m.NUME='Ibuprofen';

--ex 2
select
    *
from (
    select
    d.id_doctor as ID_DOCTOR,
    d.nume as NUME_DOC,
    d.prenume AS PRENUME_DOC,
    s.nume AS SECTTIE,
    d.salariu AS SALARIU,
    (select count(*)
            from consultatie c2
            where c2.id_doctor = d.id_doctor
               )
from doctor d
join sectie s on d.id_sectie=s.ID_SECTIE
WHERE     (select count(*)
            from consultatie c2
            where c2.id_doctor = d.id_doctor
               ) >=2
order by d.SALARIU desc, (select count(*)
            from consultatie c2
            where c2.id_doctor = d.id_doctor
               ) >=2
     )
where ROWNUM<=2;

--ex 3

select
    s.nume as SECTIE,
    DECODE(doc.nume, NULL, '-', doc.nume) as NUME_DOCTOR,
    DECODE(doc.prenume,NULL,'-',doc.prenume) as PRENUME_DOCTOR,
    DECODE(doc.SALARIU,NULL,0,doc.SALARIU) as SALARIU
from sectie s
left join (select d.id_sectie,
                  d.nume,
                  d.prenume,
                  d.salariu
           from doctor d
           where d.salariu=
                 (
                     select
                         max(SALARIU)
                     from DOCTOR temp
                     where temp.ID_SECTIE=d.ID_SECTIE
                     )
           )  doc on doc.id_sectie=s.ID_SECTIE
group by s.nume, doc.nume, doc.prenume, doc.salariu


--ex 4
with sectie_consult as (
    select
    s.ID_SECTIE as nume_sectie,
    count(c.ID_CONSULTATIE) as numar_consultatii
from sectie s
join doctor d on s.ID_SECTIE=d.ID_SECTIE
join consultatie c on d.ID_DOCTOR = c.ID_DOCTOR
group by s.ID_SECTIE
), min_consult as (
    select
        MIN(numar_consultatii) as minim
    from sectie_consult
)
select
    *
from pacient d
join sectie_consult s on s.nume_sectie=d.ID_SECTIE
join min_consult m on m.minim=s.numar_consultatii






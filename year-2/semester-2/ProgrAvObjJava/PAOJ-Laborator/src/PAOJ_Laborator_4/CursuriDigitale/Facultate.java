package PAOJ_Laborator_4.CursuriDigitale;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Facultate
{
    public String nume;
    public String adresa;
    public List<Profesor> profesori; //agregare
    public List<Curs> cursuri=new ArrayList<>(); //compozitie

    public Facultate(String nume, String adresa)
    {
        this.nume = nume;
        this.adresa = adresa;
        this.profesori=new ArrayList<>();
    }

    public void adaugaProfesor(Profesor p)
    {
        this.profesori.add(p);

    }
    public void stergeProfesor(Profesor p)
    {
        this.profesori.remove(p);
    }
    public List<Profesor> listareProfesori()
    {
        profesori.forEach(System.out::println);
        return this.profesori;
    }



    void adaugaCurs(String nume, Profesor profesorTitular)
    {
        Curs c=new Curs(nume, profesorTitular);
        this.cursuri.add(c);
    }
    void stergeCurs(Curs c)
    {
        this.cursuri.remove(c);
    }

    public List<Curs> cautareCurs(String keyword)
    {
        List<Curs> rezultateCautare1=cursuri
                .stream()
                .filter(c->c.getNume().toLowerCase().contains(keyword.toLowerCase()))
                .toList();
        List<Curs> rezultateCautare2=cursuri //cautam daca apare in descrierea lectiilor
                .stream()
                .filter(c->c.lectii
                        .stream()
                        .anyMatch(l->l.getDescriere().toLowerCase().contains(keyword.toLowerCase())))
                .toList();

        Set<Curs> rezultat =new HashSet<>();
        rezultat.addAll(rezultateCautare1);
        rezultat.addAll(rezultateCautare2);

        return rezultat.stream().toList();

    }








}

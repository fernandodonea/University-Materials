package PAOJ_Laborator_4.CursuriDigitale;

import java.util.ArrayList;
import java.util.List;

public class Curs
{
    public String nume;
    public Profesor profesorTitular;
    public List<Lectie> lectii=new ArrayList<>();//compozitie

    public Curs(String nume, Profesor profesorTitular) {
        this.nume = nume;
        this.profesorTitular = profesorTitular;
    }

    public String getNume() {return nume;}
    public void setNume(String nume) {this.nume = nume;}
    public Profesor getProfesorTitular() {return profesorTitular;}
    public void setProfesorTitular(Profesor profesorTitular) {this.profesorTitular = profesorTitular;}

    public void adaugaLectie(String nume, String descriere)
    {
        Lectie l=new Lectie(nume, descriere);
        lectii.add(l);
    }
    public void afiseazaLectii()
    {
        lectii.forEach(System.out::println);
    }
    public void stergeLectie(int id)
    {
        lectii.removeIf(l->l.getId()==id);
    }

    @Override
    public String toString() {
        StringBuilder rezultat=new StringBuilder();
        rezultat.append("Curs: ").append(nume).append("Profesor Titular:").append(profesorTitular);
        if(!lectii.isEmpty())
        {
            rezultat.append("\nLectii:\n");
            for(Lectie l:lectii)
            {
                rezultat.append(l.toString()).append("\n");
            }
        }
        return rezultat.toString();
    }
}

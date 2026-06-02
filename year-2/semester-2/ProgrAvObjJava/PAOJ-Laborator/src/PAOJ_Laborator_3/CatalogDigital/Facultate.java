package PAOJ_Laborator_3.CatalogDigital;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Facultate
{
    public String nume;
    public String adresa;

    public List<Materie> materii=new ArrayList<>();
    private List<Student> studenti=new ArrayList<>();
    public List<Profesor> profesori=new ArrayList<>();
    private Map<Materie,Map<Student, List<Integer>>> catalog=new HashMap<>();

    public Facultate(String nume, String adresa) {
        this.nume = nume;
        this.adresa = adresa;
        this.studenti=new ArrayList<>();
        this.materii=new ArrayList<>();
        this.profesori=new ArrayList<>();
    }




    public void adaugaStudent(Student s) {studenti.add(s);}
    public void adaugaProfesor(Profesor p) {profesori.add(p);}
    public void adaugaMaterie(Materie m){materii.add(m);
    catalog.putIfAbsent(m, new HashMap<>());}

    public List<Materie> cautaMaterie(String cuvantCheie)
    {
        return materii
                .stream()
                .filter(m->m.getNume().toLowerCase().contains(cuvantCheie.toLowerCase()))
                .toList();
    }

    public List<Integer> obtineNote(Student student, Materie materie)
    {
        if(catalog.containsKey(materie) && catalog.get(materie).containsKey(student))
        {
            return catalog.get(materie).get(student);
        }
        return new ArrayList<>();
    }

    public List <Student> cautaStudent(Profesor profesor, String cuvantCheie)
    {
        List <Student> rezultateCautare=new ArrayList<>();
        for(var s: studenti)
        {
            if(s.getNume().toLowerCase().contains(cuvantCheie.toLowerCase()) ||
            s.getPrenume().toLowerCase().contains(cuvantCheie.toLowerCase()))
                rezultateCautare.add(s);
        }

        return rezultateCautare;
    }
    public void adaugaNota(Profesor profesor, Student student, Materie materie, Integer nota)
    {
        boolean verif=false;//verificam daca are voie sa modifica nota
        for(Materie m: profesor.getMateriiPredate())
        {
            if(m.equals(materie))
            {
                verif=true;
                break;
            }
        }
        if(verif)
        {
            if(catalog.get(materie).containsKey(student))
            {
                catalog.get(materie).get(student).add(nota);
            }
            else
            {
                List<Integer> note=new ArrayList<>();
                note.add(nota);
                catalog.get(materie).put(student,note);
            }

        }
    }
    public void modificaNota(Profesor profesor, Student student, Materie materie,int indexNotaVeche, Integer notaNoua)
    {

        boolean verif=false;//verificam daca are voie sa modifica nota
        for(Materie m: profesor.getMateriiPredate())
        {
            if(m.equals(materie))
            {
                verif=true;
                break;
            }
        }
        if(verif)
        {
            catalog.get(materie).get(student).set(indexNotaVeche, notaNoua);
        }
    }










}

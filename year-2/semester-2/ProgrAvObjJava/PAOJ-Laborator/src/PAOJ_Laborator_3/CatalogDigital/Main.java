package PAOJ_Laborator_3.CatalogDigital;

import java.util.List;

public class Main
{


    static void main()
    {
        Student s1=new Student("Popescu","Andrei","5030501245765","333/2024",2);
        Student s2=new Student("Popescu","Ana","4220771245765","222/2025",1);

        Materie m1=new Materie("Prog Orien Obiecte Java",5);
        Materie m2=new Materie("Retele",3);
        Materie m3=new Materie("Flp",1);

        Profesor p1= new Profesor("Nisioi","ionel","5030501243213","Lector", List.of(m2,m3),5000);
        Profesor p2= new Profesor("Popescu","Ioana","5030501243213","Labornt", List.of(m1),3000);


        Facultate fac=new Facultate("Facultatea de Informatica","Str. Universitatii nr. 1, Iasi");


        fac.adaugaStudent(s1);
        fac.adaugaStudent(s2);
        fac.adaugaMaterie(m1);

        fac .adaugaMaterie(m2);
        fac.adaugaMaterie(m3);

        fac.adaugaProfesor(p1);
        fac.adaugaProfesor(p2);

        System.out.println((fac.cautaMaterie("te")));
        List<Student> rezultateSearch=fac.cautaStudent(p1,"popescu");
        System.out.println(rezultateSearch);

        fac.adaugaNota(p1, rezultateSearch.get(1),m2,10);
        fac.adaugaNota(p1, rezultateSearch.get(1),m2,8);
        fac.adaugaNota(p1, rezultateSearch.get(1),m2,9);

        System.out.println((fac.obtineNote(rezultateSearch.get(1), m2)));

        fac.modificaNota(p1, rezultateSearch.get(1),m2,1,7);
        System.out.println((fac.obtineNote(rezultateSearch.get(1), m2)));
    }



}

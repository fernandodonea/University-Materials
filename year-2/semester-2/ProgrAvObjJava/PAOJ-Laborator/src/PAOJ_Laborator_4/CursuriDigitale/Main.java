package PAOJ_Laborator_4.CursuriDigitale;

public class Main
{
    static void main() {
        Profesor p1=new Profesor("Pop", "Ion", "1234567890123");
        Profesor p2=new Profesor("Ionescu", "Maria", "1234567890124");
        Profesor p3=new Profesor("Vasilescu", "Andrei", "1234567890125");

        Facultate f1=new Facultate("Facultatea de Informatica","Str. Universitatii nr. 1");
        Facultate f2=new Facultate("Facultatea de Matematica","Str. Universitatii nr. 2");


        f1.adaugaProfesor(p1);
        f1.adaugaProfesor(p3);
        f2.adaugaProfesor(p2);

        f1.adaugaCurs("Programare Orientata pe Obiecte", p1);
        f1.adaugaCurs("Structuri de Date", p1);
        f1.adaugaCurs("Analiza Matematica", p3);

        f2.adaugaCurs("Algebra", p2);
        f2.adaugaCurs("Geometrie", p2);

        f1.listareProfesori();



        //adaugam lectii
        f1.cursuri.getFirst().adaugaLectie("Clase si Obiecte", "Invatam despre clase si obiecte in Java");
        f1.cursuri.getFirst().adaugaLectie("Mostenire", "Invatam despre mostenire in Java");
        f1.cursuri.getFirst().adaugaLectie("Polimorfism", "Invatam despre polimorfism in Java");


        System.out.println(f1.cautareCurs("mostenire"));

        f1.cursuri.get(0).stergeLectie(1);
        System.out.println(f1.cautareCurs("despre"));


    }
}

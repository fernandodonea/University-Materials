package paoj.lab.PAOJ_Laborator_11.Streams;

public class Student
{
    private String nume;
    private String grupa;
    private double nota;

    public Student(String nume, String grupa, double nota) {
        this.nume = nume;
        this.grupa = grupa;
        this.nota = nota;
    }

    public String getNume() {
        return nume;
    }

    public String getGrupa() {
        return grupa;
    }

    public double getNota() {
        return nota;
    }

    @Override
    public String toString() {
        return nume + " (" + grupa + ") - " + nota;
    }
}

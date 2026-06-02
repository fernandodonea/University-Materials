package PAOJ_Laborator_3.CatalogDigital;

import java.util.Objects;

public class Student extends Persoana
{
    public String nrMatricol;
    public Integer anStudiu;

    public String getNrMatricol() {return nrMatricol;}
    public void setNrMatricol(String nrMatricol) {this.nrMatricol = nrMatricol;}
    public Integer getAnStudiu() {return anStudiu;}
    public void setAnStudiu(Integer anStudiu) {this.anStudiu = anStudiu;}

    public Student(String nume, String prenume, String cnp, String nrMatricol, Integer anStudiu) {
        super(nume, prenume, cnp);
        this.nrMatricol = nrMatricol;
        this.anStudiu = anStudiu;
    }

    @Override
    public String toString()
    {
        return "Student "+super.toString()+" | Nr. Matricol: "+ this.nrMatricol;
    }

    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Student student = (Student) o;
        return Objects.equals(this.getCnp(), student.getCnp());
    }
    @Override
    public int hashCode() {
        return Objects.hash(this.getCnp());
    }
}

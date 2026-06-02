package PAOJ_Laborator_3.CatalogDigital;

import java.util.List;

public class Profesor extends Persoana
{
    public String titluAcademic;
    public List<Materie> materiiPredate;
    private Integer salariu;

    public Profesor(String nume, String prenume, String cnp, String titluAcademic, List<Materie> materiiPredate, Integer salariu) {
        super(nume, prenume, cnp);
        this.titluAcademic = titluAcademic;
        this.materiiPredate = materiiPredate;
        this.salariu = salariu;
    }
    public String getTitluAcademic() {return titluAcademic;}
    public void setTitluAcademic(String titluAcademic) {this.titluAcademic = titluAcademic;}
    public Integer getSalariu() {return salariu;}
    public void setSalariu(Integer salariu) {this.salariu = salariu;}
    public List<Materie> getMateriiPredate() {return materiiPredate;}
    public void setMateriiPredate(List<Materie> materiiPredate) {this.materiiPredate = materiiPredate;}
    public void adaugaMateriiPredate(Materie materie){this.materiiPredate.add(materie);}

    @Override
    public String toString()
    {
        return "Profesor "+super.toString()+" | Titlu Academic: "+ this.titluAcademic+"\n";
    }
}

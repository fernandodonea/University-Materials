package PAOJ_Laborator_3.CatalogDigital;

public class Materie
{
    public String nume;
    private Integer nrCredite;

    public Materie(String nume, Integer nrCredite) {
        this.nume = nume;
        this.nrCredite = nrCredite;
    }

    public String getNume() {return nume;}
    public void setNume(String nume) {this.nume = nume;}
    public Integer getNrCredite() {return nrCredite;}
    public void setNrCredite(Integer nrCredite) {this.nrCredite = nrCredite;}

    @Override
    public String toString() {
        return "Materie | "+nume+" | Nr. Credite: "+nrCredite;
    }

    @Override
    public boolean equals(Object obj)
    {
        if(this==obj)return true;
        if(obj==null || this.getClass() != obj.getClass())return false;

        Materie materie = (Materie)obj;//downcast
        if(this.getNume().equals(materie.getNume()))
            return true;
        else return false;
    }
}

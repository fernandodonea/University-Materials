package PAOJ_Laborator_4.CursuriDigitale;

public class Lectie
{
    public String nume;
    public String descriere;
    private int id;

    private static int ct=0;

    public Lectie(String nume, String descriere) {
        this.nume = nume;
        this.descriere = descriere;
        this.id=ct++;
    }

    public String getNume() {return nume;}
    public void setNume(String nume) {this.nume = nume;}
    public String getDescriere() {return descriere;}
    public void setDescriere(String descriere) {this.descriere = descriere;}
    public int getId() {return id;}
    public void setId(int id) {this.id = id;}

    @Override
    public String toString()
    {
        return "[LECTIE]: Id:"+this.id+" | Nume lectie: "+this.nume+" | Descriere: "+this.descriere;
    }
}

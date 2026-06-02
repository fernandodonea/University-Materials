package PAOJ_Laborator_3.CatalogDigital;

public abstract class Persoana
{
    public String nume;
    public String prenume;
    private String cnp;
    private Integer id;
    private static Integer ct=0;

    public Persoana(String nume, String prenume, String cnp) {
        this.nume = nume;
        this.prenume = prenume;
        this.cnp = cnp;
        this.id=ct++;
    }

    public String getNume() {return nume;}
    public void setNume(String nume) {this.nume = nume;}
    public String getPrenume() {return prenume;}
    public void setPrenume(String prenume) {this.prenume = prenume;}
    public String getCnp() {return cnp;}
    public void setCnp(String cnp) {this.cnp = cnp;}
    public Integer getId() {return id;}
    public void setId(Integer id) {this.id = id;}

    @Override
    public String toString()
    {
        return "[ID: "+this.id+"] | Nume: "+this.nume+" | Prenume: "+this.prenume+"\n";
    }
}

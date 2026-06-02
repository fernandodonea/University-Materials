package PAOJ_Laborator_4.CursuriDigitale;

import java.util.List;

public class Profesor
{
    public String nume;
    public String prenume;
    private String cnp;

    public Profesor(String nume, String prenume, String cnp) {
        this.nume = nume;
        this.prenume = prenume;
        this.cnp = cnp;
    }
    public String getNume() {return nume;}
    public void setNume(String nume) {this.nume = nume;}
    public String getPrenume() {return prenume;}
    public void setPrenume(String prenume) {this.prenume = prenume;}
    public String getCnp() {return cnp;}
    public void setCnp(String cnp) {this.cnp = cnp;}


    @Override
    public String toString() {
        return "[Profesor] Nume: "+this.nume +" | Prenume: "+this.prenume;
    }
}

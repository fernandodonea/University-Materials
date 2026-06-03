package PAOJ_Laborator_5;

public class Facultate
{
    private String nume;
    public void setNume(String nume) { this.nume = nume; }
    public String getNume() { return nume; }

    public Facultate(String nume)
    {
        this.nume=nume;
    }

    public Facultate(Facultate other)
    {
        this.nume=other.nume;
    }
}

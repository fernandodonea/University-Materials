package paoj.lab.PAOJ_Laborator_6.OnlineBanking;

public class Profesor extends Utilizator
{
    private int salariu;

    public Profesor(String nume, double sold, String email, String parola, int salariu) {
        super(nume, sold, email, parola);
        this.salariu = salariu;
    }

    public int getSalariu() {return salariu;}
    public void setSalariu(int salariu) {this.salariu = salariu;}


    @Override
    public int compareTo(Utilizator o)
    {
        if (o instanceof Profesor)
        {
            Profesor p = (Profesor) o;
            return Integer.compare(p.salariu, this.salariu); //comparam descrecator
        }
        return 0; // sau aruncam o exceptie daca nu sunt comparabili

    }
}

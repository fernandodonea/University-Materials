package paoj.lab.PAOJ_Laborator_6.OnlineBanking;

public class FirmaPartenera extends Utilizator
{
    private double buget;

    public FirmaPartenera(String nume, double sold, String email, String parola, double buget) {
        super(nume, sold, email, parola);
        this.buget = buget;
    }

    public double getBuget() {return buget;}
    public void setBuget(double buget) {this.buget = buget;}

    @Override
    public int compareTo(Utilizator o)
    {
        if(o instanceof FirmaPartenera)
        {
            FirmaPartenera f= (FirmaPartenera) o;
            return Double.compare( f.buget,this.buget); //comparam descrecator
        }
        return 0;
    }
}

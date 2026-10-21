package paoj.lab.PAOJ_Laborator_6.OnlineBanking;

public abstract class Utilizator implements Comparable<Utilizator>, OperatiiContBancar
{
    public String nume;
    private double sold;
    private String email;
    private String parola;


    public Utilizator(String nume, double sold, String email, String parola) {
        this.nume = nume;
        this.sold = sold;
        this.email = email;
        this.parola = parola;
    }
    public String getNume() {return nume;}
    public void setNume(String nume) {this.nume = nume;}
    public double getSold() {return sold;}
    public void setSold(double sold) {this.sold = sold;}
    public String getEmail() {return email;}
    public void setEmail(String email) {this.email = email;}
    public String getParola() {return parola;}
    public void setParola(String parola) {this.parola = parola;}


    @Override
    public boolean autentificare()
    {
        // Implementare simpla pentru exemplu
        return email != null && parola != null && !email.isEmpty() && !parola.isEmpty();
    }
    @Override
    public double soldCurent()
    {
        return getSold();
    }
    @Override
    public void plata(double suma)
    {
        if(suma<=getSold())
        {
            setSold(getSold()-suma);
            System.out.println("Plata de "+suma+" procesata. Sold actualizat:"+getSold());
        }
        else
        {
            System.out.println("Fonduri insuficiente");

        }
    }
}

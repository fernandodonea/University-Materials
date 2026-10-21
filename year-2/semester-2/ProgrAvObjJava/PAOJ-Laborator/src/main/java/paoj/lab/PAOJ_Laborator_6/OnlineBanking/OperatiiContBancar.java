package paoj.lab.PAOJ_Laborator_6.OnlineBanking;

public interface OperatiiContBancar
{
    boolean autentificare();
    double soldCurent();
    void plata(double suma);

}

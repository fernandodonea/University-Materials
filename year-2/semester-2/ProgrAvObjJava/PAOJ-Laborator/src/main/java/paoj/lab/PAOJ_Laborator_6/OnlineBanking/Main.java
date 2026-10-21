package paoj.lab.PAOJ_Laborator_6.OnlineBanking;

public class Main
{
    public static void proceseazaPlati(OperatiiContBancar[] v, double suma)
    {
        for(OperatiiContBancar o: v)
        {
            if(o.autentificare())
            {
                System.out.println("Utilizator autentificat. Sold curent: " + o.soldCurent());
                o.plata(suma);
            }
            else
            {
                System.out.println("Autentificare esuata pentru un utilizator.");
            }
        }
    }
    static void main() {
        Student s=new Student("Andrei Popescu",500,"andrei@gmail.com","parola123",8);
        Profesor p=new Profesor("Stefan Rusu",5000,"rusu@yahoo","123123",5000);
        FirmaPartenera fp=new FirmaPartenera("Google",100000,"google@gmail.com","google",30000);


        OperatiiContBancar[] v= new OperatiiContBancar[] {s,p,fp};

        proceseazaPlati(v,1500);

    }

}

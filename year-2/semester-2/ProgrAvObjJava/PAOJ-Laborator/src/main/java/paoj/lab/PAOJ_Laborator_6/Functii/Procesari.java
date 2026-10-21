package paoj.lab.PAOJ_Laborator_6.Functii;

public class Procesari
{
    public static int suma(FunctieIntreg f, int n)
    {
        int s=0;
        for(int i=1;i<=n;i++)
        {
            s+=f.valoare(i);
        }
        return s;
    }

    public static int numara(FunctieIntreg f, int n)
    {
        int ctPozitive =0;
        for(int i=1;i<=n;i++)
        {
            if(f.valoare(i)>0)
                ctPozitive +=1;
        }
        return ctPozitive;
    }
    public static int[] transforma(FunctieIntreg f, int n)
    {
        int[] v=new int[n];
        for(int i=0;i<n;i++)
        {
            v[i]=f.valoare(i+1);
        }
        return v;
    }

}

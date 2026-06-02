package PAOJ_Laborator_1;

import java.util.Scanner;

public class Main
{




    //ex 1
    static void ex1_palindrom()
    {
        Scanner sc = new Scanner(System.in);//citim de la consola
        System.out.print("n=");
        int n=sc.nextInt();

        int cn=n,ogl=0;
        while(cn!=0)
        {
            int c=cn%10;
            cn=cn/10;
            ogl=ogl*10+c;
        }
        if(n==ogl)
            System.out.println("Numarul "+n+" este palindrom!");
        else
            System.out.println("Numarul "+n+" NU este palindrom!");
    }

    private static String fromIntToBinary(int n)
    {
        int binary=0;
        int p=1;
        while(n!=0)
        {
            int c=n%2;
            n=n/2;

            binary=binary+c*p;
            p=p*10;
        }
        return Integer.toString(binary);

    }

    //ex 2
    static void ex2_nrImparInBaza2()
    {
//        Scanner sc= new Scanner(System.in);
//        System.out.print("n=");
//        int n=sc.nextInt();
        int n=4;

        String b=fromIntToBinary(n);
        int k=0;
        for(int i=0;i<b.length();i++)
        {
            if(b.charAt(i)=='1')
                k++;
        }
        System.out.println("n="+n);
        System.out.println(n+"="+b);
        System.out.println("Nr de cifre de 1 in baza 2:  "+k);
        if(k%2==0)
            System.out.println("False");
        else System.out.println("True");


    }

    static void ex3_celMaiLungsubsirUnu()
    {
        int n=102;

        String s=fromIntToBinary(n);

        int subsirCurent=0, subsirMax=0;
        for(int i=0;i<s.length();i++)
        {
            if(s.charAt(i)=='1')
                subsirCurent+=1;
            else
            {
                if(subsirCurent>subsirMax)
                    subsirMax=subsirCurent;
                subsirCurent=0;
            }
        }
        System.out.println(subsirMax);
    }

    public static void ex4_and_or()
    {
        int n=4;
        String binary=fromIntToBinary(n);

        int v_and=1, v_or=0;
        for(int i=0;i<binary.length();i++)
        {
            if(binary.charAt(i)=='1')
            {
                v_or=1;
            }
            else{
                v_and=0;
            }
        }
        if(v_and==v_or)
            System.out.println(true);
        else System.out.println(false);


    }


    static void main()
    {
        //ex1_palindrom();
        //ex2_nrImparInBaza2();
        //ex3_celMaiLungsubsirUnu();
        //ex4_and_or();



    }
}

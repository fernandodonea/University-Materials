package PAOJ_Laborator_2;

import java.util.Scanner;

public class Main
{

    public static void ex_1celMaiLungSubsirCrescator()
    {
        int[] v={1, 2, 3, 2, 1, 4, 5, 6, 5, 7, 8, 9, 10};
        int subsirCurent=1,subsirMax=0;
        for(int i=1;i<v.length;i++)
        {
            if(v[i]>v[i-1])
                subsirCurent+=1;
            else
            {
                if(subsirCurent>subsirMax)
                    subsirMax=subsirCurent;
                subsirCurent=1;
            }
        }
        if(subsirCurent>subsirMax)
            subsirMax=subsirCurent;


        System.out.println(subsirMax);
    }

    public static void ex2_matriceVeciniUnu()
    {
        int n=2,m=2;
        Scanner sc=new Scanner(System.in);

        int[][] a = new int[n+2][m+2];
        int nrAparatiiUnu=0, nrTotiVeciniiZero=0;


        //citire
        for(int i=0;i<=n+1;i++)
        {
            for(int j=0;j<=m+1;j++)
            {
                if(i==0 || j==0 || i==n+1 || j==m+1)
                    a[i][j]=0;
                else
                    a[i][j]=sc.nextInt();
            }
        }

        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=m;j++)
            {
                if(a[i][j]==1)
                    nrAparatiiUnu+=1;
                if(a[i][j-1]==0 && a[i][j+1]==0 && a[i-1][j]==0 && a[i+1][j]==0)
                    nrTotiVeciniiZero+=1;
            }
        }
        System.out.println(nrAparatiiUnu);
        System.out.println(nrTotiVeciniiZero);

    }

    public static void ex3_sumaMaximaSubsir()
    {
        int[] v={1 ,2,-3, 1,2,3,-5,1,2,-4,1,2};
        int sumaCurenta=0,sumaMaxima=-100000;
        for(int i=0;i<v.length;i++)
        {
            sumaCurenta+=v[i];
            if(sumaCurenta>sumaMaxima)
                sumaMaxima=sumaCurenta;
            if(sumaCurenta<0)
            {
                sumaCurenta=0;
            }
        }
        System.out.println(sumaMaxima);
    }

    public static void ex4_lista()
    {
        List list=new List();
        list.addLast(3);
        list.addLast(5);
        list.addLast(4);

        list.addLast(1);


        System.out.println(list);

        list.addAtIndex(100,3);
        list.addFirst(100);


        System.out.println(list);
        System.out.println(list.find(100));
        System.out.println(list.size());

        list.sort();
        System.out.println(list);

        list.remove(100);
        System.out.println(list);


        List copyList=new List(list);
        System.out.println(copyList);

    }

    static void main() {
        //ex_1celMaiLungSubsirCrescator();
        //ex2_matriceVeciniUnu();
        //ex3_sumaMaximaSubsir();
        //ex4_lista();

    }
}

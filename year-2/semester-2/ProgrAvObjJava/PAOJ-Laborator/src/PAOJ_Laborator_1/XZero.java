package PAOJ_Laborator1;

import java.util.Scanner;

public class XZero
{



    static void main(String[] args)
    {
        xAndZero();
    }





    private static void initTable(char [][] table)
    {
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                table[i][j]='_';
            }
        }

    }

    private static void printTable(char [][] table)
    {
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                System.out.print(table[i][j]);
            }
            System.out.println();
        }
    }

    private static char winner(char [][] table)
    {
        //verificam pe linie
        for(int i=0;i<3;i++)
        {
            if(table[i][0]== table[i][1] & table[i][1]==table[i][2])
                if(table[i][0]!='_')
                    return table[i][0];
        }
        //verificam pe coloana
        for(int j=0;j<3;j++)
        {
            if(table[0][j]==table[1][j] & table[1][j]==table[2][j])
                if(table[0][j]!='_')
                    return table[0][j];

        }
        //verificam pe diagonala
        if(table[0][0]==table[1][1] & table[1][1]==table[2][2])
            if(table[0][0]!='_')
                return table[0][0];
        if(table[0][2]==table[1][1] & table[1][1]==table[2][0])
            if(table[0][2]!='_')
                return table[0][2];

        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                if(table[i][j]=='_')
                    return 'n'; //jocul continua
            }
        }
        return '_'; //remiza

    }


    private static void makeMove(char [][] table, char player)
    {
        System.out.println("Jucatorul "+player);


        System.out.print("Linie: ");
        Scanner sc = new Scanner(System.in);
        int line = sc.nextInt();



        System.out.print("Coloana ");
        sc = new Scanner(System.in);
        int column = sc.nextInt();

        if(line<1 | line >3 | column <1 | column>3)
        {
            System.out.println("Mutare invalida");
            makeMove(table,player);
        }
       else if( table[line-1][column-1]!='_')
       {
           System.out.println("Loc ocupat deja!");
           makeMove(table,player);
       }
       else  table[line-1][column-1]=player;
    }






    private static void xAndZero()
    {

        char [][] table = new char[3][3];
        char turn ='X';

        initTable(table);
        printTable(table);

        while(winner(table)=='n')
        {

            makeMove(table,turn);
            printTable(table);


            if(turn=='X')
                turn='0';
            else turn='X';
        }

        System.out.println("Castigatorul este: "+ winner(table));





    }

}

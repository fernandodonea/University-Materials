package paoj.lab.PAOJ_Laborator_7;

import java.io.*;
import java.util.InputMismatchException;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class CitireFisier
{


    static void main()
    {
        String path="src/PAOJ_Laborator_7/";
        String inputFilename="numere.txt";
        String outputFilename="rezultat.txt";
        int a,b,c;


        try(Scanner r=new Scanner(new File(path+inputFilename));
            PrintWriter w=new PrintWriter(new File(path+outputFilename))
        )
        {
            a=r.nextInt();
            b=r.nextInt();

            c=a/b;
            w.println(c);
        }
        catch (FileNotFoundException e)
        {
            System.out.println("Fisierul nu a fost gasit");
        }
        catch (InputMismatchException e)
        {
            System.out.println("Nu au fost citire doua inturi");
        }
        catch(NoSuchElementException e)
        {
            System.out.println("Nu au fost citire destule numere");

        }
        catch(ArithmeticException e)
        {
            System.out.println("Impartire la zero");

        }
        catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}

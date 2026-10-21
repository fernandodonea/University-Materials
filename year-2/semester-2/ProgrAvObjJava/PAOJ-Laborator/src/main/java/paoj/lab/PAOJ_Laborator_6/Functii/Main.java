package paoj.lab.PAOJ_Laborator_6.Functii;

import java.util.Arrays;

public class Main
{
    static void main() {
        System.out.println(Procesari.numara(new Identitate(), 5));
        System.out.println(Procesari.suma(new Identitate(),5));

        int[] v=Procesari.transforma(new PatratPerfect(),5);
        Arrays.stream(v).forEach(p-> System.out.print(p+" "));
    }
}

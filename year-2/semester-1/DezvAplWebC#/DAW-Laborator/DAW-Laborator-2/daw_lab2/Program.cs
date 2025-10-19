

/*
    TEORIE LABORATOR
*/

// namespace Laborator
// {
//     public class Program
//     {
//         public static void Run(string[] args)
//         {
//             Console.WriteLine("Hello, World!");

//             //Tipuri de date
//             int nr = 100;
//             string str = "Acesta este un text";
//             double d = 12.35;
//             char c = 'a';
//             bool b = true;
//             object obj = 100;
//             Console.WriteLine("Numarul este " + nr);
//             Console.WriteLine("Stringul este: " + str);
//             Console.WriteLine("Numarul in virgula mobila este: " + d);
//             Console.WriteLine("Caracterul este: " + c);
//             Console.WriteLine("Valoarea de adevar este: " + b);
//             Console.WriteLine("Obiectul este: " + obj);

//             //readline si writeline citesesc si afiseaza doar stringuri


//             // CONVERSII IMPLICITE
//             int nrInt = 10;
//             // Metoda GetType() preia tipul de date
//             Type tipNrInt = nrInt.GetType();
//             // Conversie implicita
//             double nrDouble = nrInt;
//             // Se preia tipul
//             Type tipNrDouble = nrDouble.GetType();
//             // Afisare valori inainte de conversie
//             Console.WriteLine("nrInt value: " + nrInt);
//             Console.WriteLine("nrInt Type: " + tipNrInt);
//             // Afisare valori dupa conversia implicita
//             Console.WriteLine("nrDouble value: " + nrDouble);
//             Console.WriteLine("nrDouble Type: " + tipNrDouble);


//             // CONVERSII EXPLICITE
//             double nDouble = 25.123;
//             // Conversie explicita
//             int nInt = (int)nDouble;
//             // Afisarea valorii inainte de conversie
//             Console.WriteLine("Valoarea inainte de conversie a fost: " + nDouble);
//             // Afisarea valorii dupa conversie
//             Console.WriteLine("Valoarea dupa conversie este: " + nInt);


//             // CONVERSIE UTILIZAND PARSE()
//             string st = "100";
//             // tipul de date
//             Type tip1 = st.GetType();
//             // Se converteste tipul string in int
//             int x = int.Parse(st);
//             Type tip2 = x.GetType();
//             Console.WriteLine("Valoarea initiala a fost: " + st);
//             Console.WriteLine("A avut tipul: " + tip1);
//             Console.WriteLine("Noua valoare dupa conversie este: " + x);
//             Console.WriteLine("Valoarea dupa conversie are tipul: " + tip2);
//         }

//     }
// }














/*
    EX 1
*/


// namespace Laborator2
// {
//     public class Program
//     {
//         static void Main(string[] args)
//         {
//             int n, cn, x;
//             n = int.Parse(Console.ReadLine());

//             cn = n;
//             x = 0;
//             while (cn != 0)
//             {
//                 int c = cn % 10;
//                 cn /= 10;
//                 x = x * 10 + c;
//             }
//             if (n == x)
//             {
//                 Console.WriteLine("DA");
//             }
//             else Console.WriteLine("NU");
//         }

//     }
// }


















/*
    EX 2
*/


// class Program
// {
//     void Palindrom(int n)
//     {
//         int cn, x;

//         cn = n;
//         x = 0;
//         while (cn != 0)
//         {
//             int c = cn % 10;
//             cn /= 10;
//             x = x * 10 + c;
//         }
//         if (n == x)
//         {
//             Console.WriteLine("DA");
//         }
//         else Console.WriteLine("NU");

//     }
//     static void Main(string[] args)
//     {
//         int n = int.Parse(Console.ReadLine());
//         Program idk = new Program();
//         idk.Palindrom(n);
//     }
// } 


















/*
    EX 3
*/


class Program
{
    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());
        bool ok = true;
        int[] v = new int[101];
        v[1] = int.Parse(Console.ReadLine());
        for (int i = 2; i <= n; i++)
        {
            int x = int.Parse(Console.ReadLine());
            v[i] = x;
            if (v[i - 1] % 2 == v[i] % 2)
                ok = false;
        }
        if (ok == false)
            Console.WriteLine("NU");
        else Console.WriteLine("DA");
    }
} 
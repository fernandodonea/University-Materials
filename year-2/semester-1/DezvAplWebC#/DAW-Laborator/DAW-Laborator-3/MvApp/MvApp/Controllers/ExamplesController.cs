using Microsoft.AspNetCore.Mvc;

namespace MyApp.Namespace
{
    public class Examples : Controller
    {
        // GET: MvApp
        public string Concatenare(string? s1, string? s2)
        {
            return s1 + s2;
        }
        public string Produs(int a, int? b)
        {
            if (b == null)
            {
                return "Introduceti ambele valori";
            }
            else return (a * b).ToString();

        }
        public string Operatie(int? param1, int? param2, string op)
        {
            string eroare = "Introduceti paramtrul ";
            if (param1 == null)
            {
                eroare += "1/";

            }
            if (param2 == null)
            {
                eroare += "2/";
            }
            if (op == null)
            {
                eroare += "3";
            }

            if (param1 != null && param2 != null && op != null)
            {
                if (op == "plus") return (param1 + param2).ToString();
                if (op == "minus") return (param1 - param2).ToString();
                if (op == "ori") return (param1 * param2).ToString();
                if (op == "div") return (param1 / param2).ToString();
                else return eroare;
            }
            else return eroare;
            
        
        }


    }
}

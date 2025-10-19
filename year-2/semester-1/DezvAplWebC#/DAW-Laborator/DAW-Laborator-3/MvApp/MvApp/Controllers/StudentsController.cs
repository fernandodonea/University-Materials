using Microsoft.AspNetCore.Mvc;

namespace MyApp.Namespace
{
    public class Students : Controller
    {
        public string Index()
        {
            return "Afisarea tuturor studentilor";
        }
        public string Create()
        {
            return "Creare student";
        }
        public string Show(int? id)
        {
            if (id is null)
            {
                return "NU exista id-ul";
            }
            else return "Afisare student cu id-ul:" + id;
        }
        public string Edit(int? id)
        {
            if (id is null)
            {
                return "NU exista id-ul";
            }
            else return "Editare student cu id-ul:" + id;
        }
        public string Delete(int? id)
        {
            if (id is null)
            {
                return "NU exista id-ul";
            }
            else return "Stergere student cu id-ul:" + id;
        }     
    }

}

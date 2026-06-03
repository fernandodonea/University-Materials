package PAOJ_Laborator_5;

//trebuie ca clasa sa fie declarata final
final class Student
{
    //toate atributele tre sa fie private si final
    private final String nume;
    private final Facultate facultate;

    public Student(String nume, Facultate facultate)
    {
        this.nume = nume;
        this.facultate = new Facultate(facultate); //tre sa fie compozitie nu agregare
    }

    public Facultate getFacultate()
    {
        //nu trebuie sa returnam referinta
        return new Facultate(facultate);
    }


    public String getNume() {
        return nume;
    }

}
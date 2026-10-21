package paoj.lab.PAOJ_Laborator_6.OnlineBanking;

public class Student extends Utilizator
{

    private int medie;

    public Student(String nume, double sold, String email, String parola, int medie) {
        super(nume, sold, email, parola);
        this.medie = medie;
    }

    public int getMedie() {return medie;}
    public void setMedie(int medie) {this.medie = medie;}


    @Override
    public int compareTo(Utilizator o) {
        if(o instanceof Student)
        {
            Student s = (Student) o;
            return getNume().compareTo(s.getNume());
        }
        return  this.nume.compareTo(o.getNume());

    }



}

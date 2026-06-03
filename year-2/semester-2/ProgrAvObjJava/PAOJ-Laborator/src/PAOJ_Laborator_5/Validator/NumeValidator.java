package PAOJ_Laborator_5.Validator;

public class NumeValidator implements Validator<String>
{
    @Override
    public boolean validate(String nume)
    {
        if(nume==null)
            return false;

        for(int i=0;i<nume.length();i++)
        {
            char ch=nume.charAt(i);
            if(Character.isLetter(ch)==false)
                return false;
            if(i==0 && Character.isLowerCase(ch)==true) //numele trebuie sa inceapa cu majuscula
                return false;
            if(i!=0 && Character.isLowerCase(ch)==false) //restul trebuie sa fie litere mici
                return false;
        }
        return true;
    }
}

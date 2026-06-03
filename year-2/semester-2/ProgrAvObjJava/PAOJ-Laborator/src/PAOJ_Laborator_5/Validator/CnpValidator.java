package PAOJ_Laborator_5.Validator;

public class CnpValidator implements Validator<String>
{
    @Override
    public boolean validate(String cnp)
    {
        if(cnp==null)
            return false;
        cnp=cnp.replaceAll(" ", "");

        if(cnp.length()!=13)
            return false;
        for(int i=0;i<cnp.length();i++)
        {
            char ch=cnp.charAt(i);
            if(Character.isDigit(ch)==false)
                return false;
        }

        return true;
    }
}

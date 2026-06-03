package PAOJ_Laborator_5.Validator;

public class TelefonValidator implements Validator<String>
{

    private boolean allNumbers(String text)
    {
        for(int i=0;i<text.length();i++)
        {
            char ch=text.charAt(i);
            if(Character.isDigit(ch)==false)
                return false;
        }
        return true;
    }

    @Override
    public boolean validate(String nrTelefon)
    {
        if(nrTelefon==null)
            return false;

        nrTelefon=nrTelefon.replaceAll(" ","");

        //cazul +40 728 791 065
        if(nrTelefon.length()==12)
        {
            if(nrTelefon.charAt(0)!='+')
                return false;

            return allNumbers(nrTelefon.substring(1));

        }
        if(nrTelefon.length()==10)
        {
            if(nrTelefon.charAt(0)!='0')
                return false;

            return allNumbers(nrTelefon);

        }
        return false;
    }
}

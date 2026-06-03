package PAOJ_Laborator_5.Validator;

public class DataValidator implements Validator<String>
{



    @Override
    public boolean validate(String data)
    {
        if(data==null)
            return false;

        data=data.replaceAll(" ","");

        //DD-MM-YYYY
        if(data.length()!=10)
            return false;

        String[] parsedDate =data.split("-");
        String zi= parsedDate[0];
        String luna= parsedDate[1];
        String an=parsedDate[2];

        try{
            int day=Integer.parseInt(zi);
            int month=Integer.parseInt(luna);
            int year=Integer.parseInt(an);

            if(day<1 || day>31)
                return false;
            if(month<1 || month>12)
                return false;
            if(year<1800 || year>2026)
                return false;

            return true;
        }
        catch (NumberFormatException e)
        {
            return false;
        }



    }
    static void main()
    {
        String data="12-01-2024";
        DataValidator db= new DataValidator();
        System.out.println(db.validate(data));




    }
}

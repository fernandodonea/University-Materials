package PAOJ_Laborator_5.Validator;



public class ValidatorInscriereStudent
{
    private static final Validator<String> cnpValidator=new CnpValidator();
    private static final Validator<String> telefonValidator=new TelefonValidator();
    private static final Validator<String> numeValidator=new NumeValidator();
    private static final Validator<String> dateValidator = new DataValidator();

    public static boolean validateCnp(String cnp)
    {
        return ValidationEngine.validate(cnp, cnpValidator);
    }
    public static boolean validateNume(String nume)
    {
        return ValidationEngine.validate(nume, numeValidator);
    }
    public static boolean validateTelefon(String telefon)
    {
        return ValidationEngine.validate(telefon, telefonValidator);
    }
    public static int extrageAnNastere(String data)
    {
        if(ValidationEngine.validate(data,dateValidator)==false)
            return -1;
        //DD-MM-YYYY
        return Integer.parseInt(data.substring(6));
    }




}

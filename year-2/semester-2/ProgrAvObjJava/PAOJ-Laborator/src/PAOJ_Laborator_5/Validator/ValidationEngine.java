package PAOJ_Laborator_5.Validator;

public class ValidationEngine
{
    public static boolean validate(String value, Validator<String> validator)
    {
        return validator.validate(value);
    }
}


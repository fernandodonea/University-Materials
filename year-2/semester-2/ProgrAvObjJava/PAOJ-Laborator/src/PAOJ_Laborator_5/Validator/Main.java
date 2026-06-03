package PAOJ_Laborator_5.Validator;

public class Main {
    public static void main(String[] args) {


        System.out.println("CNP  1961001223456 " + ValidatorInscriereStudent.validateCnp("1961001223456"));
        System.out.println("CNP  123 " + ValidatorInscriereStudent.validateCnp("123"));


        System.out.println("Telefon: 0712345678 " + ValidatorInscriereStudent.validateTelefon("0712345678"));
        System.out.println("Telefon +40712345678 " + ValidatorInscriereStudent.validateTelefon("+40712345678"));
        System.out.println("Telefon 1234: " + ValidatorInscriereStudent.validateTelefon("1234"));


        System.out.println("Nume Ion " + ValidatorInscriereStudent.validateNume("Ion"));
        System.out.println("Nume Io4n " + ValidatorInscriereStudent.validateNume("Io4n"));


        String date = "10-11-2001";
        int year = ValidatorInscriereStudent.extrageAnNastere(date);
        System.out.println("An extras din " + date + " = " + year);
    }
}
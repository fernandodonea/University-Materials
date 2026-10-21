package paoj.lab.PAOJ_Laborator_11;



import paoj.lab.PAOJ_Laborator_11.Streams.Student;
import paoj.lab.PAOJ_Laborator_11.ProductsDB.*;

import java.util.List;
import java.util.stream.Collectors;


public class Main {

    public static void ex1_getStudentiPromovati_Medie()
    {
        List<Student> studenti = List.of(
                new Student("Ana", "MI221", 9.5),
                new Student("Bogdan", "MI221", 4.8),
                new Student("Cristina", "MI222", 8.7),
                new Student("Dan", "MI221", 6.2),
                new Student("Elena", "MI222", 10.0),
                new Student("Florin", "MI223", 5.5),
                new Student("George", "MI223", 3.9),
                new Student("Irina", "MI222", 7.8)
        );

        List<String> studentiPromovati=studenti
                .stream()
                .filter(s->s.getNota()>=5)
                .map(Student::getNume)
                .collect(Collectors.toList());
        System.out.println(studentiPromovati);


        double mediePromovati=studenti
                .stream()
                .filter(s->s.getNota()>=5)
                .mapToDouble(s-> s.getNota())
                .average().orElse(0);

        System.out.println(mediePromovati);

    }

    public static void ex2_product_database()
    {
        DataBase db= new DataBase();

        Product banana=new Product(1,"banane","fructe",10,5);
        Product mar=new Product(2,"mere","fructe",110,15);
        Product tricou=new Product(4,"hanorac","haine",300,2);

        ProductDatabase productDatabase=new ProductDatabase(db.getCon());

        //productDatabase.create(tricou);

        productDatabase.findAll().forEach(System.out::println);

        System.out.println(productDatabase.findById(2));

        System.out.println();
        productDatabase.findByCategory("haine").forEach(System.out::println);

        productDatabase.updatePriceAndStock(1,100000,300);

        productDatabase.deleteById(3);
        productDatabase.findAll().forEach(System.out::println);

    }



    static void main()
    {
        //ex1_getStudentiPromovati_Medie();
        ex2_product_database();
    }



}



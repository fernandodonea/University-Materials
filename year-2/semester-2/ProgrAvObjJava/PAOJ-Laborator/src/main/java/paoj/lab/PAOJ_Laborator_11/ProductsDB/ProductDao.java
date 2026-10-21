package paoj.lab.PAOJ_Laborator_11.ProductsDB;

import java.util.List;

public interface ProductDao
{

    /* insereaza in baza de date un produs al carei date vin prin parametrul 'product' */
    void create(Product product);

    /*
    intoarce inapoi din baza de date toate produsele sub forma unei liste
     daca nu exista nici un produs se va returna o lista goala
     */
    List<Product> findAll();


    /*
    intoarce din baza de date un produs cu id-ul dat
    daca nu exista  nici un produs cu id-ul respectiv se va returna null
     */
    Product findById(int id);



    /*
     * returneaza toate produsele din baza care au aceasta categorie
     * daca nu exista nici un produs se va returna o lista goala
     */
    List<Product> findByCategory(String category);


    /*
     pentru produsul cu id-ul dat updateaza pretul si stocul
     daca nu exista nici un produs cu id-ul dat se va arunca o exceptie custom
     */
    void updatePriceAndStock(int id, double price, int stock);


    /*
    sterge din baza produsul cu id-ul dat ca parametru
     */
    void deleteById(int id);
}
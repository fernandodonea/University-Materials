package paoj.lab.PAOJ_Laborator_11.ProductsDB;

import java.io.IOException;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;

public class DataBase
{
    private String url;
    private String user;
    private String password;
    public Connection con;

    private void connectToDb()
    {
        try{
            this.con=DriverManager.getConnection(url, user, password);
        }
        catch (SQLException e)
        {
            System.out.println("Baza de date nu merge");
        }
    }

    private void loadPropertiesFromFile()
    {
        Properties props = new Properties();
        try (InputStream input = getClass().getClassLoader().getResourceAsStream("application.properties")) {
            if (input == null) {
                System.out.println("Fișierul application.properties nu a fost găsit!");
                return;
            }
            props.load(input);
            this.url = props.getProperty("db.url");
            this.user = props.getProperty("db.user");
            this.password = props.getProperty("db.password");
        } catch (IOException e) {
            System.out.println("Eroare la citirea fișierului properties: " + e.getMessage());
        }

    }


    public DataBase() {
        loadPropertiesFromFile();
        connectToDb();
    }


    public DataBase(String url, String user, String password) {
        this.url = url;
        this.user = user;
        this.password = password;

        connectToDb();
    }

    public String getUrl() {return url;}
    public void setUrl(String url) {this.url = url;}
    public String getUser() {return user;}
    public void setUser(String user) {this.user = user;}
    public String getPassword() {return password;}
    public void setPassword(String password) {this.password = password;}
    public Connection getCon() {return con;}
    public void setCon(Connection con) {this.con = con;}
}

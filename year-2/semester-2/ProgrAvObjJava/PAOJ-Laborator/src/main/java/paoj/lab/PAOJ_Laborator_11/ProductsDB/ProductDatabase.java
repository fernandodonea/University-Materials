package paoj.lab.PAOJ_Laborator_11.ProductsDB;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class ProductDatabase implements ProductDao
{
    private Connection con;

    public ProductDatabase(Connection con) {
        if(con!=null)
            this.con = con;
         else
            System.out.println("Conexiunea nu a fost realizata");
    }

    public Connection getCon() {return con;}
    public void setCon(Connection con) {this.con = con;}


    @Override
    public void create(Product product)
    {
       try{
           String sql="INSERT INTO products(name,category,price,stock) VALUES (?,?,?,?)";
           PreparedStatement ps=con.prepareStatement(sql);


           ps.setString(1,product.getName());
           ps.setString(2,product.getCategory());
           ps.setDouble(3, product.getPrice());
           ps.setInt(4,product.getStock());

           ps.executeUpdate();
           System.out.println("S-a inserat cu succes");

       }
       catch (SQLException e)
       {
           System.out.println("Eroare la inserare");
       }

    }
    @Override
    public List<Product> findAll()
    {
        List<Product> produse=new ArrayList<>();

        String sql="SELECT * FROM products";
        try{
            Statement stmt = con.createStatement();
            ResultSet rs = stmt.executeQuery(sql);

            while(rs.next())
            {
                Product p=new Product(
                        rs.getInt("id"),
                        rs.getString("name"),
                        rs.getString("category"),
                        rs.getDouble("price"),
                        rs.getInt("stock")
                );
                produse.add(p);
            }

        }
        catch (SQLException e)
        {
            System.out.println("Eroare la interogare");
        }

        return produse;
    }
    @Override
    public Product findById(int id)
    {
        String sqlQuery="SELECT * FROM products WHERE id=(?)";
        try{

            PreparedStatement pstm=con.prepareStatement(sqlQuery);
            pstm.setInt(1,id);

            ResultSet rs= pstm.executeQuery();

            if(rs.next())
            {
                Product p=new Product(
                        rs.getInt("id"),
                        rs.getString("name"),
                        rs.getString("category"),
                        rs.getDouble("price"),
                        rs.getInt("stock")
                );
                return p;
            }
        }
        catch (SQLException e)
        {
            System.out.println("Eroare la cautare");
        }
        return null;
    }
    @Override
    public List<Product> findByCategory(String category)
    {
        List<Product> produse=new ArrayList<>();

        String sql="SELECT * FROM products WHERE category=(?)";
        try{
            PreparedStatement stmt = con.prepareStatement(sql);
            stmt.setString(1,category);

            ResultSet rs = stmt.executeQuery();

            while(rs.next())
            {
                Product p=new Product(
                        rs.getInt("id"),
                        rs.getString("name"),
                        rs.getString("category"),
                        rs.getDouble("price"),
                        rs.getInt("stock")
                );
                produse.add(p);
            }

        }
        catch (SQLException e)
        {
            System.out.println("Eroare la cautarea dupa categorie");
        }

        return produse;
    }
    @Override
    public void updatePriceAndStock(int id, double price, int stock)
    {
        String sql="UPDATE products SET price=(?), stock=(?) WHERE id=(?)";
        try{
            PreparedStatement pstm=con.prepareStatement(sql);
            pstm.setDouble(1,price);
            pstm.setInt(2,stock);
            pstm.setInt(3,id);

            int n=pstm.executeUpdate();
            if(n>0)
            {
                System.out.println("produs actulizat");
                System.out.println(findById(id));
            }
            else{
                System.out.println("nu exista produsa");
            }


        }
        catch (SQLException e)
        {
            System.out.println("Eroare la update");
        }



    }
    @Override
    public void deleteById(int id)
    {
        String sql="DELETE FROM products WHERE ID=?";
        try{
            PreparedStatement pstm=con.prepareStatement(sql);
            pstm.setInt(1,id);

            int n=pstm.executeUpdate();
            if(n>0)
            {
                System.out.println("S a sters cu succes");
            }
            else{
                System.out.println("nu s a gasit produsul");
            }


        }
        catch (SQLException e)
        {
            System.out.println("Nu s a putut sterge");

        }


    }
}

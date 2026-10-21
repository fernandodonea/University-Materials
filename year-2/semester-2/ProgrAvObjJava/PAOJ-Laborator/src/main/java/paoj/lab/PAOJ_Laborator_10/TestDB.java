package paoj.lab.PAOJ_Laborator_10;

import java.sql.*;

public class TestDB
{
    Connection connection = DriverManager.getConnection("jdbc:mysql://zephyr.proxy.rlwy.net:58623/railway", "root", "rBwHXAyHQnICanhqfMBvNYdzEtatyRmc");


    public TestDB() throws SQLException {}

    public Connection getConnection() {return connection;}
    public void setConnection(Connection connection) {this.connection = connection;}

    static void main() throws SQLException {
        TestDB db=new TestDB();
        Connection con=db.getConnection();

        //PreparedStatement ps=con.prepareStatement("UPDATE idk SET name=? where id=?");
        PreparedStatement psBatch = con.prepareStatement("INSERT INTO idk(nume, hello) VALUES(?,?)");
        for (int i=0;i<2;i++)
        {
            psBatch.setString(1,"Produs "+i);
            psBatch.setString(2,"Buna");

            psBatch.addBatch();
        }
        psBatch.executeBatch();

        Statement stmt = con.createStatement();
        ResultSet rs = stmt.executeQuery("select * from idk");
        while(rs.next())
        {
            System.out.println("col1="+rs.getString("nume")+rs.getString("hello"));
        }

    }
}

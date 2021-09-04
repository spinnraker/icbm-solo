import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class MyJDBC{

    public static void main(String [] args){


        try {
            Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/icmb-tables", "root", "katana");

            Statement statement = connection.createStatement();

            System.out.println("Connection Successful.");

            ResultSet resultSet = statement.executeQuery("select * from questions;");

            while (resultSet.next()) {
                System.out.println(resultSet.getString("Question_Description"));
            }//While

            //ResultSet st = statement.executeQuery("select * questions");
        } catch (Exception e) {
            e.printStackTrace();
        }//Catch
    }//Main
}//Class

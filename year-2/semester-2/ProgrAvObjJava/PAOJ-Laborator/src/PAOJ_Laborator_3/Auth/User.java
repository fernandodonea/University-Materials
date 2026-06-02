package PAOJ_Laborator_3.Auth;

import java.util.Objects;

public abstract class User
{
    private String username;
    private String password;
    boolean isAuthenticated;
    Integer id;

    public abstract Integer generateId();
    public abstract void login();

    //constructor
    public User()
    {
        this.id=generateId();
    }

    //getteri
    public String getUsername() {return username;}
    public String getPassword() {return password;}
    public boolean isAuthenticated() {return isAuthenticated;}
    public Integer getId() {return id;}

    //setteri
    public void setUsername(String username) {this.username = username;}
    public void setPassword(String password) {this.password = password;}
    public void setAuthenticated(boolean authenticated) {isAuthenticated = authenticated;}
    public void setId(Integer id) {this.id = id;}


    public boolean isLoggedIn()
    {
        return this.isAuthenticated;
    }


    @Override
    public boolean equals(Object obj)
    {
        if (this==obj)return true; //daca e acelasi obiect (referinta)
        if (obj==null || getClass() != obj.getClass())return false;

        User user=(User) obj; //facem downcasting

        return Objects.equals(this.id, user.id);//2 obiecte sunt egale daca au acelasi id
    }

}

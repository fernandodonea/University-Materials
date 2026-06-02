package PAOJ_Laborator_3.Auth;

public class InMemoryUser extends User
{
    private static Integer contortId=0;

    private String[] usernames={"ana","popescu"};
    private String[] passwords={"123","admin"};



    @Override
    public Integer generateId()
    {
        contortId++;
        return contortId;
    }

    @Override
    public void login()
    {
        for(int i=0;i<usernames.length;i++)
        {
            if(usernames[i].equals(this.getUsername()) && passwords[i].equals(this.getPassword()))
            {
                this.setAuthenticated(true);
                return;
            }
        }
        this.setAuthenticated(false);


    }

    @Override
    public String toString()
    {
        return getId().toString();
    }
}

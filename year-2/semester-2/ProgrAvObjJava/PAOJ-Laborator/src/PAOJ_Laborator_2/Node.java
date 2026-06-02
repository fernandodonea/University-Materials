package PAOJ_Laborator_2;

public class Node
{
    private int info;
    private Node next;
    private Node prev;

    public Node(int info) 
    {
        this.info=info;
        this.next=null;
        this.prev=null;
    }

    
    public int getInfo(){return this.info;}
    public Node getNext(){return this.next;}
    public Node getPrev(){return this.prev;}
    
    public void setInfo(int info){this.info=info;}
    public void setNext(Node next){this.next=next;}
    public void setPrev(Node prev){this.prev=prev;}

    @Override
    public String toString()
    {
        StringBuilder displayNode= new StringBuilder();
        displayNode.append("info:").append(this.getInfo()).append("\n");

        displayNode.append("prev:");
        if(this.getPrev()==null)
            displayNode.append("null\n");
        else
            displayNode.append(this.getPrev().getInfo()).append("\n");

        displayNode.append("next:");
        if(this.getNext()!=null)
            displayNode.append(this.getNext().getInfo()).append("\n");
        else
            displayNode.append("null\n");

        return displayNode.toString();
    }
}

package PAOJ_Laborator_2;


public class List
{
    private Node head;

    public List()
    {
        this.head=null;
    }

    public Node getHead() {return this.head;}
    public void setHead(Node node)
    {
        this.head=node;
        if(head!=null)
        {
            this.head.setPrev(null);
        }
    }

    public Node addLast(int info)
    {
        Node newNode=new Node(info);

        if(getHead()==null)
        {
            setHead(newNode);
        }
        else
        {
            Node currentNode=getHead();
            while(currentNode.getNext()!=null)
            {
                currentNode=currentNode.getNext();
            }

            newNode.setPrev(currentNode);
            currentNode.setNext(newNode);
        }

        return newNode;//returnam referinta noului nod creat
    }

    public Node addFirst(int info)
    {
        Node newNode=new Node(info);

        if(getHead()==null)
        {
            setHead(newNode);
        }
        else
        {
            Node currentNode=getHead();

            currentNode.setPrev(newNode);
            newNode.setNext(currentNode);

            setHead(newNode);
        }

        return newNode;
    }

    public int size()
    {
        int size=0;
        Node currentNode=getHead();
        while(currentNode!=null)
        {
            size+=1;
            currentNode=currentNode.getNext();
        }
        return size;

    }

    public void addAtIndex(int info, int index)
    {
        if(index>size() || index<0)
        {
            System.out.println("Index invalid");
        }
        else if(index==0)
            this.addFirst(info);
        else if(index==size())
            this.addLast(info);
        else
        {
            int contor=0;

            Node currentNode=getHead();
            while(contor<index-1 && currentNode!=null)
            {
                currentNode=currentNode.getNext();
                contor+=1;
            }

            Node newNode=new Node(info);
            newNode.setNext(currentNode.getNext());
            newNode.setPrev(currentNode);

            currentNode.getNext().setPrev(newNode);
            currentNode.setNext(newNode);

        }

    }

    public boolean find(int value)
    {
        Node currentNode=getHead();
        while(currentNode!=null)
        {
            if(currentNode.getInfo()==value)
                return true;
            currentNode=currentNode.getNext();
        }
        return false;

    }

    public void remove(int value)
    {
        Node currentNode=getHead();

        while(currentNode!=null)
        {
            Node prevNode=currentNode.getPrev();
            Node nextNode=currentNode.getNext();

            if(currentNode.getInfo()==value)
            {
                if (prevNode == null && nextNode == null)
                {
                    setHead(null);
                }
                else if (prevNode == null && nextNode != null)
                {
                    setHead(nextNode);
                }
                else if (prevNode != null && nextNode == null)
                {
                    prevNode.setNext(null);
                }
                else if (prevNode != null && nextNode != null)
                {
                    prevNode.setNext(nextNode);
                    nextNode.setPrev(prevNode);
                }
            }

            currentNode=nextNode;
        }

    }

    public Node sort()
    {
        if(getHead()==null || head.getNext()==null)
            return getHead();

        boolean ok=true;
        do{
            Node currentNode=head;
            ok=false;
            while(currentNode.getNext()!=null)
            {
                if(currentNode.getInfo()>currentNode.getNext().getInfo())
                {
                    int a,b;
                    a=currentNode.getInfo();
                    b=currentNode.getNext().getInfo();
                    currentNode.setInfo(b);
                    currentNode.getNext().setInfo(a);

                    ok=true;
                }
                currentNode=currentNode.getNext();

            }

        }while(ok==true);

        return head;



    }
    public List(List other)
    {
        if(other!=null && other.getHead()!=null)
        {
            Node currentNode=other.getHead();
            while(currentNode!=null)
            {
                this.addLast(currentNode.getInfo()); //adaugam o copie la valoare
                currentNode=currentNode.getNext();
            }
        }
    }


    @Override
    public String toString()
    {
        StringBuilder displayList = new StringBuilder();
        Node currentNode = getHead();

        if (currentNode == null)
        {
            return "Lista vida";
        }
        else
        {
            while (currentNode != null)
            {
                displayList.append(currentNode.getInfo()).append("->");
                currentNode = currentNode.getNext();
            }
            displayList.append("null");
            return displayList.toString();
        }
    }

}

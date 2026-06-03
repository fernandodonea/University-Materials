package PAOJ_Laborator_5.EditorText;

import java.util.Comparator;

public class ByLengthComparator  implements Comparator<String>
{
    @Override
    public int compare(String o1, String o2)
    {
        int l1=0,l2=0;
        if(o1!=null)
            l1=o1.length();
        if(o2!=null)
            l2=o2.length();
        return Integer.compare(l1,l2);
    }
}

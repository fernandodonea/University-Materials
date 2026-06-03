package PAOJ_Laborator_5.EditorText;

import java.util.Comparator;

public class ByWordCountComparator implements Comparator<String>
{
    @Override
    public int compare(String o1, String o2)
    {
        TextEditor editor=new TextEditor();

        int c1=editor.countWords(o1);
        int c2=editor.countWords(o2);
        return Integer.compare(c1,c2);
    }
}

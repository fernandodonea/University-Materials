package PAOJ_Laborator_5.EditorText;

import paoj.lab.PAOJ_Laborator_5.EditorText.ByLengthComparator;
import paoj.lab.PAOJ_Laborator_5.EditorText.ByWordCountComparator;
import paoj.lab.PAOJ_Laborator_5.EditorText.TextEditor;

public class Main
{
    static void main()
    {
        TextEditor p=new TextEditor();
        String text="Ana are MERE si alune.  Aluneeeeeeeeeeeeeeeeeeeeeeee  si MERE?  Da! Alune si multe mere...";
        System.out.println(p.extractSentences(text));
        System.out.println(p.summarize(text));
        //p.sortSentence(text, new ByWordCountComparator());
        System.out.println(p.sortSentence(text, new ByLengthComparator()));
        System.out.println(p.sortSentence(text, new ByWordCountComparator()));

    }
}

package PAOJ_Laborator_5.EditorText;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class TextEditor implements TextProcessor, TextAnalyzer, TextSummarizer
{

    //functii ajutatoare
    private List<String> getWords(String text)
    {
        text=normalizeSpaces(text);
        return Arrays.stream(text.split("[ ,?.!]")).toList();

    }

    @Override
    public String normalizeSpaces(String text)
    {
        return text.replaceAll("[ ]+", " ").trim();
    }

    @Override
    public int countWords(String text)
    {
        if(text.isEmpty())
            return 0;
        else return getWords(text).size();
    }

    @Override
    public int countOccurrences(String text, String word)
    {
        List<String> words=getWords(text);
        int ct=0;
        for(var w:words)
        {
            System.out.println(w);
            if(w.equals(word))
                ct+=1;
        }
        return ct;
    }

    @Override
    public List<String> extractSentences(String text)
    {
        text=normalizeSpaces(text);
        List<String> rezultat= new ArrayList<>();

        String[] sentences=text.split("[.?!]+");
        for(var sentence:sentences)
        {
            sentence=sentence.trim();
            if(!sentence.isEmpty())
                rezultat.add(sentence);
        }
        return rezultat;

    }

    public String replaceWordWithLower(String text, String word)
    {
       return text.replaceAll(word, word.toLowerCase());
    }

    @Override
    public String summarize(String text)
    {
        StringBuilder summary= new StringBuilder();

        List<String> sentences=extractSentences(text);
        for (var sentence:sentences)
        {
            List <String> words=getWords(sentence);
            if(words.size()>0)
            {
                String firstWord=words.getFirst();
                System.out.println(firstWord);
                if(!firstWord.isEmpty())
                    summary.append(firstWord.charAt(0));
            }
            if(words.size()>1)
            {
                String secondWord =words.get(1);
                System.out.println(secondWord);
                if(!secondWord.isEmpty())
                    summary.append(secondWord.charAt(0));
            }

        }
        return summary.toString();
    }

    public List<String> sortSentence(String text, Comparator<String> comparator)
    {
        List<String> sentences=extractSentences(text);
        sentences.sort(comparator);
        return sentences;
    }



}

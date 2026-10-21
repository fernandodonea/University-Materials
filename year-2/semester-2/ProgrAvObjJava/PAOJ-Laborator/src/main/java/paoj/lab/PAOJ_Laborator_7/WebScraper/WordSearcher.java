package paoj.lab.PAOJ_Laborator_7.WebScraper;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class WordSearcher
{
    private List<String> wordsToSearch;
    private String htmlText;

    public WordSearcher(List<String> wordsToSearch, String htmlText) {
        this.wordsToSearch = wordsToSearch;
        this.htmlText = htmlText;
    }


    public int countWordsOccurent(String word)
    {
        if (htmlText == null || word == null || word.isEmpty()) {
            return 0;
        }

        List<String> words = Parser.getWordsFromText(htmlText);
        int count = 0;
        for (String w : words) {
            if (word.equalsIgnoreCase(w)) {
                count++;
            }
        }
        return count;
    }
    public Map<String, Integer> searchAllWords()
    {
        Map<String,Integer> results=new HashMap<>();
        if(wordsToSearch==null || wordsToSearch.isEmpty())
        {
            System.out.println("Eroare: liste de cuvinte e goala");
            return null;
        }

        for(String word:wordsToSearch)
        {
            int occurences=countWordsOccurent(word);
            results.put(word,occurences);
        }
        return results;
    }

    void printResults()
    {
        Map<String, Integer> results=searchAllWords();
        if(results==null || results.isEmpty())
        {
            System.out.println("Niciun cuvant nu a fost procesat ");
        }
        assert results != null;
        for(Map.Entry<String,Integer> entry: results.entrySet())
        {
            System.out.println(entry.getKey()+":"+entry.getValue());
        }
    }
}

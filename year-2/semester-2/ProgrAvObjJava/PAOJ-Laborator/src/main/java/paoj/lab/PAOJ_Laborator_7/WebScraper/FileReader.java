package paoj.lab.PAOJ_Laborator_7.WebScraper;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class FileReader
{
    private String path;
    private String fileNme;

    public FileReader(String path, String inputFilename) {
        this.path = path;
        this.fileNme = inputFilename;
    }


    public List<String> readWords()
    {
        List<String> words=new ArrayList<>();
        File file=new File(path+"/"+ fileNme);

        try(Scanner sc=new Scanner(file))
        {
            while (sc.hasNext())
            {
                String token = sc.next().trim();
                if (!token.isEmpty()) {
                    words.add(token);
                }
            }
            if (words.isEmpty())
            {
                System.err.println("Fisierul este gol");
            }
            else if(words.size()!=10)
            {
                System.err.println("Fisierul trebuie sa contine exact 10 cuvinte");
            }
        }
        catch (FileNotFoundException e)
        {
            System.out.println("fisierul nu a fost gasit");
        }
        catch (NoSuchElementException e)
        {
            System.out.println("Fisier gol");
        }
        return words;
    }
}

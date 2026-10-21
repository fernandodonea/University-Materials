package paoj.lab.PAOJ_Laborator_7.WebScraper;


import javax.swing.text.html.HTML;
import java.util.List;

public class WebScrapper
{
    private FileReader fileReader;
    private HtmlDownloader htmlDownloader;
    private WordSearcher wordSearcher;

    public WebScrapper(String url, String path, String fileName)
    {
        this.fileReader=new FileReader(path, fileName);
        this.htmlDownloader=new HtmlDownloader(url);
    }

    public void execute()
    {
        //citim cuvintele din fisier
        List<String> words=fileReader.readWords();

        //descarca html
        String html=htmlDownloader.downloadHTML();

        if(html==null)
        {
            System.out.println("Nu s-a putut descarca html-ul");
        }

        //curata html-ul
        String cleanText=Parser.cleanHTML(html);


        wordSearcher = new WordSearcher(words, html);
        wordSearcher.printResults();
    }


    static void main() {
        String url="https://www.gsp.ro/";
        String path="src/PAOJ_Laborator_7/WebScraper";
        String fileName="date.txt";

        WebScrapper scrapper=new WebScrapper(url, path, fileName);
        scrapper.execute();
    }

}

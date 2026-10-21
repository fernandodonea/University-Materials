package paoj.lab.PAOJ_Laborator_7.WebScraper;

import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;
import java.net.URL;

public class HtmlDownloader
{
    private URL url;

    public HtmlDownloader(String url)
    {
        try
        {
            this.url = new URL(url);
        }
        catch (MalformedURLException e)
        {
            System.out.println("URL invalid");
        }
    }

    public String downloadHTML()
    {
        if(url==null)
        {
            System.out.println(getClass()+": url invalid");
            return null;
        }

        try(InputStream is = url.openStream())
        {
            int ptr = 0;
            StringBuffer buffer = new StringBuffer();
            while ((ptr = is.read()) != -1)
            {
                buffer.append((char)ptr);
            }
            return buffer.toString();
        }
        catch (IOException e)
        {
            System.out.println("Nu s a putut citi website-ul");
        }

        return null;
    }
}

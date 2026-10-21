package paoj.lab.PAOJ_Laborator_7.WebScraper;

import java.util.Arrays;
import java.util.List;

public class Parser
{
    public static String cleanHTML(String html)
    {
        if(html==null)
            return "";

        //eliminima scripturile
        String noScript = html.replaceAll("(?s)<script.*?>.*?</script>", " ");

        //eliminam style
        String noStyle = noScript.replaceAll("(?s)<style.*?>.*?</style>", " ");

        //eliminam tagurile html
        String noTags = noStyle.replaceAll("<[^>]+>", " ");
        //normalizam spatiile
        return noTags.replaceAll("\\s+", " ").trim();
    }

    public static List<String> getWordsFromText(String text)
    {
        return Arrays.stream(text.split("[ ,?.!]")).toList();
    }



}

package PAOJ_Laborator_5.EditorText;

import java.util.List;

public interface TextAnalyzer {
    int countOccurrences(String text, String word);
    List<String> extractSentences(String text);
}

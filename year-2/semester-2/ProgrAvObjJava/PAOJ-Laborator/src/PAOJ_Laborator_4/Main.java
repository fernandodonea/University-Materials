package PAOJ_Laborator_4;

public class Main
{
    public  static void ex1_LongestAlphabeticalSubstring()
    {
        String str="abc123dab";
        int currLen =0, maxLen =0;
        int currStart =-1, maxStart =-1;
        for(int i=0;i<str.length()-1;i++)
        {
            char c=str.charAt(i);
            if(Character.isAlphabetic(c)==false)
            {
                currLen =0;
                currStart =-1;
                continue;
            }

            if(currLen==0)
            {
                currStart =i;
                currLen=1;
            }
            else
            {
                char prev=str.charAt(i-1);
                if(Character.isAlphabetic(prev) && prev<c)
                {
                    currLen++;
                }
                else{
                    currStart =i;
                    currLen =1;
                }
            }

            if(currLen > maxLen)
            {
                maxLen = currLen;
                maxStart = currStart;
            }
        }
        if(maxLen >0)
            System.out.println(str.substring(maxStart,maxStart+maxLen));
        else
            System.out.println("nah");

    }
    public static void ex2_twoStringsPermutations()
    {
        String str1,str2;
        str1="abc";
        str2="cab";

//        Scanner sc = new Scanner(System.in);
//        str1=sc.nextLine();
//        str2=sc.nextLine();


        boolean ok=true;

        if(str1.length()!=str2.length())
        {
            ok=false;
        }
        else
        {
            int [] fr1 = new int[27];
            int [] fr2 = new int[27];
            for(int i=0;i<27;i++)
                fr1[i]=fr2[i]=0;

            for(int i=0;i<str1.length();i++)
            {
                int x,y;
                x=str1.charAt(i)-'a';
                y=str2.charAt(i)-'a';

                fr1[x]++;
                fr2[y]++;
            }

            for(int i=0;i<27;i++)
            {
                if(fr1[i]!=fr2[i])
                {
                    ok=false;
                    break;
                }
            }

        }

        if(ok)
        {
            System.out.println("Stringul ''"+str1+"'' este e o permutarea a stringului ''"+str2+"''");
        }
        else
        {
            System.out.println("Stringul ''"+str1+"'' NU este e o permutarea a stringului ''"+str2+"''");
        }

    }


    static void main() {
        ex1_LongestAlphabeticalSubstring();
        ex2_twoStringsPermutations();
    }
}

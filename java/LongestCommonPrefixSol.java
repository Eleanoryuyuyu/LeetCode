import java.util.HashMap;
import java.util.Scanner;

public class LongestCommonPrefixSol {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length==0){
            return "";
        }
        int min = Integer.MAX_VALUE;
        String min_strs = "";
        for(int i=0;i<strs.length;i++){
            if(min>strs[i].length()){
                min_strs=strs[i];
                min=strs[i].length();
            }
        }
        if(min==0){
            return "";
        }
            for(int i = min;i>=0;i--){
                String standard = min_strs.substring(0,i);
                int j=0;
                for (j=0;j<strs.length;j++){
                    if(strs[j].substring(0,i).equals(standard)){
                        continue;
                    }else
                        break;
                }
                if(j==strs.length){
                    return standard;
                }
            }

        return "";

    }

    public static void main(String[] args){
        LongestCommonPrefixSol lcp=new LongestCommonPrefixSol();
        String[] strs = new String[3];
        Scanner scan = new Scanner(System.in);
        for (int i=0;i<3;i++){
            String temp = scan.next();
            strs[i]= temp;
        }
        String ans = lcp.longestCommonPrefix(strs);
        System.out.println(ans);
    }
}

public class Longest_Palindromic_Substring_5 {
    public String longestPalindrome(String s) {
        if(s==null)
            return null;
        StringBuffer sub =null;
        for(int i=0;i<s.length();i++){
            sub.setCharAt(i,s.charAt(i));
            if(sub.equals(sub.reverse()))
                break;
        }
        return sub.toString();

    }
    public static void main(String[] args){
        Longest_Palindromic_Substring_5 lps = new Longest_Palindromic_Substring_5();
        String s = "bab";
        StringBuffer s1 = new StringBuffer(s);
        //System.out.println(lps.longestPalindrome(s));
        System.out.println(s1.equals(s1.reverse()));
    }
}

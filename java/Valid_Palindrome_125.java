public class Valid_Palindrome_125 {
    public boolean isPalindrome(String s) {
        s=s.replaceAll("[^a-zA-Z0-9]","").toLowerCase();
        int length = s.length();
        int i=0,j=length-1;
        while (i<j){
            if(s.charAt(i)!=s.charAt(j)){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
    public boolean isPalindrome2(String s){
        s = s.replaceAll("[^a-zA-Z0-9]","").toLowerCase();
        String rev = new StringBuffer(s).reverse().toString();
        return s.equals(rev);

    }

    public static void main(String[] args){
        String s = new String("race a car");
        Valid_Palindrome_125 vp = new Valid_Palindrome_125();
        System.out.println(vp.isPalindrome2(s));

    }
}

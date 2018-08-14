import java.util.Scanner;

public class PalindromeNumber {
    public boolean isPalindrome(int x) {
        int result=0;
        int a=x;
        while (x!=0){
            result=result*10+x%10;
            x=x/10;
        }
        if(a<0)
            result=result*-1;
        return a==result;

    }

//    public boolean isPalindrome(int x) {
//        String str = String.valueOf(x);
//        int start = 0;
//        int end = str.length() - 1;
//        while(start < end){
//            if(str.charAt(start++) != str.charAt(end--)) return false;
//        }
//        return true;
//    }

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int x = in.nextInt();
        PalindromeNumber pn = new PalindromeNumber();
        boolean result = pn.isPalindrome(x);
        System.out.println(result);


    }
}

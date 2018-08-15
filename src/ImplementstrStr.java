import java.util.Scanner;

public class ImplementstrStr {
    public int strStr(String haystack, String needle) {
        return (haystack.indexOf(needle));
    }

    public static void main(String[] args){
        Scanner str = new Scanner(System.in);
        String haystack = str.next();
        String needle = str.next();
        ImplementstrStr is = new ImplementstrStr();
        int i = is.strStr(haystack,needle);
        System.out.println(i);
    }
}

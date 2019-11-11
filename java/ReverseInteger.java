import java.util.*;

public class ReverseInteger {
    public int reverse(int x) {
        long result=0;
        while (x!=0){
            result=result*10+x%10;
            x=x/10;

        }
        if (result> Integer.MAX_VALUE || result < Integer.MIN_VALUE)
            return 0;
        return (int) result;

    }

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
         int x = in.nextInt();
        ReverseInteger ri = new ReverseInteger();
         int result = ri.reverse(x);
         System.out.println(result);


    }
}

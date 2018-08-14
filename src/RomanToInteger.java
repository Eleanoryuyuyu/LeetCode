import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class RomanToInteger {
    public int romanToInt(String s) {
        Map<String,Integer> map = new HashMap<String, Integer>(){
            {
                put("I",1);
                put("V",5);
                put("X",10);
                put("L",50);
                put("C",100);
                put("D",500);
                put("M",1000);
            }
        };
        int sum=0;
        int len=s.length();
        for(int i=0;i<len;i++){
            int value = map.get(s.charAt(i)+"");
            System.out.println(s.charAt(i));
            if(i<len-1 && value<map.get(s.charAt(i+1)+""))
                sum-=value;
            else
                sum+=value;
        }
        return sum;

    }

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        RomanToInteger rti = new RomanToInteger();
        int sum = rti.romanToInt(s);
        System.out.println(sum);
    }
}

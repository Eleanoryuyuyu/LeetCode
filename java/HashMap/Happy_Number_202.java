package HashMap;

import java.util.HashMap;
import java.util.Map;

public class Happy_Number_202 {
    Map<Integer,Integer>map = new HashMap<>();
    public boolean isHappy(int n) {
        if(n==0)
            return false;
        else if(n==1)
            return true;
        String s  = n+"";
        int sum = 0;
        int index=1;
        for (int i=0;i<s.length();i++){
            sum +=(s.charAt(i)-'0')*(s.charAt(i)-'0');
        }

        if(sum==1)
            return true;
        if(map.containsKey(sum))
            return false;
        else
            map.put(sum,index++);
        return isHappy(sum);
    }
    public static void main(String[] args){
        Happy_Number_202 hn = new Happy_Number_202();
        System.out.println(hn.isHappy(16));
    }
}

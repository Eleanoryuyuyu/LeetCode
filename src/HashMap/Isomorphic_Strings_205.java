package HashMap;

import java.util.HashMap;
import java.util.Map;

public class Isomorphic_Strings_205 {
    public boolean isIsomorphic(String s, String t) {
        Map<Character,Integer> map = new HashMap<>();
        Map<Character,Integer> map2 = new HashMap<>();
        for (int i=0;i<s.length();i++){
            if(map.put(s.charAt(i),i)!=map2.put(t.charAt(i),i))
                return false;
        }
         return true;
    }

    public static void main(String[] args){
        Isomorphic_Strings_205 is = new Isomorphic_Strings_205();
        System.out.println(is.isIsomorphic("foo","bar"));
    }
}

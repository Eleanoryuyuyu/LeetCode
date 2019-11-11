import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Longest_Substring_Without_Repeating_Characters_3 {
    public int lengthOfLongestSubstring(String s) {
        int len = s.length();
        int i=0,j=0,length=0;
        Set<Character> sub = new HashSet<>();
       while (i<len && j<len){
           if(!sub.contains(s.charAt(j))){
               sub.add(s.charAt(j++));
               length = Math.max(length,j-i);
           }else {
               sub.remove(s.charAt(i++));
           }
       }
       System.out.println(sub);
       return length;
    }

    /**
     * 优化滑动窗口
     * @param s
     * @return
     */
    public int lengthOfLongestSubstring2(String s){
        int len = s.length();
        int i=0,j=0,ans=0;
        Map<Character,Integer> map = new HashMap<>();
        for(;j<len;j++){
            if(map.containsKey(s.charAt(j))){
                i = Math.max(map.get(s.charAt(j)),i);
            }
            ans = Math.max(ans,j-i+1);
            map.put(s.charAt(j),j+1);
        }
        System.out.println(map);
        return ans;
    }

    public static void main(String[] args){
        String s = "abcabcbb";
        Longest_Substring_Without_Repeating_Characters_3 ls = new Longest_Substring_Without_Repeating_Characters_3();
        System.out.println(ls.lengthOfLongestSubstring2(s));
    }
}


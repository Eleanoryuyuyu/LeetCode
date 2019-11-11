package HashMap;

import java.util.HashMap;
import java.util.Map;

public class Contains_Duplicate_217 {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer,Integer> map = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if(map.containsKey(nums[i]))
                return true;
            else
                map.put(nums[i],i);
        }
        return false;
    }
    public static void main(String[] args){
        Contains_Duplicate_217 cd = new Contains_Duplicate_217();
        int[] nums={1,2,3,4};
        System.out.println(cd.containsDuplicate(nums));
    }
}

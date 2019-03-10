import java.util.Arrays;
import java.util.HashMap;

public class Single_Number_136 {
    public int singleNumber(int[] nums) {
        Arrays.sort(nums);
        for(int i=0;i<nums.length-1;i+=2){
            if(nums[i]!=nums[i+1])
                return nums[i];
        }
        return nums[nums.length-1];
    }
    public int singleNumber2(int[] nums){
        HashMap<Integer,Integer> ht = new HashMap<>();
        for(int i=0;i<nums.length-1;i++){
            if(ht.containsKey(nums[i])){
                ht.remove(nums[i]);
            }else {
                ht.put(nums[i],1);
            }
        }
        return (int)ht.keySet().toArray()[0];
    }
    public static void main(String[] args){
        int[] nums = {2,1,2};
        Single_Number_136 sn = new Single_Number_136();
        System.out.println(sn.singleNumber2(nums));
    }
}

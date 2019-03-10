import java.util.Arrays;

public class Single_Number_137 {
    public int singleNumber(int[] nums) {
        Arrays.sort(nums);
        for(int i=0;i<nums.length-2;i+=3){
            if(nums[i]!=nums[i+1]){
                return nums[i];
            }
        }
        return nums[nums.length-1];
    }
    public static void main(String[] args){
        int[] nums = {0,1,0,1,0,1,99};
        Single_Number_137 sn2 = new Single_Number_137();
        System.out.println(sn2.singleNumber(nums));
    }
}

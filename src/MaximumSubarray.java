public class MaximumSubarray {
    public int maxSubArray(int[] nums) {
        int max=Integer.MIN_VALUE;
        int sum = 0;
        for(int i=0;i<nums.length;i++){
            sum=sum+nums[i];
            if(max<sum)
                max=sum;
            if(sum<0)
                sum=0;
        }
        return max;
    }

    public static void main(String[] args){
        int[] nums={-2,1,-3,4,-1,2,1,-5,4};
        MaximumSubarray ms=new MaximumSubarray();
        int sum = ms.maxSubArray(nums);
        System.out.println(sum);
    }
}

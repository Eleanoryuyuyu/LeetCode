import java.util.Scanner;

public class SearchInsertPosition {
    public int searchInsert(int[] nums, int target) {
        if(target<nums[0])
            return 0;
        if(target>nums[nums.length-1])
            return nums.length;
        int result = 0;
        for( int i=0;i<nums.length;i++){
            if(nums[i]==target)
                result= i;
            else if(target>nums[i]&&target<nums[i+1])
                result= i+1;
        }
        return result;
    }
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int[] nums={1,3,5,6};
        int target=in.nextInt();
        SearchInsertPosition sip=new SearchInsertPosition();
        int result=sip.searchInsert(nums,target);
        System.out.println(result);

    }
}

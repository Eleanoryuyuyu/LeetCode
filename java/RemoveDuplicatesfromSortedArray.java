import java.util.Scanner;

public class RemoveDuplicatesfromSortedArray {
    public int removeDuplicates(int[] nums) {
        int j=1;
        for(int i=1;i<nums.length;i++){
            if(nums[i]>nums[i-1]){
                nums[j++]=nums[i];

            }
        }

        return j;


    }

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int len1=in.nextInt();
        int[] nums = new int[len1];
        for(int i=0;i<len1;i++){
            nums[i]=in.nextInt();
        }
        RemoveDuplicatesfromSortedArray rd = new RemoveDuplicatesfromSortedArray();
        rd.removeDuplicates(nums);
        //System.out.println(len);


    }
}

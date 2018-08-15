import java.util.Scanner;

public class RemoveElement {
    public int removeElement(int[] nums, int val) {
        int j =0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]!=val)
                nums[j++]=nums[i];
        }
        return j++;
    }
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int len = in.nextInt();
        int val = in.nextInt();
        int[] nums = new int[len];
        for (int i=0;i<len;i++){
            nums[i]=in.nextInt();
        }
        RemoveElement re=new RemoveElement();
        re.removeElement(nums,val);
//        int len1= re.removeElement(nums,val);
//        for (int i=0;i<len1;i++){
//            System.out.println(nums[i]);
//        }

    }
}

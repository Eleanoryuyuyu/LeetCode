public class Median_of_Two_Sorted_Arrays_4 {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        double result=0.0;
        int[] answer = new int[nums1.length+nums2.length];
        int i =0,j=0,k=0;
        while (i<nums1.length && j<nums2.length){
            if(nums1[i]<nums2[j]){
                answer[k]=nums1[i];
                i++;
                k++;
            }else if(nums1[i]>nums2[j]){
                answer[k]=nums2[j];
                j++;
                k++;
            }else {
                answer[k++]=nums1[i++];
                answer[k++]=nums2[j++];
            }
        }
        while (i<nums1.length){
            answer[k++]=nums1[i++];
        }
        while (j<nums2.length){
            answer[k++]=nums2[j++];
        }
        if((nums1.length+nums2.length)%2==0){
            result = (answer[answer.length/2-1]+answer[answer.length/2])/2.0;
        } else
            result = answer[answer.length/2]/1.0;
        for(int m:answer)
            System.out.println(m);

        return result;

    }
    public static void main(String[] args){
        Median_of_Two_Sorted_Arrays_4 mtsa = new Median_of_Two_Sorted_Arrays_4();
        int[] nums1 = {};
        int[] nums2 = {1};
        System.out.println(mtsa.findMedianSortedArrays(nums1,nums2));
    }
}

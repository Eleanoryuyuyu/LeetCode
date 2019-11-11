public class MergeSortedArray {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] temp =new int[m+n];
        int i =0,j=0,k=0;
        while (i!=m && j!=n){
            if(nums1[i]<nums2[j]){
                temp[k++]=nums1[i];
                i++;
            }else {
                temp[k++]=nums2[j];
                j++;
            }
        }

        while (i!=m){
            temp[k++]=nums1[i++];
        }
        while (j!=n){
            temp[k++]=nums2[j++];
        }

        for(i=0;i<k;i++){
            nums1[i]=temp[i];
        }

    }

    public static void main(String[] args){
        MergeSortedArray msa =new MergeSortedArray();
        int[] nums1 = new int[6];
        nums1[0]=1;
        nums1[1]=2;
        nums1[2]=3;
        int[] nums2 = {2,5,6};
        msa.merge(nums1,3,nums2,3);
        for(int i=0;i<6;i++){
            System.out.println(nums1[i]);
        }
    }
}

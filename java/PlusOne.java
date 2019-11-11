public class PlusOne {
    public int[] plusOne(int[] digits) {
        int len = digits.length;
        int[] results=null;
        if(digits==null||len==0){
            results=new int[len+1];
            results[0]=1;
        }
        else if(digits[len-1]<9){
            digits[len-1]=digits[len-1]+1;
            results=digits;
        }
        else if(digits[len-1]==9){
            int i;
            for(i=len-2;i>=0;i--){
                if(digits[i]!=9){
                    digits[i+1]=0;
                    digits[i]=digits[i]+1;
                    break;
                }else {
                    digits[i+1]=0;
                }
            }
            if(i==-1 && digits[0]==9){
                digits[0]=0;
                results = new int[len+1];
                System.arraycopy(digits, 0, results, 1, len);
                results[0]=1;
            }else {
                results=digits;
            }
        }
        return results;
    }

    public static void main(String[] args){
        PlusOne po=new PlusOne();
        int[] digits={5,8,7,8,8};//测试数据
        int[] results=po.plusOne(digits);
        for(int i=0;i<results.length;i++)
            System.out.println(results[i]);

    }
}

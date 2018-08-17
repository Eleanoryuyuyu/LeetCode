public class CountandSay {
    public String countAndSay(int n) {
       if(n==1)
           return "1";
       String str = countAndSay(n-1)+"*";
       char[] c = str.toCharArray();
       String s="";
       int count=1;
       for(int i=0;i<c.length-1;i++)
       {
           if(c[i]==c[i+1])
           {
               count++;
           }else {
               s=s+count+c[i];
               count=1;
           }
       }


        return s;
    }

    public static void main(String[] args){
        CountandSay cs = new CountandSay();
        int n=4; //测试用数据
        String s =cs.countAndSay(n);
        System.out.println(s);
    }
}

public class AddBinary {
    public String addBinary(String a, String b) {
        int i=a.length()-1,j=b.length()-1;
        int max=Math.max(i,j);
        int len=max+1;
        char[] aa=a.toCharArray();
        char[] bb=b.toCharArray();
        char[] res=new char[len+1];
        int flag=0;
        while (i>=0&&j>=0){
            if(aa[i]=='1' && bb[j]=='1'){
                res[len--]= flag==0? '0':'1';
                flag=1;
            }else if(aa[i]=='0' && bb[j]=='0'){
                res[len--]= flag==0? '0':'1';
                flag=0;
            }else {
                if(flag==1){
                    res[len--]='0';
                    flag=1;
                }else {
                    res[len--]='1';
                    flag=0;
                }
            }
            i--;
            j--;
        }
        while (i>=0){
            if(flag==0){
                res[len--]=aa[i];
            }else {
                if(aa[i]=='1'){
                    res[len--]='0';
                    flag=1;
                }else {
                    res[len--]='1';
                    flag=0;
                }
            }
            i--;
        }

        while (j>=0){
            if(flag==0){
                res[len--]=bb[j];
            }else {
                if(bb[j]=='1'){
                    res[len--]='0';
                    flag=1;
                }else {
                    res[len--]='1';
                    flag=0;
                }
            }
            j--;
        }

        if(flag==1){
            res[len--]='1';
        }else {
            res[len--]=' ';
        }

        return new String(res).trim();//去首位空格
    }

    public static void main(String[] args){
        String a="11"; //测试数据
        String b="1";
        AddBinary ab =new AddBinary();
        String sum =ab.addBinary(a,b);
        System.out.println(sum);
    }
}

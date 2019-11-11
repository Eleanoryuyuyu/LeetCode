public class LengthofLastWord {
    public int lengthOfLastWord(String s) {
        if(s==null || s.length()==0)
            return 0;
        if(s.contains(" ")){
            String[] list = s.split(" ");
            if(list[list.length-1]==" ")
                return list[list.length-2].length();
            else
                return list[list.length-1].length();

        }else {
            return s.length();
        }


    }

    public static void main(String[] args){
        String s="hello world welcome";
        LengthofLastWord llow = new LengthofLastWord();
        int n =llow.lengthOfLastWord(s);
        System.out.println(n);
    }
}

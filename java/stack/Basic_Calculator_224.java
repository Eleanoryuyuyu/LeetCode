package stack;

import java.util.Stack;

public class Basic_Calculator_224 {
    public int calculate(String s) {
        int length = s.length();
        int sign =1;
        int cur;
        int result = 0;
        Stack<Integer> stack = new Stack<>();
        for(int i=0;i<length;i++){
            if (Character.isDigit(s.charAt(i))){
                cur = s.charAt(i)-'0';
                while (i+1<length && Character.isDigit(s.charAt(i+1))){
                    cur = cur*10+(s.charAt(i+1)-'0');
                    i++;
                }result += cur*sign;
            }else if(s.charAt(i)=='+'){
                sign=1;
            }else  if(s.charAt(i)=='-'){
                sign=-1;
            }else if(s.charAt(i)=='('){
                stack.push(result);
                stack.push(sign);
                result=0;
                sign=1;
            }else if(s.charAt(i)==')'){
                result = stack.pop()*result+stack.pop();
            }
        }
        return result;
    }
    public static void main(String[] args){
        String s = "(1+(4+5+2)-3)+(6+8)";
        Basic_Calculator_224 bc = new Basic_Calculator_224();
        System.out.println(bc.calculate(s));
    }
}

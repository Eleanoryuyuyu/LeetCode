import java.util.Scanner;
import java.util.Stack;

public class ValidParentheses {
    public boolean isValid(String s) {
        if(s.length()==0)
            return true;
        if(s.charAt(0)==')'||s.charAt(0)==']'||s.charAt(0)=='}')
            return false;
        Stack<Character> stack=new Stack<Character>();
        int len=s.length();
        stack.add(s.charAt(0));
        for(int i =1;i<len;i++){
            char now=s.charAt(i);
            if(now==')'||now==']'||now=='}'){
                if(stack.size()==0)
                    return false;
                char temp=stack.pop();
                if(now==')'&& temp!='(')
                    return  false;
                if(now==']'&& temp!='[')
                    return  false;
                if(now=='}'&& temp!='{')
                    return  false;
            }
            else
                stack.push(now);
        }

        return stack.empty();

    }

    public static void main(String[] args){
        ValidParentheses vp=new ValidParentheses();
        Scanner scan=new Scanner(System.in);
        String s = scan.next();
        System.out.println(vp.isValid(s));
    }
}

package stack;

import java.util.ArrayList;
import java.util.List;

public class MinStack_155 {
    private List<int[]> stack;
    private int min;
    public MinStack_155() {
       stack = new ArrayList<int[]>();
    }
    public void push(int x) {
        int[] arr = new int[2];
        arr[0]=x;
        arr[1]=stack.isEmpty()?x:Math.min(x,min);
        min = arr[1];
        stack.add(arr);
    }

    public void pop() {
        if(!stack.isEmpty()){
            stack.remove(stack.size()-1);
            min = stack.isEmpty()?0:stack.get(stack.size()-1)[1];
        }

    }

    public int top() {
        return stack.get(stack.size()-1)[0];
    }

    public int getMin() {
        return min;
    }
    public static void main(String[] args){
        MinStack_155 minStack = new MinStack_155();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        System.out.println(minStack.getMin());
    }
}

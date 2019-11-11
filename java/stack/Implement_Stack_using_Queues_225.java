package stack;

import java.util.LinkedList;
import java.util.Queue;

public class Implement_Stack_using_Queues_225 {
    private Queue<Integer> stack;
    public Implement_Stack_using_Queues_225() {
        stack = new LinkedList<>();
    }

    /** Push element x onto stack. */
    public void push(int x) {
        stack.add(x);
        for (int i=0;i<stack.size()-1;i++){
            stack.add(stack.peek());
            stack.poll();
        }
    }

    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        return stack.poll();
    }

    /** Get the top element. */
    public int top() {
        return stack.peek();
    }

    /** Returns whether the stack is empty. */
    public boolean empty() {
        return stack.isEmpty();
    }
    public static void main(String[] args){
        Implement_Stack_using_Queues_225 stack = new Implement_Stack_using_Queues_225();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        System.out.println(stack.top());
        stack.pop();
        System.out.println(stack.top());
        System.out.println(stack.empty());
    }
}

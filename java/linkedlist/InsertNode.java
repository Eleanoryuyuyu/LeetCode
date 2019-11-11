package linkedlist;

import java.util.Scanner;

public class InsertNode {
    public static void main(){
        ListNode l1=null;
        ListNode point1=null;
        int[] temp =new int[3];
        for (int i=0;i<3;i++){
            Scanner in = new Scanner(System.in);
            temp[i]=in.nextInt();
            ListNode L=new ListNode(temp[i]);
            if(l1==null){
                l1=L;
                return;
            }
            point1=l1;
            while (point1.next!=null){
                point1=point1.next;
            }
            point1.next=l1;
            }
            point1=l1;
        for(int j=0;j<3;j++){
            System.out.println(point1.val+" ");
            point1=point1.next;
        }
    }




}

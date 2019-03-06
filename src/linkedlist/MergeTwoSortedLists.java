package leet;

import linkedlist.ListNode;

import java.util.Scanner;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */



public class MergeTwoSortedLists {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1==null||l2==null)
            return l1!=null? l1:l2;
        ListNode head=new ListNode(0);
        ListNode pre=head;
        if(l1!=null&&l2!=null){
            if(l1.val<l2.val){
                pre.next=l1;
                l1=l1.next;

            }else {
                pre.next=l2;
                l2=l2.next;
            }
            pre=pre.next;
        }
        while (l1!=null){
            pre.next=l1;
            pre=pre.next;
            l1=l1.next;
        }
        while (l2!=null){
            pre.next=l2;
            pre=pre.next;
            l2=l2.next;
        }

        return head.next;

    }


    public static void main(String[] args){
        MergeTwoSortedLists mtsl=new MergeTwoSortedLists();
        //Scanner in = new Scanner(System.in);
        ListNode l1=null;
        ListNode l2=null;
        ListNode point1=null;
        ListNode point2=null;
        int[] temp =new int[3];
        for (int i=0;i<3;i++){
            Scanner in = new Scanner(System.in);
           temp[i]=in.nextInt();
           ListNode L =new ListNode(temp[i]);
           if(l1==null){
               l1=L;
               return;
           }
           point1=l1;
           while (point1.next!=null){
               point1=point1.next;
           }
           point1.next=L;
        }
        point1=l1;
        for(int j=0;j<3;j++){
            System.out.print(point1.val+" ");
            point1=point1.next;
        }

    }
}

package linkedlist;

/**
 * 两个人跑步，速度有块有慢，如果跑道是环形的，一定会相遇
 */

public class Linked_List_Cycle_141 {
    public boolean hasCycle(ListNode head) {
        if (head == null)
            return false;
        ListNode slow = head;
        ListNode fast = head;
        while (slow != null && fast != null && fast.next != null) {
            if (slow == fast)
                return true;
        }
        return false;
    }
    public static void main(String[] args){
        ListNode L = new ListNode(3);
        ListNode L1 = new ListNode(2);
        ListNode L2 = new ListNode(0);
        ListNode L3 = new ListNode(-4);
        L.next=L1;
        L1.next=L2;
        L2.next=L3;
        L3.next=L1;
        Linked_List_Cycle_141 lc = new Linked_List_Cycle_141();
        System.out.println(lc.hasCycle(L));
}







































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































}

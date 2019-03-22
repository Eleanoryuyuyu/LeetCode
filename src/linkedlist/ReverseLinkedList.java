package linkedlist;

public class ReverseLinkedList {
    public ListNode reverseList(ListNode head) {
        ListNode cur;
        ListNode pre;
        ListNode nxt;
        pre = null;
        cur = head;
        while (cur!=null){
            nxt = cur.next;
            cur.next = pre;
            pre = cur;
            cur = nxt;

        }
        return pre;

    }
}

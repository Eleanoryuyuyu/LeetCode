package linkedlist;

public class RemoveDuplicatesfromSortedList_83 {
    public ListNode deleteDuplicates(ListNode head) {
        if(head==null || head.next==null){
            return head;
        }
        ListNode cur = head;
        ListNode nxt = cur.next;
        while (nxt!=null){
            if(cur.val==nxt.val){
                nxt=nxt.next;
                cur.next=nxt;
            }else {
                cur=cur.next;
                nxt=nxt.next;
            }
        }

        return head;

    }

    public static void main(String[] args){
        ListNode node1 = new ListNode(1);
        ListNode node2 = new ListNode(1);
        ListNode node3 = new ListNode(2);

        node1.next=node2;
        node2.next=node3;

        ListNode tmp = node1;
        while (tmp.next!=null){
            System.out.print(tmp.val);
            System.out.print("->");
            tmp = tmp.next;
        }
        System.out.println(tmp.val);

        RemoveDuplicatesfromSortedList_83 rm = new RemoveDuplicatesfromSortedList_83();
        ListNode head = rm.deleteDuplicates(node1);
        ListNode tmp2 = head;
        while (tmp2.next!=null){
            System.out.print(tmp2.val);
            System.out.print("->");
            tmp2 = tmp2.next;
        }
        System.out.println(tmp2.val);

    }
}

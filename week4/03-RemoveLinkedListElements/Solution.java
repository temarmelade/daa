/**
 * LeetCode 203: Remove Linked List Elements
 *
 * Remove every node whose value equals val.
 * A dummy node makes it easier to remove the original head.
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode current = dummy;

        while (current.next != null) {
            if (current.next.val == val) {
                current.next = current.next.next;
            } else {
                current = current.next;
            }
        }

        return dummy.next;
    }
}

/**
 * LeetCode 83: Remove Duplicates from Sorted List
 *
 * The list is sorted, so duplicate values are adjacent.
 * If current and current.next have the same value, skip current.next.
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode current = head;

        while (current != null && current.next != null) {
            if (current.val == current.next.val) {
                current.next = current.next.next;
            } else {
                current = current.next;
            }
        }

        return head;
    }
}

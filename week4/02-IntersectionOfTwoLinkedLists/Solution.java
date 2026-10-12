/**
 * LeetCode 160: Intersection of Two Linked Lists
 *
 * Brute-force approach: for each node in list A, scan list B.
 * Intersection means the same node object, not merely equal values.
 */
class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode a = headA;

        while (a != null) {
            ListNode b = headB;

            while (b != null) {
                if (a == b) {
                    return a;
                }
                b = b.next;
            }

            a = a.next;
        }

        return null;
    }
}

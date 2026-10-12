import java.util.ArrayList;
import java.util.List;

/**
 * LeetCode 234: Palindrome Linked List
 *
 * Beginner-friendly approach: copy values to a list,
 * then compare values from both ends.
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        List<Integer> values = new ArrayList<>();

        ListNode current = head;
        while (current != null) {
            values.add(current.val);
            current = current.next;
        }

        int left = 0;
        int right = values.size() - 1;

        while (left < right) {
            if (!values.get(left).equals(values.get(right))) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
}

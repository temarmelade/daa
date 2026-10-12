# 4. Palindrome Linked List

## Problem

Given the head of a singly linked list, determine whether its values read the same forward and backward.

Examples:
- `1 -> 2 -> 2 -> 1` is a palindrome.
- `1 -> 2` is not a palindrome.
- An empty list or a one-node list is a palindrome.

## Approach

A singly linked list is easy to traverse forward, but it is not easy to move backward. My beginner-friendly approach copies the node values into an `ArrayList`.

1. Traverse the list and store each value in the list.
2. Set `left` to the first index and `right` to the last index.
3. Compare `values[left]` and `values[right]`.
4. If they differ, return `false`.
5. If they match, move `left` forward and `right` backward.
6. If all pairs match, return `true`.

The `ArrayList` grows as values are added, so the solution does not depend on a hard-coded array size.

The implementation in `Solution.java` is:
```java
import java.util.ArrayList;
import java.util.List;

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
```

## Written Trace

Input: `1 -> 2 -> 2 -> 1`

After copying, the array is `[1, 2, 2, 1]`.

| Comparison | Left value | Right value | Result |
|---|---:|---:|---|
| 1 | 1 | 1 | Equal; move inward |
| 2 | 2 | 2 | Equal; move inward |
| Stop | left >= right | — | All pairs matched |

Output: `true`

Another input: `1 -> 2 -> 3`

Array: `[1, 2, 3]`

The first comparison is `1` versus `3`. They differ, so the method returns `false`.

## Time Complexity

**Time Complexity: O(n)**

Copying the linked-list values takes O(n) time. Comparing values from both ends takes at most O(n/2), which is O(n). The total is O(n) + O(n), so the overall time complexity is O(n).

## Space Complexity

**Space Complexity: O(n)**

The array or `ArrayList` stores one value for each node. If the list has `n` nodes, the extra storage grows linearly with `n`.

## Challenges and Testing

A singly linked list does not provide direct access to the last node, so comparing from both ends directly is awkward. Copying the values into an array makes the comparison straightforward.

Useful tests:
- Empty list -> `true`
- One node: `[5]` -> `true`
- Even palindrome: `[1,2,2,1]` -> `true`
- Odd palindrome: `[1,2,3,2,1]` -> `true`
- Not a palindrome: `[1,2,3]` -> `false`
- Different middle-side values: `[1,2,3,1]` -> `false`

## Reflection / Improvement

A more space-efficient approach uses **O(n) time and O(1) extra space**: find the middle with slow and fast pointers, reverse the second half of the list, then compare both halves. This avoids storing all values but requires careful pointer manipulation. The array approach is easier to understand and is a reasonable first solution for learning.

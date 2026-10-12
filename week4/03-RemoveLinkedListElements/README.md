# 3. Remove Linked List Elements

## Problem

Given the head of a linked list and an integer `val`, remove every node whose value equals `val`. Return the head of the remaining list.

## Approach

I create a dummy node before the original head. This makes removing the first node work in the same way as removing any other node.

- Set `dummy.next = head`.
- Start `current` at `dummy`.
- While `current.next` exists, check the value of the next node.
- If `current.next.val == val`, skip that node with `current.next = current.next.next`.
- Otherwise, move `current` forward.
- Return `dummy.next`, which points to the new head.

When a node is removed, I do not move `current` immediately. Its new next node must also be checked, because it might contain the target value too.

## Written Trace

Input: `1 -> 2 -> 6 -> 3 -> 6 -> null`, with `val = 6`.

Initially: `dummy -> 1 -> 2 -> 6 -> 3 -> 6`

| Current node | Next value | Action | List after action |
|---|---:|---|---|
| dummy | 1 | Keep node; move forward | `1 -> 2 -> 6 -> 3 -> 6` |
| 1 | 2 | Keep node; move forward | `1 -> 2 -> 6 -> 3 -> 6` |
| 2 | 6 | Skip the `6` node | `1 -> 2 -> 3 -> 6` |
| 2 | 3 | Keep node; move forward | `1 -> 2 -> 3 -> 6` |
| 3 | 6 | Skip the `6` node | `1 -> 2 -> 3` |

Output: `1 -> 2 -> 3 -> null`

The dummy node is not included in the returned list; `dummy.next` is the actual answer.

## Time Complexity

**Time Complexity: O(n)**

Each original node is checked at most once. Checking a value and changing a pointer both take constant time, so the total time is linear in the number of nodes `n`.

## Space Complexity

**Space Complexity: O(1)**

Only a fixed number of references and one dummy node are used, regardless of list length.

## Challenges and Testing

Without a dummy node, removing the head requires separate special-case logic. The dummy node avoids that complication.

Useful tests:
- Empty list: `[]`, `val = 1` -> `[]`
- Target appears nowhere: `[1,2,3]`, `val = 4` -> `[1,2,3]`
- Target at the head: `[7,1,2]`, `val = 7` -> `[1,2]`
- Several targets in a row: `[2,2,2]`, `val = 2` -> `[]`
- Target appears at the end: `[1,2,3,3]`, `val = 3` -> `[1,2]`

## Reflection / Improvement

This solution already achieves **O(n) time and O(1) extra space**, which is optimal for a general linked list because every node may need to be inspected. The dummy node simplifies the implementation rather than reducing the asymptotic complexity.

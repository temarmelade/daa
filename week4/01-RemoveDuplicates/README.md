# 1. Remove Duplicates from Sorted List

## Problem

Given the head of a sorted linked list, remove repeated values so that each value appears only once. Return the head of the resulting list.

## Approach

I use a pointer called `current` to examine the list. Because the list is sorted, equal values are next to each other.

- If `current.val == current.next.val`, I skip the next node by assigning `current.next = current.next.next`.
- Otherwise, I move `current` to `current.next`.
- The loop stops when `current` is `null` or there is no next node.

I return `head` because the first node remains the start of the list.

## Written Trace

Input: `1 -> 1 -> 2 -> 3 -> 3 -> null`

| Iteration | Current value | Next value | Action | List after action |
|---|---:|---:|---|---|
| 1 | 1 | 1 | Skip the second `1` | `1 -> 2 -> 3 -> 3` |
| 2 | 1 | 2 | Move to the next node | `1 -> 2 -> 3 -> 3` |
| 3 | 2 | 3 | Move to the next node | `1 -> 2 -> 3 -> 3` |
| 4 | 3 | 3 | Skip the second `3` | `1 -> 2 -> 3` |
| 5 | 3 | null | Stop | `1 -> 2 -> 3` |

Output: `1 -> 2 -> 3 -> null`

The pointer does not move when a duplicate is removed. This is important because there may be more than two copies of the same value.

## Time Complexity

**Time Complexity: O(n)**

In the worst case, `current` visits each node once. Each comparison and pointer update takes constant time, so the total work grows linearly with the number of nodes `n`.

## Space Complexity

**Space Complexity: O(1)**

The algorithm uses only the `current` pointer and does not create another list or array.

## Challenges and Testing

A possible mistake is moving `current` immediately after removing a duplicate. That can skip checking the new neighbor when three or more equal values occur in a row. I avoid this by staying at the same node after skipping a duplicate.

Useful tests:
- Empty list: `[]` -> `[]`
- One node: `[5]` -> `[5]`
- All equal: `[2,2,2]` -> `[2]`
- No duplicates: `[1,2,3]` -> `[1,2,3]`
- Several groups: `[1,1,2,3,3]` -> `[1,2,3]`

## Reflection / Improvement

For a sorted list, this is already an efficient solution: **O(n) time and O(1) extra space**. A general unsorted list could use a set to track values, but that would require extra memory and is unnecessary here.

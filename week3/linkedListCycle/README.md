# Merge Two Sorted Lists

## 1. Problem

We are given two sorted linked lists. The goal is to combine them into one sorted linked list.

For example:

list1:
1 → 2 → 4

list2:
1 → 3 → 4

Result:

1 → 1 → 2 → 3 → 4 → 4

## 2. Approach

I use two pointers, one for each linked list.

I also create a dummy node that helps me build the resulting list.

While both lists still contain elements, I compare their current values.

- If the first value is smaller or equal, I add it to the result.
- Otherwise, I add the value from the second list.
- Then I move the corresponding pointer forward.

When one list becomes empty, I connect the remaining part of the other list to the result.

### Example trace

list1 = 1 → 2 → 4
list2 = 1 → 3 → 4

Step 1:
1 <= 1, so take the first 1.

Result:
1

Step 2:
2 > 1, so take the second 1.

Result:
1 → 1

Step 3:
2 <= 3, so take 2.

Result:
1 → 1 → 2

Step 4:
4 > 3, so take 3.

Result:
1 → 1 → 2 → 3

The remaining elements are 4 and 4, so they are added.

Final result:

1 → 1 → 2 → 3 → 4 → 4

## 3. Time Complexity

**Time Complexity: O(n + m)**

`n` is the number of nodes in the first list and `m` is the number of nodes in the second list.

Each node is processed at most once, so the total number of operations is proportional to `n + m`.

## Space Complexity

**Space Complexity: O(1)**

I don't create a new node for every element. I only use a few pointers and connect the existing nodes.

## 4. Reflection / Improvement

The solution is already optimal in time complexity because every element from both lists has to be examined at least once.

The time complexity cannot be better than O(n + m).

The solution could be written recursively, but that would use additional stack memory, so the iterative solution is more memory efficient.
# 112. Path Sum

Link: https://leetcode.com/problems/path-sum/

Language: Python 3

Run: `python solution.py`

## 1. Problem

We are given a binary tree and a number `targetSum`. We need to say if there is a path from the root to some **leaf** where the sum of all values on the path equals `targetSum`. Values can be negative.

## 2. Approach

Recursive DFS. Instead of collecting the sum while going down, I subtract the current node's value from the target. Then each child only has to answer a smaller question: "is there a path from me to a leaf with sum = remaining?".

1. If the node is `None`, return `False` (there is no path here).
2. `remaining = targetSum - node.val`.
3. If the node is a leaf, return `remaining == 0`.
4. Otherwise return `hasPathSum(left, remaining) or hasPathSum(right, remaining)`.

Because of `or`, Python stops as soon as the left side returns `True`, so we don't search the right side for nothing.

### Tracing

Example: `[5,4,8,11,null,13,4,7,2,null,null,null,1]`, `targetSum = 22`

```
          5
         / \
        4   8
       /   / \
      11  13  4
     /  \      \
    7    2      1
```

| Call | node | remaining after subtracting | leaf? | result |
|------|------|-----------------------------|-------|--------|
| 1 | 5 | 22 - 5 = 17 | no | go left |
| 2 | 4 | 17 - 4 = 13 | no | go left |
| 3 | 11 | 13 - 11 = 2 | no | go left |
| 4 | 7 | 2 - 7 = -5 | yes | False |
| 5 | 2 | 2 - 2 = 0 | yes | **True** |

Call 5 returns `True`, so call 3, 2 and 1 return `True` too. The right subtree (8, 13, 4, 1) is never visited. The path is 5 -> 4 -> 11 -> 2.

Example 2: `[1,2,3]`, `targetSum = 5`

```
    1
   / \
  2   3
```

- node 1: remaining 4
- node 2 (leaf): 4 - 2 = 2, not 0 -> False
- node 3 (leaf): 4 - 3 = 1, not 0 -> False
- Output: `False`

### Challenges (what did not work)

My first version had this base case:

```python
if root is None:
    return targetSum == 0
```

It looked logical ("if nothing is left to add and the target is 0, we found it"), but it is wrong in two cases:
- `root = []`, `targetSum = 0`: it returned `True`, but an empty tree has no paths at all, the expected answer is `False`.
- `root = [1, 2]`, `targetSum = 1`: node 1 has no right child, so the right `None` got `remaining = 0` and returned `True`. But node 1 is not a leaf, it has a left child, so the path 1 alone does not count. Expected `False`.

The fix was to check "is this a leaf" on the real node, not on `None`. `None` always returns `False`.

Another thing I thought about: I wanted to stop early when the remaining sum becomes negative. That doesn't work here because values can be negative, e.g. `[-2, null, -3]` with target `-5`: the remaining goes from -5 to -3 and then 0. If I had cut negative values I would miss it. I added this case to the tests.

## 3. Time Complexity

**Time Complexity: O(n)**

In the worst case (no valid path, or the valid path is the last one we check) we visit every node once, and each visit does O(1) work: one subtraction and a couple of checks. If a path is found early, the `or` short-circuit stops the search, so in practice it can be faster, but the worst case is still O(n).

## 4. Space Complexity

**Space Complexity: O(h)** for the recursion stack, h = height of the tree. O(log n) for a balanced tree, O(n) for a skewed one. I don't store any paths, only the remaining number is passed down.

## 5. Reflection / Improvement

- We cannot do better than O(n) in the worst case, because without looking at every node we can't be sure that no path exists (values are arbitrary, there is no ordering like in a BST).
- An iterative version with a stack of `(node, remaining)` pairs would have the same O(n) time and O(h) space, but it would avoid Python's recursion limit on very deep trees. That is the only change I would make.

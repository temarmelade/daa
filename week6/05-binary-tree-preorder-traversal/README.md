# 144. Binary Tree Preorder Traversal

Link: https://leetcode.com/problems/binary-tree-preorder-traversal/

Language: Python 3

Run: `python solution.py`

## 1. Problem

Return the values of a binary tree in preorder: first the node itself, then its whole left subtree, then its whole right subtree.

## 2. Approach

Since I already did inorder recursively, here I made the **iterative stack version** the main solution and kept a short recursive one for checking.

Iterative idea:
1. Push the root onto the stack.
2. Pop a node and add its value to the result (preorder = visit the node first, so we add it right away).
3. Push the **right** child first and then the **left** child.
4. Repeat until the stack is empty.

Why right first: the stack is LIFO, the last pushed element comes out first. I want the left subtree to be processed before the right one, so left has to be pushed last.

### Tracing

Example: `[1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]`

```
          1
        /   \
       2     3
      / \     \
     4   5     8
        / \   /
       6   7 9
```

| Step | pop | result | push (right, then left) | stack after (bottom -> top) |
|------|-----|--------|-------------------------|-----------------------------|
| 0 | - | [] | 1 | [1] |
| 1 | 1 | [1] | 3, 2 | [3, 2] |
| 2 | 2 | [1, 2] | 5, 4 | [3, 5, 4] |
| 3 | 4 | [1, 2, 4] | - | [3, 5] |
| 4 | 5 | [1, 2, 4, 5] | 7, 6 | [3, 7, 6] |
| 5 | 6 | [1, 2, 4, 5, 6] | - | [3, 7] |
| 6 | 7 | [1, 2, 4, 5, 6, 7] | - | [3] |
| 7 | 3 | [1, 2, 4, 5, 6, 7, 3] | 8 | [8] |
| 8 | 8 | [..., 3, 8] | 9 | [9] |
| 9 | 9 | [1, 2, 4, 5, 6, 7, 3, 8, 9] | - | [] |

Output: `[1, 2, 4, 5, 6, 7, 3, 8, 9]`

Small example `[1, null, 2, 3]` gives `[1, 2, 3]`.

### Challenges

- The first time I pushed left first and then right (because it "felt" natural). The output for `[1,2,3]` was `[1, 3, 2]`, which is wrong, right subtree came before left. Then I remembered that stack reverses the order, so I swapped the pushes.
- I also first pushed children without checking for `None` and then did `if node is None: continue` after popping. That also works, but it pushes and pops a lot of useless `None` values (n + 1 of them), so I check before pushing instead.
- The recursive version I wrote as `[root.val] + left + right`. It is short and good for testing, but list concatenation copies the lists on every level, so it is O(n·h), up to O(n^2) for a skewed tree. That's another reason the iterative version is the main one.

## 3. Time Complexity

**Time Complexity: O(n)**

Each node is pushed onto the stack exactly once and popped exactly once. Every push/pop/append is O(1). So the total work is proportional to the number of nodes.

## 4. Space Complexity

**Space Complexity: O(h)** extra (not counting the output).

When we pop a node we push at most its two children, and we always go left first, so the stack holds the current path plus the right siblings that are waiting along that path. That's at most about one node per level, plus one, so O(h). Balanced tree: O(log n), skewed tree: O(n).

## 5. Reflection / Improvement

- Time O(n) is optimal, we must output n values.
- Space can be O(1) with **Morris preorder traversal**: use temporary links from the rightmost node of the left subtree back to the current node instead of a stack. It's the same trick as for inorder, the only difference is that we add the value when we create the link, not when we remove it. Result: **O(n) time, O(1) extra space**, but the tree is temporarily changed and the code is harder to debug.

# 104. Maximum Depth of Binary Tree

Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Language: Python 3

Run: `python solution.py`

## 1. Problem

Given a binary tree, find how many nodes are on the longest path from the root down to the deepest leaf. An empty tree has depth 0, a tree with only a root has depth 1.

## 2. Approach

The main solution is recursive DFS. The key observation: the depth of a tree is 1 (for the root itself) plus the bigger of the depths of its two subtrees.

```
maxDepth(None) = 0
maxDepth(node) = 1 + max(maxDepth(node.left), maxDepth(node.right))
```

So each node asks its children "how deep are you?", takes the bigger answer and adds one. The answers go back up from the leaves to the root.

I also wrote a BFS version (`maxDepthBfs`) that goes level by level and counts how many levels there are. I used it in the tests to double check the recursive one.

### Tracing

Example: `[3, 9, 20, null, null, 15, 7]`

```
      3
     / \
    9   20
       /  \
      15   7
```

Recursive calls (results come back from the bottom):

```
maxDepth(3)
  maxDepth(9)
    maxDepth(None) = 0
    maxDepth(None) = 0
    -> 1 + max(0, 0) = 1
  maxDepth(20)
    maxDepth(15) -> 1 + max(0, 0) = 1
    maxDepth(7)  -> 1 + max(0, 0) = 1
    -> 1 + max(1, 1) = 2
  -> 1 + max(1, 2) = 3
```

Output: `3`

BFS trace on the same tree:

| Level | queue at start of level | depth after level |
|-------|-------------------------|-------------------|
| 1 | [3] | 1 |
| 2 | [9, 20] | 2 |
| 3 | [15, 7] | 3 |
| - | [] -> stop | answer = 3 |

### Challenges

- At first I wanted to keep a global variable `best` and update it every time I reach a leaf with the current depth. It works, but it is more code and you need to pass the current depth down. Returning the value from the recursion is cleaner, so I changed it.
- In the BFS version I first forgot the inner `for _ in range(len(queue))` loop and incremented `depth` for every popped node. That gives the number of nodes, not the number of levels (for the example it returned 5 instead of 3). The inner loop makes sure we process one whole level before increasing the depth.
- I tested a skewed tree `[1,2,null,3,null,4,null,5]` (depth 5) to make sure that one-sided trees work, and the empty tree `[]` which must return 0.

## 3. Time Complexity

**Time Complexity: O(n)**

Each node is visited exactly once and at each node we only do a `max` of two numbers and an addition, which is O(1). So the total is O(n). We cannot skip any node, because any node could be the deepest one.

## 4. Space Complexity

**Space Complexity: O(h)** for the recursive version, where h is the height.

The recursion goes as deep as the tree is tall. Balanced tree: O(log n). Skewed tree: O(n). For BFS the space is O(w), where w is the maximum width of the tree (the largest level). For a full binary tree the last level has about n/2 nodes, so BFS can also use O(n).

## 5. Reflection / Improvement

- O(n) time is already optimal, every node has to be checked.
- There is no better asymptotic space solution without modifying the tree. What can be improved is practical: in Python the recursion limit is 1000 by default, so a very deep skewed tree could crash with `RecursionError`. To avoid this, I would use the BFS version or an iterative DFS with an explicit stack of `(node, depth)` pairs. Complexity stays O(n) time and O(h) or O(w) space, but no recursion limit problem.

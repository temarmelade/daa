# Week 6 — Binary Trees

All solutions are written in Python 3. Each folder has `solution.py` (the code + tests) and `README.md` (the report).

To run all tests from this folder:

```bash
for d in */; do python3 "$d/solution.py"; done
```

| # | Problem | Main approach | Time | Space |
|---|---------|---------------|------|-------|
| 01 | [Binary Tree Inorder Traversal](01-binary-tree-inorder-traversal) | Recursive DFS (+ iterative stack) | O(n) | O(h) |
| 02 | [Maximum Depth of Binary Tree](02-maximum-depth-of-binary-tree) | Recursive DFS (+ BFS) | O(n) | O(h) |
| 03 | [Minimum Depth of Binary Tree](03-minimum-depth-of-binary-tree) | BFS with early stop | O(n) | O(w) |
| 04 | [Path Sum](04-path-sum) | DFS, subtract from target | O(n) | O(h) |
| 05 | [Binary Tree Preorder Traversal](05-binary-tree-preorder-traversal) | Iterative stack | O(n) | O(h) |
| 06 | [Binary Tree Postorder Traversal](06-binary-tree-postorder-traversal) | Reversed modified preorder | O(n) | O(n) |
| 07 | [Invert Binary Tree](07-invert-binary-tree) | Recursive swap | O(n) | O(h) |
| 08 | [Binary Tree Paths](08-binary-tree-paths) | DFS + backtracking | O(n · h) | O(h) |
| 09 | [Sum of Left Leaves](09-sum-of-left-leaves) | DFS with `is_left` flag | O(n) | O(h) |
| 10 | [Merge Two Binary Trees](10-merge-two-binary-trees) | Recursive, reuse tree 1 | O(min(n1, n2)) | O(min(h1, h2)) |

n = number of nodes, h = height of the tree, w = maximum width of the tree.

## General notes

- Most problems this week are the same pattern: solve the problem for the left and right subtrees, then combine the answers at the current node. The hard part was usually not the recursion itself, but the base cases (empty tree, node with only one child, what counts as a leaf).
- Recursion in Python has a default limit of 1000 calls, so for very deep (skewed) trees an iterative version with an explicit stack or queue is safer. I mention this in the reflection of several tasks.
- Each `solution.py` includes a small `build_tree` helper that builds a tree from LeetCode's array format, so I could test with the same examples as on the website.

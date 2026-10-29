# 404. Sum of Left Leaves

Link: https://leetcode.com/problems/sum-of-left-leaves/

Language: Python 3

Run: `python solution.py`

## 1. Problem

Sum the values of all leaves that are a **left child** of their parent. A leaf is a node without children. The root alone is not counted, because it isn't anybody's left child.

## 2. Approach

Recursive DFS where every call also knows **how it got to this node**: as a left child or as a right child. I pass a boolean `is_left`.

1. If the node is `None`, return 0.
2. If the node is a leaf: return its value if `is_left` is `True`, else return 0.
3. Otherwise return `dfs(left, True) + dfs(right, False)`.

The root is called with `is_left = False`, so a tree with only one node returns 0.

### Tracing

Example: `[3, 9, 20, null, null, 15, 7]`

```
      3
     / \
    9   20
       /  \
      15   7
```

| Call | node | is_left | leaf? | returns |
|------|------|---------|-------|---------|
| dfs(3, False) | 3 | False | no | dfs(9) + dfs(20) |
| dfs(9, True) | 9 | True | yes | **9** |
| dfs(20, False) | 20 | False | no | dfs(15) + dfs(7) |
| dfs(15, True) | 15 | True | yes | **15** |
| dfs(7, False) | 7 | False | yes | 0 |

`dfs(20) = 15 + 0 = 15`, `dfs(3) = 9 + 15 = 24`

Output: `24`

Another case I traced: `[1, 2, null, 3, 4]`

```
      1
     /
    2
   / \
  3   4
```

Node 2 is a left child, but it is **not** a leaf, so it isn't counted. Node 3 is a left leaf (counted), node 4 is a right leaf (not counted). Answer = 3.

### Challenges (what did not work)

- My first idea was to only check the left child of each node: `if node.left: total += node.left.val`. That gave 9 + 15 + ... but it also added node values that are left children but **not leaves**. For `[1, 2, null, 3, 4]` it returned 2 + 3 = 5 instead of 3. I needed to also check that the left child has no children of its own.
- Then I wrote the version without the flag, where the parent checks: "if my left child exists and is a leaf, add its value, else recurse into it". It works, but the checks were messier (`node.left and not node.left.left and not node.left.right`). Passing `is_left` down made the code simpler, because each node decides only about itself.
- Edge case: `[1]` must return 0, not 1. The root is a leaf, but not a left one. Starting with `is_left = False` handles this.

## 3. Time Complexity

**Time Complexity: O(n)**

Every node is visited once (plus calls for `None` children, which is n + 1 more calls, still O(n)). Each call does a constant amount of work: a couple of `if` checks and one addition. We need to visit all nodes because a left leaf could be anywhere in the tree.

## 4. Space Complexity

**Space Complexity: O(h)** for the recursion stack, h = height of the tree. That's O(log n) for a balanced tree and O(n) for a skewed one. No other data structures are used.

## 5. Reflection / Improvement

- O(n) time is optimal, any node could be a left leaf, so all of them must be checked.
- The same logic can be done with BFS: put `(node, is_left)` into a queue. Same **O(n)** time, O(w) space (w = width of the tree), and no recursion limit for very deep trees.
- Morris traversal could reduce space to O(1), but for this problem it would make the code a lot harder to read for very little benefit.

# 617. Merge Two Binary Trees

Link: https://leetcode.com/problems/merge-two-binary-trees/

Language: Python 3

Run: `python solution.py`

## 1. Problem

We have two binary trees. We put one on top of the other: where both trees have a node in the same position, the new node's value is the sum of both. Where only one tree has a node, we just take that node (with its whole subtree). We return the root of the merged tree.

## 2. Approach

Recursive, going through both trees at the same time, position by position.

1. If `root1` is `None`, return `root2` (whatever is in tree 2 at this position, even if it's `None` too).
2. If `root2` is `None`, return `root1`.
3. Both exist: add `root2.val` to `root1.val`.
4. Merge the left children and attach the result as `root1.left`. Same for the right.
5. Return `root1`.

So I reuse the nodes of the first tree instead of creating a new tree. The important part is step 1 and 2: when one side is missing, I don't go deeper at all, I just attach the existing subtree as it is.

### Tracing

Example: `root1 = [1, 3, 2, 5]`, `root2 = [2, 1, 3, null, 4, null, 7]`

```
Tree 1:        Tree 2:          Merged:
     1              2                 3
    / \            / \               / \
   3   2          1   3             4   5
  /                \   \           / \   \
 5                  4   7         5   4   7
```

| Call | root1 | root2 | action | result |
|------|-------|-------|--------|--------|
| merge(1, 2) | 1 | 2 | both exist, 1 + 2 = 3 | node 3, recurse |
| merge(3, 1) | 3 | 1 | both exist, 3 + 1 = 4 | node 4, recurse |
| merge(5, None) | 5 | None | root2 missing | return 5 as is |
| merge(None, 4) | None | 4 | root1 missing | return 4 as is |
| merge(2, 3) | 2 | 3 | both exist, 2 + 3 = 5 | node 5, recurse |
| merge(None, None) | None | None | root1 missing | return None |
| merge(None, 7) | None | 7 | root1 missing | return 7 as is |

Output (level order): `[3, 4, 5, 5, 4, null, 7]`

Notice that the calls only went into 3 pairs where both nodes existed. The nodes 5, 4 and 7 were attached directly, the recursion didn't go into their subtrees.

### Challenges (what did not work)

- At first I wrote it to always create a new node and handle `None` by using 0 as its value:
  ```python
  v1 = root1.val if root1 else 0
  v2 = root2.val if root2 else 0
  node = TreeNode(v1 + v2)
  node.left = merge(root1.left if root1 else None, root2.left if root2 else None)
  ```
  It worked, but it was full of `if ... else None` and it walked through **every** node of both trees, even the parts where one tree was empty. It also copies the subtrees instead of reusing them. The current version stops as soon as one side is missing.
- I was worried about the edge cases where one or both trees are empty. Tests `[] + [1, 2]`, `[1, 2] + []` and `[] + []` all work, because the first two `if`s return the other tree directly.
- One thing to be aware of: my solution **modifies tree 1** and the result shares nodes with tree 2. For LeetCode this is allowed. If the original trees had to stay unchanged, I would need to create new nodes and copy the remaining subtrees (that would cost O(n1 + n2) time).

## 3. Time Complexity

**Time Complexity: O(min(n1, n2))**, where n1 and n2 are the number of nodes in the two trees.

Recursion only continues where **both** trees have a node. When one side is `None`, the call returns in O(1) and the other subtree is attached without visiting it. So the number of "real" calls equals the number of overlapping positions, which is at most min(n1, n2). Each call does O(1) work (one addition, two assignments). The calls with a `None` side are at most twice the number of overlapping nodes (each overlapping node has 2 children), so it's still O(min(n1, n2)).

## 4. Space Complexity

**Space Complexity: O(min(h1, h2))** for the recursion stack.

The recursion only goes down while both trees have nodes, so its depth is bounded by the height of the overlapping part, which is at most the smaller height. No new nodes are created, the result reuses existing nodes.

## 5. Reflection / Improvement

- This is already better than the "obvious" O(n1 + n2) solution, because overlapping is the only part where real work is needed. I don't think it can be asymptotically better, because every overlapping position needs its values added.
- An iterative version with a stack of pairs `(node1, node2)` would have the same **O(min(n1, n2))** time and avoid Python's recursion limit for very deep trees.
- If the problem required not to modify the input, the complexity would become O(n1 + n2), because we'd have to copy every node into the new tree.

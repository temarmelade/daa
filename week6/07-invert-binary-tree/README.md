# 226. Invert Binary Tree

Link: https://leetcode.com/problems/invert-binary-tree/

Language: Python 3

Run: `python solution.py`

## 1. Problem

Mirror a binary tree: for every node, its left and right children switch places. The result looks like the original tree in a mirror. We return the root of the changed tree.

## 2. Approach

Recursive. To invert a tree:
1. If the node is `None`, return `None`.
2. Invert the right subtree, this becomes the new left.
3. Invert the left subtree, this becomes the new right.
4. Attach them and return the node.

So every node swaps its two children, and the recursion makes sure the swap also happens inside the children. I change the tree in place, no new nodes are created.

### Tracing

Example: `[4, 2, 7, 1, 3, 6, 9]`

```
Before:            After:
      4                 4
    /   \             /   \
   2     7           7     2
  / \   / \         / \   / \
 1   3 6   9       9   6 3   1
```

Order of calls (the swap at a node happens after both of its children are already inverted):

```
invert(4)
  invert(7)                 (right of 4, will become left)
    invert(9) -> leaf, children None, returns 9
    invert(6) -> leaf, returns 6
    7.left = 9, 7.right = 6
  invert(2)                 (left of 4, will become right)
    invert(3) -> returns 3
    invert(1) -> returns 1
    2.left = 3, 2.right = 1
  4.left = 7, 4.right = 2
```

Output (level order): `[4, 7, 2, 9, 6, 3, 1]`

Example 2: `[1, 2]`, so 1 has only a left child 2. After inverting, 2 is the right child: `[1, null, 2]`.

### Challenges (what did not work)

My first version looked like this:

```python
root.left = self.invertTree(root.right)
root.right = self.invertTree(root.left)
```

The output for `[2, 1, 3]` was `[2, 3, 3]`, which is obviously wrong. The bug: after the first line `root.left` is already overwritten with the inverted right subtree, so on the second line I invert the **new** left (which was the old right) instead of the old left. Node 1 was lost completely.

The fix is to compute both results first, and only then assign them. In my solution I store them in `new_left` and `new_right` first. (Python's tuple assignment `root.left, root.right = invert(root.right), invert(root.left)` also works, because the right side is fully evaluated before anything is assigned.)

To check the output I wrote a `tree_to_list` helper that converts the tree back into LeetCode's level-order format, so I can compare with the expected arrays.

## 3. Time Complexity

**Time Complexity: O(n)**

Every node is visited exactly once, and at each node we only do two assignments (the swap), which is O(1). So it's O(n) total. Every node has to be touched, because every node's children must be swapped.

## 4. Space Complexity

**Space Complexity: O(h)**

No new nodes are created, the tree is changed in place. The only extra memory is the recursion stack, whose depth is the height h of the tree: O(log n) if balanced, O(n) if skewed.

## 5. Reflection / Improvement

- O(n) time is optimal, we must swap the children of every node.
- The order of visiting doesn't matter for this problem, I could also use BFS with a queue: pop a node, swap its children, push them. Time stays **O(n)**, space becomes O(w) (width of the tree) instead of O(h). That version avoids the Python recursion limit for very deep trees, which is the only real improvement here.

# 257. Binary Tree Paths

Link: https://leetcode.com/problems/binary-tree-paths/

Language: Python 3

Run: `python solution.py`

## 1. Problem

Return all paths from the root to every leaf, as strings in the format `"1->2->5"`. The order of the paths in the answer doesn't matter on LeetCode.

## 2. Approach

DFS with **backtracking**. I keep one list `path` with the values on the way from the root to the current node.

1. When entering a node, append its value (as a string) to `path`.
2. If the node is a leaf, join `path` with `"->"` and save the string to the result.
3. Otherwise go into the left child, then into the right child.
4. When leaving the node, remove its value from `path` (`path.pop()`), so the list is correct again for the parent's other branch.

This way I reuse one list for the whole traversal and only build a string when I actually reach a leaf.

### Tracing

Example: `[1, 2, 3, null, 5]`

```
     1
    / \
   2   3
    \
     5
```

| Step | action | path | result |
|------|--------|------|--------|
| 1 | enter 1 | [1] | [] |
| 2 | enter 2 | [1, 2] | [] |
| 3 | left of 2 is None, return | [1, 2] | [] |
| 4 | enter 5 (leaf) -> save | [1, 2, 5] | ["1->2->5"] |
| 5 | leave 5 | [1, 2] | ["1->2->5"] |
| 6 | leave 2 | [1] | ["1->2->5"] |
| 7 | enter 3 (leaf) -> save | [1, 3] | ["1->2->5", "1->3"] |
| 8 | leave 3 | [1] | ... |
| 9 | leave 1 | [] | ["1->2->5", "1->3"] |

Output: `["1->2->5", "1->3"]`

### Challenges (what did not work)

- My first version didn't have `path.pop()`. For the example above it returned `["1->2->5", "1->2->5->3"]`: the values from the left branch stayed in the list when I went into the right branch. That is when I understood that with one shared list I have to "undo" the change on the way back (that is what backtracking means).
- My second version passed the path as a string: `dfs(child, path + "->" + str(node.val))`. It works and doesn't need `pop()` because every call gets its own new string. But each `+` copies the whole string, so every node costs O(length of path). I kept the list version because it only builds a string once per leaf.
- I almost forgot negative numbers, but `str(-1)` gives `"-1"`, so `[-1, null, 20]` correctly becomes `"-1->20"`.
- A single node tree `[1]` must give `["1"]` without any arrow, `"->".join(["1"])` handles this automatically.

## 3. Time Complexity

**Time Complexity: O(n · h)** in general, where h is the height. In the worst case this is O(n^2).

Why: the traversal itself is O(n), every node is entered and left once, and `append`/`pop` are O(1). The extra cost is building the strings: for every leaf, `join` costs O(length of the path) = O(h). There are at most O(n) leaves, so O(n · h) for building strings.

- Balanced tree: about n/2 leaves, each path is log n long -> O(n log n).
- Worst case: a long "spine" of n/2 nodes with a leaf hanging off each spine node. Then there are about n/2 leaves with paths of length up to n/2 -> O(n^2).
- Skewed tree (like a linked list): only 1 leaf -> O(n).

The output itself has this size, so we can't avoid it.

## 4. Space Complexity

**Space Complexity: O(h)** extra for the recursion stack and the `path` list (both hold at most one root-to-leaf path). The output is not counted, but it can be O(n · h) characters as explained above.

## 5. Reflection / Improvement

- Since the answer itself can contain O(n · h) characters, no algorithm can be asymptotically faster than that, so my solution is optimal in terms of output size.
- Compared to the string-concatenation version, mine is better: that one builds a new string at **every** node (not only at leaves), which costs more in practice (O(n · h) for all nodes instead of only for leaves).
- An iterative DFS with a stack of `(node, path_string)` would avoid the recursion limit, but it has to store a separate string for every node in the stack, so it uses more memory. I would only use it if the tree was very deep.

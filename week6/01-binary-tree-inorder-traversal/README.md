# 94. Binary Tree Inorder Traversal

Link: https://leetcode.com/problems/binary-tree-inorder-traversal/

Language: Python 3

Run: `python solution.py`

## 1. Problem

We get the root of a binary tree and need to return the values of all nodes in "inorder" order. Inorder means: first everything in the left subtree, then the node itself, then everything in the right subtree. This rule is applied at every node, not only at the root.

## 2. Approach

I wrote two versions. The main one is recursive, because it follows the definition directly. The second one is iterative with a stack (the problem has a follow-up asking for it, so I wanted to try).

### Recursive version (`inorderTraversal`)

I have a helper `visit(node, result)`:
1. If the node is `None`, just return (base case).
2. Call `visit` on the left child.
3. Append the current value to `result`.
4. Call `visit` on the right child.

I pass the same list `result` into every call, so all calls write into one list and I don't create new lists all the time.

### Iterative version (`inorderIterative`)

The idea is to simulate what recursion does with the call stack:
1. Go left as far as possible, pushing every node onto the stack.
2. When there is no left child anymore, pop a node, this is the next node in inorder, so add it.
3. Move to its right child and repeat from step 1.

### Tracing

Example: `root = [1, null, 2, 3]`

```
    1
     \
      2
     /
    3
```

Recursive trace (indentation = recursion depth):

```
visit(1)
  visit(None)          -> return
  append 1             result = [1]
  visit(2)
    visit(3)
      visit(None)      -> return
      append 3         result = [1, 3]
      visit(None)      -> return
    append 2           result = [1, 3, 2]
    visit(None)        -> return
```

Output: `[1, 3, 2]`

Iterative trace on the same tree:

| Step | current | stack (bottom -> top) | action | result |
|------|---------|-----------------------|--------|--------|
| 1 | 1 | [1] | push 1, go left (None) | [] |
| 2 | None | [] | pop 1, add, go right to 2 | [1] |
| 3 | 2 | [2] | push 2, go left to 3 | [1] |
| 4 | 3 | [2, 3] | push 3, go left (None) | [1] |
| 5 | None | [2] | pop 3, add, go right (None) | [1, 3] |
| 6 | None | [] | pop 2, add, go right (None) | [1, 3, 2] |
| 7 | None | [] | loop ends | [1, 3, 2] |

Second example from LeetCode: `[1,2,3,4,5,null,8,null,null,6,7,9]` gives `[4,2,6,5,7,1,3,9,8]`, both versions return the same thing (checked in the tests).

### Challenges

- My first recursive version returned lists and concatenated them: `return left + [root.val] + right`. It works, but every `+` creates a new list and copies elements. For a skewed tree it becomes O(n^2) because the lists get copied again on every level. So I switched to one shared `result` list.
- In the iterative version I first wrote `while stack:` as the loop condition. It failed immediately because at the start the stack is empty and the loop didn't run at all, so I got `[]` for every tree. The condition must be `while current or stack`, because there are moments when the stack is empty but we still have a node to process (the root at the start, or a right child).
- I also tested the empty tree `[]` and a single node `[1]`, both are fine.

## 3. Time Complexity

**Time Complexity: O(n)**, where n is the number of nodes.

Every node is visited exactly once. In the recursive version `visit` is called once for each node plus once for each `None` child. A binary tree with n nodes has n + 1 `None` children, so the total is about 2n + 1 calls, each doing O(1) work. In the iterative version every node is pushed once and popped once, which is also O(n).

## 4. Space Complexity

**Space Complexity: O(h)** extra, where h is the height of the tree (not counting the output list, which is O(n) anyway).

The recursion stack (or my explicit stack) holds at most one path from the root down, so its size is at most h. For a balanced tree h = log n, but in the worst case (tree like a linked list) h = n, so the worst case is O(n).

## 5. Reflection / Improvement

- Time cannot be better than O(n), because we have to output all n values.
- Space can be improved with **Morris traversal**. It temporarily links the rightmost node of the left subtree back to the current node (a "thread"), so we can come back up without a stack, and then removes the link. This gives **O(n) time and O(1) extra space**.
- What I would need to change: remove the stack and instead, for every node with a left child, find its inorder predecessor and create/remove the temporary pointer. The downside is that it modifies the tree during the traversal (it restores it at the end), and the code is harder to read, so I kept the stack version.

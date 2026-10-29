# 145. Binary Tree Postorder Traversal

Link: https://leetcode.com/problems/binary-tree-postorder-traversal/

Language: Python 3

Run: `python solution.py`

## 1. Problem

Return the node values in postorder: left subtree first, then right subtree, and the node itself at the very end. So the root is always the last element of the answer.

## 2. Approach

Postorder recursively is easy (left, right, then append), so I wrote it as `postorderRecursive` for checking. For the main solution I wanted an iterative one, but iterative postorder is harder than preorder because a node must be added only **after** both of its subtrees are done.

The trick I used: postorder is `left -> right -> node`. If I reverse that, I get `node -> right -> left`. That is just preorder with left and right swapped, which is easy to do with a stack (I already did preorder in task 5). So:

1. Do a "modified preorder": pop a node, add it, push **left** first and then **right** (so right is processed first).
2. This gives the order `node, right, left`.
3. Reverse the result list at the end to get `left, right, node`.

### Tracing

Example: `[1, null, 2, 3]`

```
    1
     \
      2
     /
    3
```

| Step | pop | result (node-right-left) | push (left, then right) | stack after |
|------|-----|--------------------------|-------------------------|-------------|
| 0 | - | [] | 1 | [1] |
| 1 | 1 | [1] | -, 2 | [2] |
| 2 | 2 | [1, 2] | 3, - | [3] |
| 3 | 3 | [1, 2, 3] | - | [] |

Reverse `[1, 2, 3]` -> `[3, 2, 1]`. Correct.

Bigger example: `[1,2,3,4,5,null,8,null,null,6,7,9]`

```
          1
        /   \
       2     3
      / \     \
     4   5     8
        / \   /
       6   7 9
```

| Step | pop | result before reverse | stack after (bottom -> top) |
|------|-----|-----------------------|-----------------------------|
| 1 | 1 | [1] | [2, 3] |
| 2 | 3 | [1, 3] | [2, 8] |
| 3 | 8 | [1, 3, 8] | [2, 9] |
| 4 | 9 | [1, 3, 8, 9] | [2] |
| 5 | 2 | [1, 3, 8, 9, 2] | [4, 5] |
| 6 | 5 | [1, 3, 8, 9, 2, 5] | [4, 6, 7] |
| 7 | 7 | [..., 5, 7] | [4, 6] |
| 8 | 6 | [..., 7, 6] | [4] |
| 9 | 4 | [1, 3, 8, 9, 2, 5, 7, 6, 4] | [] |

After reverse: `[4, 6, 7, 5, 2, 9, 8, 3, 1]`, which matches the expected output.

### Challenges (what did not work)

- My first iterative attempt was: pop a node, if it has children push the node back and then push its children, otherwise add it. The problem: when the node came back to the top of the stack, it still had children, so it pushed them again and again, and the program got stuck in an infinite loop. To fix it I would need to remember which nodes were already "expanded" (a visited set or a `prev` pointer). That is possible, but I found the reverse trick simpler and less error-prone.
- I also wondered if the reverse trick is "cheating" because it's not a real postorder walk: the nodes are not visited in postorder, only the final list is. For this problem only the output matters, so it is fine. But if I needed to process each node in real postorder (for example free memory of children before parent), this trick would not work, and I would need the version with a `prev` pointer.

## 3. Time Complexity

**Time Complexity: O(n)**

Each node is pushed once and popped once, O(1) each, so O(n) for the traversal. Reversing the list is also O(n). Total O(n) + O(n) = O(n).

## 4. Space Complexity

**Space Complexity: O(n)**

The output list is O(n) anyway. The stack can hold up to O(n) nodes in bad cases (for this modified preorder it is O(h) plus waiting siblings, so O(n) in the worst case like a skewed tree). The recursive version uses O(h) for the call stack.

## 5. Reflection / Improvement

- Time O(n) is already the best possible.
- If I didn't want to build the full list and then reverse it (for example, if I needed to process nodes one by one in true postorder), I'd use the one-stack method with a `prev` pointer: go left as far as possible, then look at the top of the stack; if it has a right child that was not visited yet, go there, otherwise pop and process it. It's still **O(n) time, O(h) space**.
- Morris traversal can also do postorder in O(1) extra space, but it's quite complicated (it needs to reverse parts of the right edges), so I didn't implement it.

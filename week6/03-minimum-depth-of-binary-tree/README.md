# 111. Minimum Depth of Binary Tree

Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/

Language: Python 3

Run: `python solution.py`

## 1. Problem

We need the number of nodes on the shortest path from the root to a **leaf**. A leaf is a node that has no children at all. This "leaf" part is the tricky thing in this problem, a node with only one child is not the end of a path.

## 2. Approach

My final solution uses **BFS** (level order traversal). BFS visits nodes level by level, so the first leaf that I take out of the queue is guaranteed to be the closest one to the root. At that moment I can return its depth and stop, I don't need to look at the rest of the tree.

Steps:
1. If the tree is empty, return 0.
2. Put `(root, 1)` into a queue.
3. Pop a `(node, depth)`. If the node has no children, it's a leaf, return `depth`.
4. Otherwise push its existing children with `depth + 1` and continue.

### Tracing

Example 1: `[3, 9, 20, null, null, 15, 7]`

```
      3
     / \
    9   20
       /  \
      15   7
```

| Step | popped | leaf? | queue after |
|------|--------|-------|-------------|
| 1 | (3, 1) | no | [(9, 2), (20, 2)] |
| 2 | (9, 2) | **yes** | return 2 |

Output: `2`. Nodes 15 and 7 are never even visited.

Example 2: `[2, null, 3, null, 4, null, 5, null, 6]`

```
2
 \
  3
   \
    4
     \
      5
       \
        6
```

| Step | popped | leaf? | queue after |
|------|--------|-------|-------------|
| 1 | (2, 1) | no | [(3, 2)] |
| 2 | (3, 2) | no | [(4, 3)] |
| 3 | (4, 3) | no | [(5, 4)] |
| 4 | (5, 4) | no | [(6, 5)] |
| 5 | (6, 5) | **yes** | return 5 |

Output: `5`

### Challenges (what did not work)

My first idea was to just copy the solution from Maximum Depth and change `max` to `min`:

```python
return 1 + min(minDepth(root.left), minDepth(root.right))
```

I left it in the file as `minDepthWrong`. It passed example 1, but on example 2 it returns **1** instead of 5. The reason: at node 2 the left child is `None`, so `minDepth(None) = 0`, and `min(0, something) = 0`, so the answer becomes `1 + 0 = 1`. It treats the missing child as if it was a path of length 0, but a missing child is not a leaf. The path has to end at a real leaf.

Then I fixed the recursion (`minDepthDfs`): if one child is missing, only go into the other child; only use `min` when both children exist. That version is correct, but it always visits the whole tree. That's why I switched to BFS as the main solution: it can stop early at the first leaf.

I also tested `[1, 2]` (root with one child) which should be 2, not 1. Both correct versions return 2.

## 3. Time Complexity

**Time Complexity: O(n)** in the worst case.

In the worst case (for example the skewed tree from example 2, or when the closest leaf is on the last level) BFS has to visit all n nodes, each one is pushed and popped once, O(1) per node. In good cases it is much faster: it only visits the nodes on levels up to the first leaf. For example 1 it visited 2 nodes out of 5.

The fixed DFS version is always Θ(n), because it has to explore every branch before it knows which one is the shortest.

## 4. Space Complexity

**Space Complexity: O(w)**, where w is the maximum number of nodes on one level (the queue holds at most about one level plus part of the next). For a complete tree this can be about n/2, so O(n) worst case. The DFS version uses O(h) for the recursion stack.

Another reason I liked BFS here: LeetCode allows up to 10^5 nodes, and a skewed tree of that size would hit Python's default recursion limit (1000) with the recursive version. BFS has no recursion.

## 5. Reflection / Improvement

- In the worst case O(n) time is unavoidable, because the only leaf could be at the very bottom and we have to reach it.
- BFS is already the "improved" version compared to my DFS because of early stopping.
- A possible small trade-off: if the tree is very wide but the leaves are deep, BFS uses more memory than DFS. In that case DFS with pruning (stop going deeper than the best depth found so far) would use only O(h) space, but its time is still O(n) in the worst case.

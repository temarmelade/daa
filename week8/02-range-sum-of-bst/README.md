# 938. Range Sum of BST

Link: https://leetcode.com/problems/range-sum-of-bst/

Language: Python 3

Run: python solution.py

## 1. Problem

We have a binary search tree and two numbers, low and high. We need to add up all values in the tree that are between low and high (including low and high).

## 2. Approach

Simple way: visit every node, and if its value is between low and high, add it. This works.

But the tree is a BST, so I can skip parts of it:
- If the node value is smaller than low, then everything on its left is even smaller. So I skip the left side and only go right.
- If the node value is bigger than high, then everything on its right is even bigger. So I skip the right side and only go left.
- Otherwise the node is inside the range. I add it and check both sides.
- Empty node gives 0.

Tracing, tree [10, 5, 15, 3, 7, null, 18], low = 7, high = 15:

      10
     /  \
    5    15
   / \     \
  3   7     18

node 10: inside range, add 10, check both sides.
node 5: 5 < 7, skip left (3 is not needed), go right.
node 7: inside range, add 7. Its children are empty, give 0.
node 15: inside range, add 15, check both sides.
node 18: 18 > 15, skip right, go left, it is empty, gives 0.

Sum = 10 + 7 + 15 = 32. Node 3 was never visited.

Challenges: at first I wrote the simple version that checks all nodes and it gave the right answer. Then I tried to stop completely when a node is out of range (return 0), but that was wrong: in the example node 5 is out of range, but its right child 7 is inside. So I can't throw away the whole node, only one side of it.

## 3. Time Complexity

Time Complexity: O(n) in the worst case.

If all nodes are inside the range, I must visit and add all of them, so it is n steps. When many nodes are outside the range, the skipping makes it much faster, about O(h + k), where h is the height and k is how many nodes are inside the range.

Space Complexity: O(h). This is because of recursion. The computer remembers one call for every level I go down. For a balanced tree it is O(log n), for a "line" tree it is O(n).

## 4. Reflection / Improvement

Time can't be better than O(k) because I have to add every good number at least once. I could rewrite it with my own stack instead of recursion, but it still uses O(h) memory. Using Morris traversal could make memory O(1), but it is much harder and changes the tree for a while, so I did not do it.

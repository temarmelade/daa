# 700. Search in a Binary Search Tree

Link: https://leetcode.com/problems/search-in-a-binary-search-tree/

Language: Python 3

Run: python solution.py

## 1. Problem

We have a binary search tree and a number. We need to find the node with this number and return it (with everything under it). If there is no such node, we return nothing (null).

## 2. Approach

A binary search tree has a simple rule: everything on the left is smaller, everything on the right is bigger. So I don't need to look at every node. I start at the root and ask: is my number smaller or bigger? If smaller, I go left. If bigger, I go right. If equal, I found it. If I fall off the tree (node is empty), the number is not there.

It is like the game "guess the number" where someone says "smaller" or "bigger" after each guess.

Tracing, tree [4, 2, 7, 1, 3], looking for 2:

    4
   / \
  2   7
 / \
1   3

Step 1: node = 4. 2 is smaller than 4, go left.
Step 2: node = 2. 2 equals 2, stop. Answer is the subtree [2, 1, 3].

Tracing, same tree, looking for 5:

Step 1: node = 4. 5 is bigger than 4, go right.
Step 2: node = 7. 5 is smaller than 7, go left.
Step 3: node is empty. Stop. Answer is null.

Challenges: my first idea was to check every node with recursion (left and right both). It worked, but it ignored the BST rule and visited the whole tree, so it was O(n). Then I understood that I only need to go one way at each step. I also wrote it with a while loop instead of recursion so it does not use extra stack memory.

## 3. Time Complexity

Time Complexity: O(h), where h is the height of the tree.

At every step I go one level down, and I never come back up. So the number of steps is at most the height. If the tree is balanced, h is about log n. If the tree is like a long line (all nodes only on one side), h = n, so the worst case is O(n).

Space Complexity: O(1). I only keep one variable "node". No recursion, no extra lists.

## 4. Reflection / Improvement

This is already the best way for this problem. You can't do better than O(h) because you must walk down to the node. The only thing that could help is if the tree was always balanced (like AVL or Red-Black tree), then it is always O(log n). But the tree is given to us, so we can't change that.

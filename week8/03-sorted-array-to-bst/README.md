# 108. Convert Sorted Array to Binary Search Tree

Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Language: Python 3

Run: python solution.py

## 1. Problem

We get an array of numbers sorted from small to big. We need to build a binary search tree from it that is balanced, which means the left and right sides of every node have almost the same height (difference is at most 1).

## 2. Approach

The idea: take the middle number and make it the root. Then all numbers on the left of it are smaller, so they go to the left subtree. All numbers on the right are bigger, so they go to the right subtree. Then I do the same thing again for the left half and for the right half. When the part is empty, I return nothing.

Because I always take the middle, both sides get about the same number of elements, so the tree is balanced.

I use two indexes, left and right, instead of cutting the array into new arrays.

Tracing, nums = [-10, -3, 0, 5, 9]:

make(0, 4): mid = 2, root = 0
  make(0, 1): mid = 0, node = -10
    make(0, -1): empty
    make(1, 1): mid = 1, node = -3
  make(3, 4): mid = 3, node = 5
    make(3, 2): empty
    make(4, 4): mid = 4, node = 9

Result tree:

      0
     / \
  -10   5
     \    \
     -3    9

Output: [0, -10, 5, null, -3, null, 9]. In my test I also check that the inorder traversal gives back the same array (so it is a correct BST) and print the height.

Challenges: my first idea was to just put the numbers one after another, every next one to the right, because each next number is bigger. It is a correct BST but it looks like a long line, so it is not balanced. Then I understood that the root must be the middle. My first version also used slicing like nums[:mid], which makes copies of the array every time. Using left and right indexes is simpler and doesn't copy anything.

## 3. Time Complexity

Time Complexity: O(n).

Every number in the array becomes exactly one node, and making one node takes constant time (find middle, create node). So n numbers means n steps.

Space Complexity: O(log n) extra for recursion, because the tree is balanced and its height is about log n. Plus O(n) for the tree itself, but that is the answer, so we must create it anyway.

## 4. Reflection / Improvement

This is already optimal: we must create n nodes, so we can't be faster than O(n). The slicing version would be O(n log n) because of copying, so using indexes is already the improvement.

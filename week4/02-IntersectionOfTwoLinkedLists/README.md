# 2. Intersection of Two Linked Lists

## Problem

Given the heads of two singly linked lists, return the node where the lists first intersect. If they do not intersect, return `null`.

Two nodes intersect only if they are the **same node object**. Two different nodes containing the same value are not an intersection.

## Approach

I start with each node in list A. For every node in A, I start at the head of list B and compare every node in B with it.

- If `a == b`, both references point to the exact same node, so I return that node.
- Otherwise, I move `b` through list B.
- After reaching the end of B, I move `a` to its next node and scan B again.
- If no shared node is found, I return `null`.

This is a straightforward brute-force solution and is easy to understand, although it repeats work.

## Written Trace

Suppose the lists are:

`A: 4 -> 1 -> 8 -> 4 -> 5`

`B: 5 -> 6 -> 1 -> 8 -> 4 -> 5`

For this illustration, assume the node with value `8` and all nodes after it are physically shared by both lists.

| Outer pointer `a` | Nodes checked by inner pointer `b` | Result |
|---|---|---|
| A's `4` | Every node in B | No identical node |
| A's `1` | Every node in B | No identical node |
| A's shared `8` | B's `5`, `6`, `1`, then shared `8` | `a == b`; return node `8` |

The important comparison is `a == b`, not `a.val == b.val`. Equal values alone do not prove that the nodes are shared.

## Time Complexity

**Time Complexity: O(m × n)**

Let `m` be the number of nodes in list A and `n` the number of nodes in list B. In the worst case, for each of the `m` nodes, the inner loop scans all `n` nodes. Therefore, there can be up to `m × n` comparisons.

## Space Complexity

**Space Complexity: O(1)**

The algorithm uses only two node references and does not store the nodes in another data structure.

## Challenges and Testing

A common mistake is comparing values instead of node references. For example, two separate nodes can both contain `7` without being an intersection.

Useful tests:
- Both lists are empty -> `null`
- One list is empty -> `null`
- Lists have equal values but no shared nodes -> `null`
- Lists share their last node -> return that shared node
- One list's head is already the intersection node -> return that node

When building a manual test, create the shared tail once and attach both lists to that same object. Do not create two separate nodes with the same values.

## Reflection / Improvement

A more efficient two-pointer approach can achieve **O(m + n) time and O(1) extra space**. Use pointers `a` and `b`; when one reaches the end, redirect it to the other list's head. They then travel equal total distances and meet at the intersection node, or both become `null`. This reduces repeated scanning from O(m × n) to O(m + n).

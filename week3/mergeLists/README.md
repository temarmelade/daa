# Linked List Cycle

## 1. Problem

We need to determine whether a linked list contains a cycle.

A cycle exists when following the `next` pointers eventually brings us back to a node that we have already visited.

For example:

3 → 2 → 0 → -4
↑         ↓
└─────────┘

There is a cycle because the node with value `2` is reached again.

## 2. Approach

I use a `HashSet` to store nodes that I have already visited.

I start from the head of the list and move through the nodes one by one.

For every node:

1. Check whether the node is already in the set.
2. If it is already there, a cycle exists.
3. Otherwise, add the node to the set.
4. Move to the next node.

If I reach `null`, the list does not contain a cycle.

### Example trace

Consider:

3 → 2 → 0 → -4
↑         ↓
└─────────┘

Initially:

Set = {}

Visit 3:

Set = {3}

Visit 2:

Set = {3, 2}

Visit 0:

Set = {3, 2, 0}

Visit -4:

Set = {3, 2, 0, -4}

Next node is 2.

2 is already in the set, so a cycle exists.

The algorithm returns `true`.

### Example without a cycle

1 → 2 → 3 → null

Visit 1 → add it.

Visit 2 → add it.

Visit 3 → add it.

Next node is `null`.

The algorithm returns `false`.

## 3. Time Complexity

**Time Complexity: O(n)**

In the worst case, we visit every node once.

The `HashSet` operations `contains()` and `add()` take O(1) average time.

Therefore the total complexity is O(n).

## Space Complexity

**Space Complexity: O(n)**

In the worst case, the set stores all `n` nodes.

## 4. Reflection / Improvement

There is a more memory-efficient solution called Floyd's Cycle Detection Algorithm, also known as the slow and fast pointer method.

It uses two pointers:

- `slow` moves one node at a time.
- `fast` moves two nodes at a time.

If there is a cycle, they will eventually meet.

This approach has:

Time Complexity: O(n)

Space Complexity: O(1)

Therefore, the main improvement would be reducing the extra memory from O(n) to O(1).
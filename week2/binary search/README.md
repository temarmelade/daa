# Binary Search

## Problem

Given a sorted array of integers `nums` in ascending order and an integer `target`, return the index of `target` if it exists in the array. Otherwise, return `-1`.

The algorithm must have a runtime complexity of `O(log n)`.

### Example

```text
Input:  nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
```

The value `9` is located at index `4`.

---

## Approach

This solution uses **binary search**.

We maintain two pointers:

* `left` — the beginning of the search range
* `right` — the end of the search range

At each iteration, we calculate the middle index:

```java
int mid = left + (right - left) / 2;
```

Then we compare `nums[mid]` with `target`.

### Cases

1. If `nums[mid] == target`, we found the target and return `mid`.

2. If `nums[mid] < target`, the target can only be on the right side, so:

```java
left = mid + 1;
```

3. If `nums[mid] > targe

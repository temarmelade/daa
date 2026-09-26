    # First Bad Version

## Problem

You are given `n` versions numbered from `1` to `n`.

At some point, a version becomes bad. Since every version is based on the previous version, all versions after the first bad version are also bad.

An API is provided:

```java
boolean isBadVersion(int version)
```

It returns `true` if the version is bad and `false` otherwise.

The goal is to find the **first bad version** while minimizing the number of API calls.

### Example

```text
Input:  n = 5, bad = 4
Output: 4
```

The versions look like:

```text
1   2   3   4   5
G   G   G   B   B
```

Version `4` is the first bad version.

---

## Approach

This problem can be solved using **binary search**.

We maintain two pointers:

* `left` — the first possible bad version
* `right` — the last possible bad version

At each iteration, we calculate the middle version:

```java
int mid = left + (right - left) / 2;
```

Then we call:

```java
isBadVersion(mid)
```

### Cases

If `mid` is bad:

```java
isBadVersion(mid) == true
```

Then `mid` could be the first bad version, so we **keep it** and search the left half:

```java
right = mid;
```

If `mid` is good:

```java
isBadVersion(mid) == false
```

Then `mid` cannot be the first bad version. Therefore, we search to the right:

```java
left = mid + 1;
```

When `left == right`, both pointers point to the first bad version.

---

## Implementation

```java
public int firstBadVersion(int n) {
    int left = 1;
    int right = n;

    while (left < right) {
        int mid = left + (right - left) / 2;

        if (isBadVersion(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return left;
}
```

---

## Why `right = mid`?

This is important.

If `mid` is bad, it might be the **first** bad version.

For example:

```text
1   2   3   4   5
G   G   G   B   B
            ↑
           mid
```

We cannot remove version `4` from the search.

Therefore:

```java
right = mid;
```

not:

```java
right = mid - 1;
```

---

## Complexity

### Time Complexity

**O(log n)**

Each API call allows us to eliminate approximately half of the remaining versions:

```text
n → n/2 → n/4 → n/8 → ...
```

Therefore, the number of calls to `isBadVersion()` is `O(log n)`.

### Space Complexity

**O(1)**

The algorithm uses only a constant amount of additional memory for `left`, `right`, and `mid`.

---

## Key Idea

This is a binary search for the **first element that satisfies a condition**.

The versions have a monotonic structure:

```text
Good Good Good Bad Bad Bad
```

The rule is:

```text
Good → search right
Bad  → search left, including mid
```

This pattern is useful for many binary search problems where we need to find the **first position satisfying a condition**.

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        remaining = targetSum - root.val
        if root.left is None and root.right is None:
            return remaining == 0
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)


def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    tests = [
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True),
        ([1, 2, 3], 5, False),
        ([1, 2, 3], 4, True),
        ([], 0, False),
        ([1, 2], 1, False),
        ([-2, None, -3], -5, True),
    ]
    s = Solution()
    for values, target, expected in tests:
        root = build_tree(values)
        assert s.hasPathSum(root, target) == expected, (values, target)
        print(values, target, "->", s.hasPathSum(root, target))
    print("All tests passed")

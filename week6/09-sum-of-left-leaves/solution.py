from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, False)

    def dfs(self, node: Optional[TreeNode], is_left: bool) -> int:
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return node.val if is_left else 0
        return self.dfs(node.left, True) + self.dfs(node.right, False)


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
        ([3, 9, 20, None, None, 15, 7], 24),
        ([1], 0),
        ([1, 2, 3, 4, 5], 4),
        ([1, None, 2, 3], 3),
        ([1, 2, None, 3, 4], 3),
    ]
    s = Solution()
    for values, expected in tests:
        result = s.sumOfLeftLeaves(build_tree(values))
        assert result == expected, values
        print(values, "->", result)
    print("All tests passed")

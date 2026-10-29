from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if node.left is None and node.right is None:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return 0

    def minDepthWrong(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + min(self.minDepthWrong(root.left), self.minDepthWrong(root.right))

    def minDepthDfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None:
            return 1 + self.minDepthDfs(root.right)
        if root.right is None:
            return 1 + self.minDepthDfs(root.left)
        return 1 + min(self.minDepthDfs(root.left), self.minDepthDfs(root.right))


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
        ([3, 9, 20, None, None, 15, 7], 2),
        ([2, None, 3, None, 4, None, 5, None, 6], 5),
        ([], 0),
        ([1], 1),
        ([1, 2], 2),
    ]
    s = Solution()
    for values, expected in tests:
        root = build_tree(values)
        assert s.minDepth(root) == expected, values
        assert s.minDepthDfs(root) == expected, values
        print(values, "->", s.minDepth(root))
    print("Wrong version on [2,null,3,null,4,null,5,null,6]:",
          s.minDepthWrong(build_tree([2, None, 3, None, 4, None, 5, None, 6])))
    print("All tests passed")

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        path = []
        self.dfs(root, path, result)
        return result

    def dfs(self, node: Optional[TreeNode], path: List[str], result: List[str]) -> None:
        if node is None:
            return
        path.append(str(node.val))
        if node.left is None and node.right is None:
            result.append("->".join(path))
        else:
            self.dfs(node.left, path, result)
            self.dfs(node.right, path, result)
        path.pop()


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
        ([1, 2, 3, None, 5], ["1->2->5", "1->3"]),
        ([1], ["1"]),
        ([1, 2, 3, 4, 5, 6, 7], ["1->2->4", "1->2->5", "1->3->6", "1->3->7"]),
        ([-1, None, 20], ["-1->20"]),
    ]
    s = Solution()
    for values, expected in tests:
        result = s.binaryTreePaths(build_tree(values))
        assert result == expected, values
        print(values, "->", result)
    print("All tests passed")

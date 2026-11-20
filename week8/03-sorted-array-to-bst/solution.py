class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        def make(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = make(left, mid - 1)
            node.right = make(mid + 1, right)
            return node

        return make(0, len(nums) - 1)


def to_list(root):
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))


if __name__ == "__main__":
    s = Solution()
    for nums in [[-10, -3, 0, 5, 9], [1, 3], [1, 2, 3, 4, 5, 6, 7]]:
        root = s.sortedArrayToBST(nums)
        print(to_list(root), inorder(root) == nums, height(root))

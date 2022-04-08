from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetsum: int) -> bool:
        if not root:
            return False

        stack = []  # [(当前节点，路径数值), ...]
        stack.append((root, root.val))

        while stack:
            cur_node, path_sum = stack.pop()

            if not cur_node.left and not cur_node.right and path_sum == targetsum:
                return True

            if cur_node.left:
                stack.append((cur_node.left, path_sum + cur_node.left.val))

            if cur_node.right:
                stack.append((cur_node.right, path_sum + cur_node.right.val))

        return False

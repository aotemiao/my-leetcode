from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def traversal(node: TreeNode, count: int) -> bool:
            count += node.val
            if not node.left and not node.right:
                if count == targetSum:
                    return True
                else:
                    return False
            if node.left:
                if traversal(node.left, count):
                    return True
            if node.right:
                if traversal(node.right, count):
                    return True
            count -= node.val
            return False

        if not root:
            return False
        return traversal(root, 0)

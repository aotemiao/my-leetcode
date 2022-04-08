from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetsum: int) -> bool:
        def isornot(root, targetsum) -> bool:
            if (not root.left) and (not root.right) and targetsum == 0:
                return True  # 遇到叶子节点，并且计数为0
            if (not root.left) and (not root.right):
                return False  # 遇到叶子节点，计数不为0
            if root.left:
                targetsum -= root.left.val  # 左节点
                if isornot(root.left, targetsum):
                    return True  # 递归，处理左节点
                targetsum += root.left.val  # 回溯
            if root.right:
                targetsum -= root.right.val  # 右节点
                if isornot(root.right, targetsum):
                    return True  # 递归，处理右节点
                targetsum += root.right.val  # 回溯
            return False

        if root == None:
            return False  # 别忘记处理空treenode
        else:
            return isornot(root, targetsum - root.val)

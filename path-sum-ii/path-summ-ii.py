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
            return []

        stack = []  # [(当前节点，路径数值), ...]
        path_list = list()
        path_list.append(root.val)
        stack.append((root, root.val, path_list))
        res = []

        while stack:
            cur_node, path_sum, path_list = stack.pop()
            temp_list = path_list
            if not cur_node.left and not cur_node.right:
                if path_sum == targetsum:
                    res.append(temp_list)
            if cur_node.left:
                stack.append((cur_node.left, path_sum + cur_node.left.val, temp_list.append(cur_node.left.val)))

            if cur_node.right:
                stack.append((cur_node.right, path_sum + cur_node.right.val, temp_list.append(cur_node.right.val)))

        return res

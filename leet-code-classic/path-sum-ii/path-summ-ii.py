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

            if not cur_node.left and not cur_node.right:
                if path_sum == targetsum:
                    res.append(path_list)
            if cur_node.left:
                temp_list = path_list[:]
                temp_list.append(cur_node.left.val)
                stack.append((cur_node.left, path_sum + cur_node.left.val, temp_list))

            if cur_node.right:
                temp_list = path_list[:]
                temp_list.append(cur_node.right.val)
                stack.append((cur_node.right, path_sum + cur_node.right.val, temp_list))

        return res


if __name__ == '__main__':
    print(Solution().pathSum(root=TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None),
                                           TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))),
                             targetsum=22))

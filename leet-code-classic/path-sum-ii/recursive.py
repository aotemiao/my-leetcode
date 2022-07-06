from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetsum: int) -> bool:
        path = []
        res = []

        def isornot(root, count) -> None:
            path.append(root.val)
            count += root.val
            if (not root.left) and (not root.right):
                if count == targetsum:
                    res.append(path[:])
            if root.left:
                isornot(root.left, count)
            if root.right:
                isornot(root.right, count)
            path.pop()



        if root == None:
            return []  # 别忘记处理空treenode
        else:
            isornot(root, 0)
            return res
if __name__ == '__main__':
    print(Solution().pathSum(root=TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None),
                                           TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))),
                             targetsum=22))

from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums: List[int], first: int):
        # 所有数都填完了
        if first == len(nums):
            self.res.append(nums[:])
        for i in range(first, len(nums)):
            # 动态维护数组
            nums[first], nums[i] = nums[i], nums[first]
            # 继续递归填下一个数
            self.backtrack(nums, first + 1)
            # 撤销操作
            nums[first], nums[i] = nums[i], nums[first]


if __name__ == '__main__':
    print(Solution().permute(nums=[1, 2, 3]))

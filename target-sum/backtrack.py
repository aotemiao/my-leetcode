from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result = 0
        if len(nums) == 0: return 0

        def backtrack(nums: List[int], i: int, rest: int):
            global result
            # 结束条件
            if i == len(nums):
                if rest == 0:
                    result += 1
                return
            for op in {+1, -1}:
                # 选择
                rest += op * nums[i]
                # 穷举 nums[i + 1] 的选择
                backtrack(nums, i + 1, rest)
                # 撤销选择
                rest -= op * nums[i]

        backtrack(nums, 0, target)
        return result


if __name__ == '__main__':
    print(Solution().findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))

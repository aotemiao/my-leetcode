from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        memo = dict()

        def dp(nums: List[int], start: int):
            if start >= length: return 0
            if start in memo: return memo[start]
            memo[start] = max(dp(nums, start + 1),
                              nums[start] + dp(nums, start + 2))
            return memo[start]

        return dp(nums, 0)

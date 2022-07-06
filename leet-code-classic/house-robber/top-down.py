from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0] * (length + 2)
        for i in range(length - 1, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        return dp[0]

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        dp_i, dp_i2, dp_i1 = 0, 0, 0
        for i in range(length - 1, -1, -1):
            dp_i = max(nums[i] + dp_i2, dp_i1)
            dp_i2 = dp_i1
            dp_i1 = dp_i
        return dp_i

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -float("inf")
        sum = 0
        for num in nums:
            if num > sum + num:
                sum = num
            else:
                sum += num
            res = max(res, sum)
        return res
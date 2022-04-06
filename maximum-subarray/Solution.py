from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = -2 ** 40
        res = dp
        for index, value in enumerate(nums):
            dp = max(dp + value, value)
            res = max(res, dp)
        return res


if __name__ == '__main__':
    print(Solution().maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))

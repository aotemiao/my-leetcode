from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(nums))]
        # 设dp状态dp[i][0]，表示考虑前i个数，第i个数作为山峰的摆动子序列的最长长度
        # 设dp状态dp[i][1]，表示考虑前i个数，第i个数作为山谷的摆动子序列的最长长度
        dp[0][0] = dp[0][1] = 1
        for i in range(1, len(nums)):
            dp[i][0] = dp[i][1] = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i][0] = max(dp[j][1] + 1, dp[j][0])
                if nums[j] > nums[i]:
                    dp[i][1] = max(dp[j][0] + 1, dp[j][1])
        return max(dp[len(nums) - 1][0], dp[len(nums) - 1][1])

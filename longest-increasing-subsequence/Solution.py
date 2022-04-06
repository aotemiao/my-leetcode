from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 定义dp[i]为以nums[i]结尾的最长递增子序列
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == '__main__':
    print(Solution().lengthOfLIS([20,14,13,13,17,7,19,11,11,9,19,19,19,11,11,17,8,1,19,13]))

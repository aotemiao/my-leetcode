from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 1
        dp = [1] * n
        dp[n - 1] = 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == '__main__':
    print(Solution().lengthOfLIS([20, 14, 13, 13, 17, 7, 19, 11, 11, 9, 19, 19, 19, 11, 11, 17, 8, 1, 19, 13]))

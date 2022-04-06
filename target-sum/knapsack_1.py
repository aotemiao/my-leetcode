from typing import List



class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        total = sum(nums)
        t_sum = (total + target) // 2
        if (total + target) % 2:
            return 0
        if abs(target) > total:
            return 0
        dp = [0] * (t_sum + 1)
        dp[0] = 1
        for i in range(n):
            for j in range(t_sum, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[t_sum]


if __name__ == '__main__':
    print(Solution().findTargetSumWays(nums = [1,1,1,1,1], target = 3))

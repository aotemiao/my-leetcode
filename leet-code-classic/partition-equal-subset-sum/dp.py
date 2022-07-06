from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: return False
        half_total = total // 2
        n = len(nums)
        dp = [0] * (half_total + 1)
        for num in nums:
            for i in range(half_total, -1, -1):
                if i - num > -1:
                    dp[i] = max(dp[i - num] + num, dp[i])
        if dp[half_total] == half_total:
            return True
        return False


if __name__ == '__main__':
    print(Solution().canPartition(nums=[1, 2, 3, 5]))

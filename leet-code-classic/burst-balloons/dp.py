from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        length = len(nums)

        def points(n: int) -> int:
            if n == 0: return 1
            if n == length + 1: return 1
            return nums[n - 1]

        dp = [[0] * (length + 2) for _ in range(length + 2)]
        for i in range(length + 1, -1, -1):
            for j in range(i + 1, length + 2):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + points(k) * points(i) * points(j))
        return dp[0][length + 1]


if __name__ == '__main__':
    print(Solution().maxCoins(nums=[3, 1, 5, 8]))

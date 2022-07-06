from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        if length == 1:
            return cost[0]
        if length == 2:
            return min(cost)
        dp = [0] * length
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, length):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[length - 1], dp[length - 2])


if __name__ == '__main__':
    print(Solution().minCostClimbingStairs(cost=[10, 15, 20]))

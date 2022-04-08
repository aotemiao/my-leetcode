from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        all_weight = sum(stones)
        target = all_weight // 2
        dp = [0] * (target + 1)
        for stone in stones:
            for i in range(target, -1, -1):
                if i >= stone:
                    dp[i] = max(dp[i], dp[i - stone] + stone)
        return all_weight - dp[target] - dp[target]

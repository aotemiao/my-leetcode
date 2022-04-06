from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # m:0
        # n:1
        # dp[i][m][n]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for single_str in strs:
            ones = single_str.count('1')
            zeros = single_str.count('0')
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i - zeros > -1 and j - ones > -1:
                        dp[i][j] = max(dp[i - zeros][j - ones] + 1, dp[i][j])
                    else:
                        dp[i][j] = dp[i][j]
        return dp[m][n]


if __name__ == '__main__':
    print(Solution().findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3))

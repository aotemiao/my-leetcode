from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # m:0
        # n:1
        # dp[i][m][n]
        l = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(l + 1)]
        for x in range(1, l + 1):
            ones = strs[x - 1].count('1')
            zeros = strs[x - 1].count('0')
            for i in range(m + 1):
                for j in range(n + 1):
                    if i - zeros > -1 and j - ones > -1:
                        dp[x][i][j] = max(dp[x - 1][i - zeros][j - ones] + 1, dp[x - 1][i][j])
                    else:
                        dp[x][i][j] = dp[x - 1][i][j]
        return dp[l][m][n]


if __name__ == '__main__':
    print(Solution().findMaxForm(strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3))

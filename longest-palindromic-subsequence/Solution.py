class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        m = len(s)
        dp = [[0] * m for _ in range(m)]
        for i in range(m - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, m):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][m - 1]


if __name__ == '__main__':
    print(Solution().longestPalindromeSubseq(s = "bbbab"))

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # dp[k][n] = floor
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        m = 0
        while dp[k][m] < n:
            m += 1
            for i in range(1, k + 1):
                dp[i][m] = dp[i - 1][m - 1] + dp[i][m - 1] + 1
        return m

if __name__ == '__main__':
    print(Solution().superEggDrop(10, 100))

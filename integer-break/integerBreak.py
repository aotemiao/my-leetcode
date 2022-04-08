class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1
        # if n == 3: return 2
        for i in range(3, n + 1):
            """
                for j in range(1, i):
                    # 拆开
                    dp[i] = max(dp[i], dp[i - j] * j)
                # 不拆（会导致n=3时输出错误答案）
                dp[i] = max(dp[i], i)
            """
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i - j] * j, j * (i - j))
        # 不拆（会导致n=3时输出错误答案）

        return dp[n]


if __name__ == '__main__':
    print(Solution().integerBreak(10))

class Solution:
    def minInsertions(self, s: str) -> int:
        m = len(s)
        dp = [0] * m
        temp = 0
        for i in range(m - 2, -1, -1):
            pre = 0
            for j in range(i+1, m):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = pre
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + 1
                pre = temp
        return dp[m - 1]


if __name__ == '__main__':
    print(Solution().minInsertions(s = "mbadm"))

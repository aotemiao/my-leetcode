class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]  # 匹配0次（其中一项为真即可）
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]  # 匹配一次（其中一项为真即可）
                else:
                    if matches(i, j):
                        f[i][j] = f[i - 1][j - 1]
        return f[m][n]

if __name__ == '__main__':
    print(Solution().isMatch(s="aaa", p="a"))

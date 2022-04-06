class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = dict()

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == -1:
                return j + 1
            if j == -1:
                return i + 1

            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i - 1, j - 1)
            else:
                memo[(i, j)] = min(
                    dp(i, j - 1) + 1,  # 插入
                    dp(i - 1, j) + 1,  # 删除
                    dp(i - 1, j - 1) + 1  # 替换
                )
            return memo[(i, j)]

        return dp(len(word1) - 1, len(word2) - 1)


if __name__ == '__main__':
    print(Solution().minDistance("dinitrophenylhydrazine","benzalphenylhydrazone"))

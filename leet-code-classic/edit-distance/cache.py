from functools import cache


class Solution:
    @cache
    def minDistance(self, word1: str, word2: str) -> int:

        def dp(i, j):

            if i == -1:
                return j + 1
            if j == -1:
                return i + 1

            if word1[i] == word2[j]:
                return dp(i - 1, j - 1)
            else:
                return min(
                    dp(i, j - 1) + 1,  # 插入
                    dp(i - 1, j) + 1,  # 删除
                    dp(i - 1, j - 1) + 1  # 替换
                )
            return dp(i, j)

        return dp(len(word1) - 1, len(word2) - 1)


if __name__ == '__main__':
    print(Solution().minDistance("dinitrophenylhydrazine","benzalphenylhydrazone"))

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(n, k, StartIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(StartIndex, n - (k - len(path)) + 1 + 1):
                path.append(i)
                backtrack(n, k, i + 1)
                path.pop()

        backtrack(n, k, 1)
        return res


if __name__ == '__main__':
    print(Solution().combine(n=4, k=3))

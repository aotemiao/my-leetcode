from typing import List


class Solution:
    def __init__(self):
        self.res = []
        self.path = []
        self.total = 0

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtrack(n, k, 1)
        return self.res

    def backtrack(self, n, k, StartIndex):
        if self.total > n:
            return
        if len(self.path) == k:
            if self.total == n:
                self.res.append(self.path[:])
            return
        for i in range(StartIndex, 10 - (k - len(self.path)) + 1):
            self.path.append(i)
            self.total += i
            self.backtrack(n, k, i + 1)
            self.path.pop()
            self.total -= i


if __name__ == '__main__':
    print(Solution().combinationSum3(k=3, n=9))

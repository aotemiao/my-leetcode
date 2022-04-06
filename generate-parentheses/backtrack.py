from typing import List


class Solution:
    def __init__(self):
        self.track = ''
        self.res = []

    def backtrack(self, left: int, right: int) -> None:
        if left < 0 or right < 0 or left > right:
            return
        if left == 0 and right == 0:
            self.res.append(self.track[:])
        self.track += '('
        self.backtrack(left - 1, right)
        self.track = self.track[:-1]

        self.track += ')'
        self.backtrack(left, right - 1)
        self.track = self.track[:-1]

    def generateParenthesis(self, n: int) -> List[str]:
        self.backtrack(n, n)
        return self.res


if __name__ == '__main__':
    print(Solution().generateParenthesis(5))

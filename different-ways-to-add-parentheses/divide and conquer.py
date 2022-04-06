from typing import List


class Solution:
    MEMO = dict()

    def diffWaysToCompute(self, expression: str) -> List[int]:
        if Solution.MEMO.get(expression):
            return Solution.MEMO[expression]
        res = []
        for index, c in enumerate(expression):
            if c == '+' or c == '-' or c == '*':
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index + 1:])

                for a in left:
                    for b in right:
                        if c == '+':
                            res.append(a + b)
                        if c == '-':
                            res.append(a - b)
                        if c == '*':
                            res.append(a * b)

        # base case
        if not res:
            res.append(int(expression))
        Solution.MEMO[expression] = res
        return res

if __name__ == '__main__':
    print(Solution().diffWaysToCompute(expression = "2*3-4*5"))

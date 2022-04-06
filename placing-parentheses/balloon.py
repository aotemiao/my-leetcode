from typing import List


class Solution:
    def placing_parenthese(self, a: List[int], op: List[str]) -> int:
        def opt(op_l: int, op_r: int, c) -> int:
            if c == '+':
                return op_l + op_r
            if c == '-':
                return op_l - op_r
            if c == '*':
                return op_l * op_r

        n = len(a)
        dp_min = [[float('inf')] * n for _ in range(n)]
        dp_max = [[float('-inf')] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp_min[i][i] = a[i]
            dp_max[i][i] = a[i]
            for j in range(i + 1, n):
                for k in range(i, j):
                    dp_max[i][j] = max(dp_max[i][j],
                                       opt(dp_min[i][k], dp_min[k + 1][j], op[k]),
                                       opt(dp_min[i][k], dp_max[k + 1][j], op[k]),
                                       opt(dp_max[i][k], dp_min[k + 1][j], op[k]),
                                       opt(dp_max[i][k], dp_max[k + 1][j], op[k]),
                                       )
                    dp_min[i][j] = min(dp_min[i][j],
                                       opt(dp_min[i][k], dp_min[k + 1][j], op[k]),
                                       opt(dp_min[i][k], dp_max[k + 1][j], op[k]),
                                       opt(dp_max[i][k], dp_min[k + 1][j], op[k]),
                                       opt(dp_max[i][k], dp_max[k + 1][j], op[k]),
                                       )
        print('max=', dp_max[0][n - 1])
        print('min=', dp_min[0][n - 1])


if __name__ == '__main__':
    print(Solution().placing_parenthese(a=[7, 4, 3, 5], op=['+', '*', '+']))

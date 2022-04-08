class Solution:
    def climbStairs(self, n: int) -> int:
        dbc = 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        dba = 1
        dbb = 2
        for i in range(3, n + 1):
            dbc = dba + dbb
            dba = dbb
            dbb = dbc
        return dbc

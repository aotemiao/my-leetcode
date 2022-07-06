class Solution:
    def minInsertions(self, s: str) -> int:
        res = need = 0
        for ch in s:
            if ch == '(':
                need += 2
                if need % 2 == 1:
                    # 插入一个右括号
                    res += 1
                    # 需要的右括号数量-1（插入了一个，再减去一个，正好凑了两个）
                    need -= 1
            if ch == ')':
                need -= 1
                if need == -1:
                    res += 1
                    need = 1
        return res + need

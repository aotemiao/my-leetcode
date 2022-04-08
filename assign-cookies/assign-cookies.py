from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(key=lambda x: -x)
        s.sort(key=lambda x: -x)
        i = j = res = 0
        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                i += 1
                j += 1
                res += 1
            else:
                j += 1

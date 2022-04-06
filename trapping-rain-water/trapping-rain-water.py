from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max = [-1] * n
        r_max = [-1] * n
        prev = -1
        for i in range(n):
            l_max[i] = height[i] if height[i] > prev else prev
            prev = l_max[i]
        prev = -1
        for i in range(n - 1, -1, -1):
            r_max[i] = height[i] if height[i] > prev else prev
            prev = r_max[i]
        res = 0
        for i in range(n):
            res += min(l_max[i], r_max[i]) - height[i]
        return res
if __name__ == '__main__':
    print(Solution().trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
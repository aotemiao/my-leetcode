from Lib import bisect
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0

        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        f = [envelopes[0][1]]
        for i in range(1, n):
            if (num := envelopes[i][1]) > f[-1]:
                f.append(num)
            else:
                index = bisect.bisect_left(f, num)
                f[index] = num
                # left, right = 0, len(f) - 1
                # loc = right
                # while left <= right:
                #     mid = (left + right) // 2
                #     loc = mid
                #     if envelopes[mid][1] < num:
                #         left = mid + 1
                #     else:
                #         right = mid - 1
                # f[loc] = num
        return len(f)


if __name__ == '__main__':
    print(Solution().maxEnvelopes(
        envelopes=[[15,8],[2,20],[2,14],[4,17],[8,19],[8,9],[5,7],[11,19],[8,11],[13,11],[2,13],[11,19],[8,11],[13,11],[2,13],[11,19],[16,1],[18,13],[14,17],[18,19]]))
    print(bisect.bisect_right([10,11,11,11,12,12,12,13,13],11))
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        len_a, len_b = len(firstList), len(secondList)
        res = []
        while i < len_a and j < len_b:
            left = max(firstList[i][0], secondList[j][0])
            right = min(firstList[i][1], secondList[j][1])
            if left <= right:
                res.append([left, right])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return res


if __name__ == '__main__':
    print(Solution().intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]],
                                          [[1, 5], [8, 12], [15, 24], [25, 26]]))

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))

        head = intervals[0][0]
        tail = intervals[0][1]
        result = []
        for start, end in intervals:
            if start <= tail:
                tail = end if end > tail else tail
            else:
                result.append([head, tail])
                head, tail = start, end
        result.append([head, tail])
        return result


if __name__ == '__main__':
    print(Solution().merge(intervals=[[1, 4], [1, 5]]))


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start point.
        # If two intervals share the same start point
        # put the longer one to be the first.
        intervals.sort(key = lambda x: (x[0], -x[1]))
        result = 0

        prev_end = -1
        for _, end in intervals:
            if end > prev_end:
                result += 1
                prev_end = end

        return result
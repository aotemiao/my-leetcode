from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_range(nums: List[int], start: int, end: int) -> int:
            dp_i, dp_i2, dp_i1 = 0, 0, 0
            for i in range(end, start - 1, -1):
                dp_i = max(nums[i] + dp_i2, dp_i1)
                dp_i2 = dp_i1
                dp_i1 = dp_i
            return dp_i

        length = len(nums)
        if length == 1: return nums[0]
        return max(rob_range(nums, start=1, end=length-1), rob_range(nums, start=0, end=length - 2))


if __name__ == '__main__':
    print(Solution().rob([2, 3, 2]))

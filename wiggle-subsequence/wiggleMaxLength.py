from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        preDiff = 0
        res = 1
        for index in range(1, len(nums)):
            curDiff = nums[index] - nums[index - 1]
            # 若差值为0，则需要跳过，否则有些情况会造成res多加了1
            if curDiff == 0:
                continue
            if (preDiff <= 0 and curDiff > 0) or (preDiff >= 0 and curDiff < 0):
                res += 1
            preDiff = curDiff
        return res

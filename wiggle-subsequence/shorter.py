from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        preC, curC, res = 0, 0, 1  # 题目里nums长度大于等于1，当长度为1时，其实到不了for循环里去，所以不用考虑nums长度
        for i in range(len(nums) - 1):
            curC = nums[i + 1] - nums[i]
            if curC * preC <= 0 and curC != 0:  # 差值为0时，不算摆动
                res += 1
                preC = curC  # 如果当前差值和上一个差值为一正一负时，才需要用当前差值替代上一个差值
        return res

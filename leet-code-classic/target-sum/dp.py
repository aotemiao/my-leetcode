from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = dict()
        length = len(nums)

        def dp(i: int, rest: int):
            if i == length:  # 结束条件
                if rest == 0:
                    return 1
                else:
                    return 0
            if (i, rest) in memo:
                return memo[(i, rest)]
            memo[(i, rest)] = dp(i + 1, rest - nums[i]) + dp(i + 1, rest + nums[i])
            return memo[(i, rest)]

        return dp(0, target)


if __name__ == '__main__':
    print(Solution().findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))

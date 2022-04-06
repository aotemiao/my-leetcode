from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_nums = sum(nums)
        if (target + sum_nums) % 2 == 1: return 0
        if len(nums) == 1:
            if nums[0] == target or nums[0] == -target:
                return 1
            else:
                return 0
        pack_sum = (target + sum_nums) // 2
        dp = [0] * (pack_sum + 1)
        dp[0] = 1

        def sub_set(nums: List[int], rest: int):
            for num in nums:
                for j in range(rest, -1, -1):
                # for j in range(rest, j - num -1, -1):
                    if j - num > -1:
                        dp[j] = dp[j] + dp[j - num]
                    else:
                        dp[j] = dp[j]
            return dp[rest]

        return sub_set(nums, pack_sum)


if __name__ == '__main__':
    print(Solution().findTargetSumWays(nums=[1, ], target=1))

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        for n in nums:
            if not lis or n > lis[-1]:
                lis.append(n)
            else:
                left, right = 0, len(lis) - 1
                loc = right
                while left <= right:
                    mid = (left + right) // 2
                    if lis[mid] >= n:
                        loc = mid
                        right = mid - 1
                    else:
                        left = mid + 1
                lis[loc] = n
        return len(lis)

if __name__ == '__main__':
    print(Solution().lengthOfLIS([20,14,13,13,17,7,19,11,11,9,19,19,19,11,11,17,8,1,19,13]))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k, res, c_dict = -1, 0, {}
        for index, char in enumerate(s):
            if char in c_dict and c_dict[char] > k:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标(判断字符是否在窗口里，不用remove)
                k = c_dict[char]
            else:
                res = max(res, index-k)
            c_dict[char] = index
        return res
if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring(s='tmmzuxt'))

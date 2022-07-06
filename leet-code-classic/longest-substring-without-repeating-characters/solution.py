class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index_end = len(s)
        i, j = 0, 0
        max_sub_len = 0
        while j < index_end:
            substr = s[i:j]
            next_char = s[j]
            # 可优化
            if substr.find(next_char) == -1:
                j += 1
                max_sub_len = max(max_sub_len, j - i)
            else:
                # 左指针并不需要依次递增，即多了很多无谓的循环。 发现有重复字符时，可以直接把左指针移动到第一个重复字符的下一个位置即可。
                i += 1
        return max_sub_len


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring(s=''))

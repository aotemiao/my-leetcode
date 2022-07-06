class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        res = ''

        def longest(s: str, l: int, r: int):
            while l > -1 and r < length and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        for index in range(length):
            if len(longest(s, index, index)) > len(res):
                res = longest(s, index, index)
            if len(longest(s, index, index + 1)) > len(res):
                res = longest(s, index, index + 1)
        return res


if __name__ == '__main__':
    print(Solution().longestPalindrome(s="babad"))

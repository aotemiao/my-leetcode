class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        unpaired_left = 0
        left_need = 0
        for ch in s:
            if ch == '(':
                unpaired_left += 1
            if ch == ')':
                if unpaired_left > 0:
                    unpaired_left -= 1
                else:
                    left_need += 1
        return unpaired_left + left_need


if __name__ == '__main__':
    print(Solution().minAddToMakeValid("()))(("))

class Solution:
    def minInsertions(self, s: str) -> int:
        length = len(s)
        left = index = insert = 0
        while index < length:
            if s[index] == '(':
                left += 1
                index += 1
            else:
                if left > 0:
                    left -= 1
                else:
                    insert += 1
                if index < length - 1 and s[index + 1] == ')':
                    index += 2
                else:
                    index += 1
                    insert += 1
        return insert + left * 2


if __name__ == '__main__':
    print(Solution().minInsertions("()"))

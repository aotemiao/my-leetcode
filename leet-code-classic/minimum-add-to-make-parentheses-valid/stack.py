class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            else:
                if not stack or (stack and stack[-1] == ')'):
                    stack.append(s[i])
                else:
                    stack.pop()

        return len(stack)

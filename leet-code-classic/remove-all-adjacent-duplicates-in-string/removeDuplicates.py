class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = list()
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)

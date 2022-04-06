import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        r = re.search(p, s);
        if r and r.group() == s:
            return True
        else:
            return False
if __name__ == '__main__':
    print(Solution().isMatch(s="aa", p="a*"))

class Solution:
    def isUnique(self, astr: str) -> bool:
        temp_str = ''
        for letter in astr:
            if letter in temp_str:
                return False
            else:
                temp_str += letter
        return True

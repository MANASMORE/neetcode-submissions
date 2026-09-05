class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')','[':']','{':'}'}
        stack = []
        if len(s) == 1:
            return False

        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if char == pairs[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return True
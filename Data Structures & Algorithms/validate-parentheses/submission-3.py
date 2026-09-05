class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')','[':']','{':'}'}
        stack = []

        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if not stack or char != pairs[stack[-1]]:
                    return False

                stack.pop()

        return len(stack) == 0
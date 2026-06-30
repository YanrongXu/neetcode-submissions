class Solution:
    def isValid(self, s: str) -> bool:
        validStack = []
        closeToOpen = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in closeToOpen:
                if validStack and validStack[-1] == closeToOpen[c]:
                    validStack.pop()
                else:
                    return False
            else:
                validStack.append(c)
        return len(validStack) == 0
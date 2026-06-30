class Solution:
    def isValid(self, s: str) -> bool:
        validStack = []

        for c in s:
            if c == ')' and len(validStack) != 0:
                if validStack[-1] == '(':
                    validStack.pop()
                else:
                    return False
            elif c == '}' and len(validStack) != 0:
                if validStack[-1] == '{':
                    validStack.pop()
                else:
                    return False
            elif c == ']' and len(validStack) != 0:
                if validStack[-1] == '[':
                    validStack.pop()
                else:
                    return False
            else:
                validStack.append(c)
        return len(validStack) == 0
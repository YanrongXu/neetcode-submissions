class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            if operation == "+":
                newSum = stack[-1] + stack[-2]
                stack.append(newSum)
            elif operation == "C":
                stack.pop()
            elif operation == "D":
                newNum = stack[-1] * 2
                stack.append(newNum)
            else:
                stack.append(int(operation))
        return sum(stack)
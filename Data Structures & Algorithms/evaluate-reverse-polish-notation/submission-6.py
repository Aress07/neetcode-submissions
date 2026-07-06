class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            stack.append(t)
            if t == '+':
                stack.pop()
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(op2) + int(op1))
            elif t == '*':
                stack.pop()
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(op2) * int(op1))
            elif t == "-":
                stack.pop()
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(op2) - int(op1))
            elif t == "/":
                stack.pop()
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(op2) / int(op1))

        return int(stack[-1])
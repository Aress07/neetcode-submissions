class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                o1 = int(stack.pop())
                o2 = int(stack.pop())
                r = o2 + o1
                stack.append(r)
            elif t == "*":
                o1 = int(stack.pop())
                o2 = int(stack.pop())
                r = o2 * o1
                stack.append(r)
            elif t == "-":
                o1 = int(stack.pop())
                o2 = int(stack.pop())
                r = o2 - o1
                stack.append(r)
            elif t == "/":
                o1 = int(stack.pop())
                o2 = int(stack.pop())
                r = int(o2 / o1)
                stack.append(r)
            else:
                stack.append(int(t))
        return stack[-1]
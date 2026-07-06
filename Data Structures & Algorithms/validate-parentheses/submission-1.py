class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {'(':')',
                    '[':']',
                    '{':'}',
                    ']':'',
                    '}':'',
                    ')':''}

        stack = []

        for i in s:
            if len(stack) > 0:
                if hashMap[stack[-1]] == i:
                    stack.pop()
                else: 
                    stack.append(i)
            else:
                stack.append(i)
            
        return len(stack) == 0
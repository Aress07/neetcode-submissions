class Solution:
    def isValid(self, s: str) -> bool:
        map_ = {"[": "]", 
                "(":")", 
                "{":"}",
                "]": "",
                "}": "",
                ")": ""}
        stack = []

        for c in s:
            if len(stack) > 0:
                if c == map_[stack[-1]]:
                    stack.pop()
                else: 
                    stack.append(c)
            else:
                stack.append(c)

        return len(stack) == 0
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperatures_ = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                temperatures_[idx] = i - idx
            stack.append(i)

        return temperatures_
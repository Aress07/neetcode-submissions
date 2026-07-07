class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            temp = temperatures[i]

            while stack and temp > stack[-1][0] :
                ref = stack.pop()
                distance = i - ref[1]
                arr[ref[1]] = distance
            
            stack.append((temp,i))
        return arr
import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr2 = [[(target - i) / j, i] for i,j in zip(position, speed)]
        arr2.sort(reverse=True, key=lambda x: x[1])
        
        times = []
        for car in arr2:
            time = car
            if times and times[-1][0] >= time[0]:
                continue
            
            times.append(time)
        return len(times)

        
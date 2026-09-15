class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr_ = [[(target - i) / j, i] for i, j in zip(position, speed)]
        arr_.sort(reverse=True, key= lambda x: x[1])

        times = []
        for i in range(len(arr_)):
            if times and arr_[i][0] <= times[-1][0]:
                continue
            else:
                times.append(arr_[i])

        return len(times)
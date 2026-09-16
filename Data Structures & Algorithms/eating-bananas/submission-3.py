import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_ = max(piles)
        min_ = 1

        list_ = range(min_, max_ + 1)
        l, r = 0, len(list_) - 1
        res = list_[r]
        while l <= r:
            
            m = (l + r) // 2
            k = 0
            for p in piles:
                k += math.ceil(p / list_[m])
            if k > h:
                l = m + 1
            else:
                r = m - 1
                res = min(res, list_[m])
        return res

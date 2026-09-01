class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for n in nums:
            hashMap[n] = hashMap.get(n, 0) + 1
            if hashMap[n] > 1:
                return True
        return False
        
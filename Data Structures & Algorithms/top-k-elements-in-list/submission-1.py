class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for n in nums:
            hashMap[n] = hashMap.get(n, 0) + 1
        
        arr = sorted(hashMap.items(), key=lambda x: x[1]) 
        list_ = [_[0] for _ in arr]
        return list_[len(list_) - k:]
        # [1, 2, 4, 4, 2, 2] -> [4, 2]

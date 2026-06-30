class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        r = []
        for n in nums:
            hashMap[n] = hashMap.get(n, 0) + 1

        vals = hashMap.items()
        # sorted(data, key=lambda x: x[1])
        vals = sorted(vals, key=lambda x: x[1])
        for k in vals[len(vals) - k:]:
            r.append(k[0])
        return r
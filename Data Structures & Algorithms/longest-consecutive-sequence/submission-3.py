class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        lengths = []
        # length = 1
        hashMap = {}
        # m = min(nums)
        for num in nums:
            m = num
            length = 1
            while m + 1 in nums:
                length += 1
                m += 1
            lengths.append(length)
        return max(lengths)
        
            
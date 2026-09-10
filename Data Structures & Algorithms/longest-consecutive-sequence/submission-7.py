class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_ = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in set_:
                length = 0
                while n + length in set_:
                    length += 1
                longest = max(length, longest)
        
        return longest
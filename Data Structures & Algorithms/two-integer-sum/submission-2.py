class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # 3, 4, 5, 6 - 7
    # 3: 0
    # [0, 1]

        hashMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i

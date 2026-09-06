class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # 3, 4, 5, 6 - 7
    # 3: 7-3=4
    # 4:

        hashMap = {}
        for i, n in enumerate(nums):
            if target - n in hashMap: return [hashMap[target - n][1], i]
            hashMap[n] = [target - n, i]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        length = len(nums)

        for i in range(length):
            if target - nums[i] not in hashMap:
                hashMap[nums[i]] = i
            else:
                return [hashMap[target - nums[i]], i]
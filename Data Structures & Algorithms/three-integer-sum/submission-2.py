class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        nums.sort()
        for i in range(len(nums)):
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    if [nums[l], nums[r], nums[i]] not in arr:     
                        arr.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return arr
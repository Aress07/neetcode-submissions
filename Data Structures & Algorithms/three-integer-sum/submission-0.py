class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        nums = sorted(nums)
        for i in range(len(nums)):
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    if [nums[i], nums[l], nums[r]] not in arr:
                        arr.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return arr

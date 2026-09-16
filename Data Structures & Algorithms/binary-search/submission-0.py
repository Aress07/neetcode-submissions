class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            middle_idx = (l + r) // 2

            if nums[middle_idx] == target: return middle_idx
            elif nums[middle_idx] > target: r -= 1
            else: l += 1
        return -1
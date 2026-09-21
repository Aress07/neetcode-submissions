class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = nums[0]
        inf = 0
        l, r = 0, len(nums) - 1
        if len(nums) == 2:
            if target == nums[0]: return 0
            if target == nums[1]: return 1
            else: return -1
        while l <= r:
            if nums[l] < nums[r]: 
                if nums[l] <= res:
                    res = nums[l]
                    inf = l
                    break
            m = l + (r - l) // 2
            if nums[m] <= res:
                res = nums[m]
                inf = m
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        l1, r1 = 0, inf - 1
        l2, r2 = inf, len(nums) - 1

        while l1 <= r1:
            m1 = l1 + (r1 - l1) // 2
            if nums[m1] == target: return m1
            elif target > nums[m1]: l1 = m1 + 1
            else: r1 = m1 - 1

        while l2 <= r2:
            m2 = l2 + (r2 - l2) // 2
            if nums[m2] == target: return m2
            elif target > nums[m2]: l2 = m2 + 1
            else: r2 = m2 - 1

        return -1


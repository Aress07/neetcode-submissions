class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = [1] * len(nums), [1] * len(nums)

        k = 1
        for i in range(1, len(nums)):
            k *= nums[i-1]
            pre[i] = k
        
        k = 1
        for i in range(len(nums) - 2, -1, -1):
            k *= nums[i+1]
            post[i] = k

        prod = []
        for i in range(len(nums)):
            prod.append(pre[i] * post[i])

        return prod
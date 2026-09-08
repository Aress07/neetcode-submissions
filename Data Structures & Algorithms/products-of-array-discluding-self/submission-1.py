class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = [1] * len(nums), [1] * len(nums)
        res = [1] * len(nums)
        cum = 1
        for n in range(len(nums)):
            pre[n] = cum
            cum *= nums[n]

        cum_ = 1
        for n in range(len(nums)-1, -1, -1):
            post[n] = cum_
            cum_ *= nums[n]

        for k in range(len(nums)):
            res[k] = pre[k] * post[k]

        return res
            
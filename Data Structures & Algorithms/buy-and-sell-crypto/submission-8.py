class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0
        for i in range(len(prices)):
            if prices[l] < prices[i]:
                maxP = max(maxP, prices[i] - prices[l])
            else:
                l = i
        return maxP
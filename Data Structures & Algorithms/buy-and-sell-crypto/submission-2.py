class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Dynamic Programming method:
        maxProfit=0
        lowestPrice=prices[0]
        for curPrice in prices:
            maxProfit=max(maxProfit,curPrice-lowestPrice)
            lowestPrice=min(lowestPrice,curPrice)
        return maxProfit
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # The Two pointer method
        buy,sell=0,1
        maxProfit=0
        while sell<len(prices):
            if prices[buy]<prices[sell]:
                curProfit=prices[sell]-prices[buy]
                maxProfit=max(maxProfit,curProfit)
            else:
                buy=sell
            sell+=1
        return maxProfit
        
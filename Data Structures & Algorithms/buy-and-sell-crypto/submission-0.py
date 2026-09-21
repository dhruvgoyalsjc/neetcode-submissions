class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        bestBuyDay = 0

        # iterate thru possible sell days
        for i, price in enumerate(prices):
            if (i == 0):
                continue
            
            currProfit = price - prices[bestBuyDay]
            if (currProfit > maxProfit):
                maxProfit = currProfit

            if price < prices[bestBuyDay]:
                bestBuyDay = i
        
        return maxProfit
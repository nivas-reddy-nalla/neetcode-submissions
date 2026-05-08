class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, curBuy = 0, float("inf")

        for price in prices:
            if curBuy > price:
                curBuy = price
            else:
                profit = max(profit, price-curBuy)
        
        return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_buy = float('inf')
        max_profit = 0

        for price in prices:
            if price<cur_buy:
                cur_buy = price
            else:
                max_profit = max(max_profit, price-cur_buy)
        return max_profit
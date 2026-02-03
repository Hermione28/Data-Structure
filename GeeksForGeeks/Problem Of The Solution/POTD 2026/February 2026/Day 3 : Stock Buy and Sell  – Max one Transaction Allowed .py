class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        min_price = float('inf')  # initialize to a very large number
        max_profit = 0
        
        for price in prices:
            # update minimum price so far
            if price < min_price:
                min_price = price
            # calculate profit if sold today
            profit = price - min_price
            # update maximum profit
            if profit > max_profit:
                max_profit = profit
        
        return max_profit


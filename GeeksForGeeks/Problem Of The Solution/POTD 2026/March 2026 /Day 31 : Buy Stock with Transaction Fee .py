class Solution:
    def maxProfit(self, arr, k):
        if not arr:
            return 0
        
        hold = -arr[0]   # buying first stock
        cash = 0         # no stock, no profit
        
        for price in arr[1:]:
            prev_hold = hold
            
            hold = max(hold, cash - price)
            cash = max(cash, prev_hold + price - k)
        
        return cash

def maxProfit(prices):
        buy = 0
        sell = 1
        profit = 0
        
        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
                sell = buy + 1
            else:
                dayProfit = prices[sell] - prices[buy]
                profit = max(profit,dayProfit)
                sell += 1
        return profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
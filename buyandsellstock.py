prices = [7,1,5,3,6,4]
def maxprofit(prices):
    high = -10
    for i in range(len(prices)):
        check = prices[i]
        val = 0
        for j in range(i+1,len(prices)):
            val = val + prices[j-1]-prices[j]
            high = max(high,val)
maxprofit(prices)

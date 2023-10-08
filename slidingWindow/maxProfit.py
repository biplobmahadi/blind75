def maxProfit(prices):
    maxP, p, i, j = 0, 0, 0, 1
    while j<len(prices):
        total = p + (prices[j]-prices[i])
        if total<0:
            p = 0
        else:
            maxP = max(maxP, total)
            p = total
        i+=1 
        j+=1
    return maxP

prices = [7, 1, 5, 3, 6, 4]

def maxProfitBrute(prices):
    profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = max(profit, prices[j] - prices[i])
    return profit


def maxProfitOptimal(prices):
    maxP, l, r = 0, 0, 1
    while r<len(prices):
        if prices[r]>prices[l]:
            maxP = max(maxP, prices[r] - prices[l])
        else:
            l = r
        r+=1
    return maxP

print(maxProfit(prices))
print(maxProfitBrute(prices))
print(maxProfitOptimal(prices))
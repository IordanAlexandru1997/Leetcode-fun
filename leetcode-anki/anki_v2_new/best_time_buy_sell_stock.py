def maxProfit(prices):
    maxP, minVal = 0, float("inf")
    for p in prices:
        minVal = min(minVal, p)
        maxP = max(p - minVal, maxP)
    return maxP

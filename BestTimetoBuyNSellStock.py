"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

"""
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0
    delta = 0
    profit = 0
    pastStockPrice = prices[0]
    for i in range(len(prices)):
        priceOfStock = prices[i]
        delta = priceOfStock - pastStockPrice
        if delta > 0:
            profit += delta
        elif delta <0:
            profit += pastStockPrice
            profit -= priceOfStock
        else:
            continue
        pastStockPrice = priceOfStock
    return profit

print(maxProfit([1,2,4,5,2,3,1]))
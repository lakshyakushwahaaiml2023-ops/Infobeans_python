def bttbs(prices):
    min_price = prices[0]
    max_profit = 0
    profit = 0
    for price in prices[1:]:
        min_price = min(price, min_price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit

prices = [7,5,1,2,6]
print(bttbs(prices))
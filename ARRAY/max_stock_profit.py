def max_stock_profit(prices):
    if len(prices) < 2:
        return f"{prices} : 0"
    
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
    
    return f"{prices} : {max_profit}"

a1 = [1, 3, 4, 5, 3, 6, 3, 101]
a2 = [7]
a3 = []
a4 = [7, 10, 1, 3, 6, 9, 2]
a5 = list(eval(input("Enter a list\n:")))

print(max_stock_profit(a1))
print(max_stock_profit(a2))
print(max_stock_profit(a3))
print(max_stock_profit(a4))
print(max_stock_profit(a5))
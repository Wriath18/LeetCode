def buy_sell(prices):
    arr = []
    for i in range(0, len(prices)):
        for j in range(0, len(prices)):
            if i < j:
                arr.append((prices[j] - prices[i]))


    val = max(arr)
    if val <= 0:
        return 0
    else:
        return val



val = buy_sell([7,6,4,3,1])

print(val)

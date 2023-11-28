def candy(ratings):
    count = 0
    n = len(ratings)
    candies = [1] * n
    for i in range(1,n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
        elif ratings[i] == ratings[i-1]:
            continue

    
    for i in range(n-2,-1,-1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
        elif ratings[i] == ratings[i+1]:
            continue

    return sum(candies)


val = candy([1,0,2])
print(val)
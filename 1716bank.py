def bank(n):
    sum = 0
    last_monday = 1
    curr_day = 1
    count = 0
    for i in range(1,n+1):
        sum += last_monday
        if curr_day == 7:
            curr_day = 1
            count = 0
        while(count <= 7):
            prev_day += 1
            sum += (prev_day + 1)
            count += 1
        
    
    print(sum)

bank(4)

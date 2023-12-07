def largest(num):
    
    if int(num) % 2 == 0:
        l = list(num)
        largest = 0
        current = 0

        for i in l:
            i = int(i)
            if i % 2 != 0:
                current = current * 10 + i
                largest = max(current, largest)
            else:
                current = 0

        if largest == 0:
            return ""
        else:
            return str(largest)
    


val = largest("10133890")
print(val)
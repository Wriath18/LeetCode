def check(num):
    sum = 0
    while(num > 0):
        mod = num % 10
        sum += mod
        num //= 10

    return sum

def reduce(num):
    while num >= 10:
        num = check(num)
    return num

while True:
    num = int(input("Ennter the number:  "))
    result = reduce(num)
    print(result)

    

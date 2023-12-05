def teama(n):
    count = 0
    if n!= 1 or n != 0:
        while(n!=1):
            if n%2 ==0:
                count += n//2
                n //= 2
            else:
                count += (n-1)//2
                n = ((n-1)//2) + 1

        return count
    else:
        return n




val = teama(7)
print(val)
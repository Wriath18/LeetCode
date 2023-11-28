def hindex(nums):
    nums_s = sorted(nums, reverse=True)
    for i, num in enumerate(nums_s):
        if (num > i+1):
            continue
        elif(num <= i+1):
            return num
        

val = hindex([1,3,1])
print(val)
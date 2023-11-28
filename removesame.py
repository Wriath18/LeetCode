def remove(nums):
    k = 0
    res = []
    [res.append(x) for x in nums if x not in res]
    for i in range(len(res)):
        nums[i] = res[i]
    
    print(nums)
    return (len(res))

val = remove([0,0,1,1,1,2,2,3,3,4])
print(val)
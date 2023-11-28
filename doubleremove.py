def remove(nums):
    k = 0
    for i in range(len(nums)-1):
        val = nums[i]
        if nums[i+1] == val:
            j = i
            while(nums[j] == val and j <= 2):
                nums[i] = nums[j]
                j += 1
            k = j
        
    
    print(nums)
    return k

val = remove([1,1,1,2,2,3])
print(val)

        
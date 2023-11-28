def remove(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1

    print(nums)
    return i


val = remove([0,1,2,2,3,0,4,2], 2)
print(val)
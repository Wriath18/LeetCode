def rotate(nums, k):
    temp2 = nums[:(len(nums) - k)]  # Get the first three elements
    temp = nums[-k:] 

    nums = temp
    nums += temp2
    print(nums)

    # print(temp)
    # print(temp2)

rotate([1,2,3,4,5,6,7], 3)

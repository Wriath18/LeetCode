def can_jump(nums):
    maxi = 0
    last = len(nums) - 1
    for i, num in enumerate(nums):
        if i > maxi:
            return False
        maxi = max(maxi, i + num)

        if maxi >= last:
            return True
        


val = can_jump([2,3,1,1,4])
print(val)

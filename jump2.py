# def can_jump(nums):
#     maxi = 0
#     last = len(nums) - 1
#     for i, num in enumerate(nums):
#         if i > maxi:
#             return False
#         maxi = max(maxi, i + num)

#         if maxi >= last:
#             return True
        


def can_jump(nums):
    maximum = 0
    jumps = 0
    end = 0
    last = len(nums)-1
    for i, num in enumerate(nums):
        maximum = max(maximum, i + num)
        if i == end:
            jumps += 1
            end = maximum

        if maximum >= last:
            return jumps
        
    return jumps

            


val = can_jump([2,3,1,1,4])
print(val)
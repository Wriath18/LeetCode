# def profuct(nums):
#     answer = []
#     for i, num in enumerate(nums):
#         product = 1
#         for j in nums:
#             product *= j

#         answer.append(product//num)

#     print(answer)


# def profuct(nums):
#     answer = []
#     for num in nums:
#         product = 1
#         for j in nums:
#             if j != num:
#                 product *= j
#         answer.append(product)

#     print(answer)

# profuct([-1,1,0,-3,3])


def product(nums):
    answer = []
    for i, num in enumerate(nums):
        product = 1
        for j in range(0,i):
            product *= nums[j]
        for k in range(i+1, len(nums)):
            product *= nums[k]

        answer.append(product)

    print(answer)

for i, num in enumerate([1,2,3,4]):
    print(f"{num} = {i}")

product([-1,1,0,-3,3])
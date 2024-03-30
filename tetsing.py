# # def generate_combinations(arr):
# #     def backtrack(index, path):
# #         if index == len(arr):
# #             combinations.append(path)
# #             return
# #         for operator in ['+', '-']:
# #             if index == 0:
# #                 backtrack(index + 1, str(arr[index]))
# #             else:
# #                 backtrack(index + 1, f'{path}{operator}{arr[index]}')
# #                 backtrack(index + 1, f'{path}{operator}{-arr[index]}')

# #         for i in range(index + 1, len(arr)):
# #             backtrack(i + 1, f'{path}+{arr[index]}+{arr[i]}')
# #             backtrack(i + 1, f'{path}+{arr[index]}-{arr[i]}')
# #             backtrack(i + 1, f'{path}-{arr[index]}+{arr[i]}')
# #             backtrack(i + 1, f'{path}-{arr[index]}-{arr[i]}')

# #     arr.sort()
# #     combinations = []
# #     backtrack(0, '')
# #     return list(set(combinations))

# # # Example usage:
# # array = [1, 2, 3]
# # result = generate_combinations(array)
# # print("All possible combinations:", result)

# def generate_combinations(arr):
#     def backtrack(index, path):
#         if index == len(arr):
#             combinations.append(path)
#             return
#         for operator in ['+', '-']:
#             if index == 0:
#                 backtrack(index + 1, str(arr[index]))
#             else:
#                 backtrack(index + 1, f'{path}{operator}{arr[index]}')
#                 backtrack(index + 1, f'{path}{operator}{-arr[index]}')

#         for i in range(index + 1, len(arr)):
#             for operator in ['+', '-']:
#                 backtrack(i + 1, f'{path}{operator}{arr[index]}{operator}{arr[i]}')

#     combinations = []
#     backtrack(0, '')
#     return list(set(combinations))

# # Example usage:
# array = [1, 2, 3]
# result = generate_combinations(array)
# print("All possible combinations:", result)



def generate_operand_combinations(arr):
    def backtrack(index, expression):
        if index == len(arr):
            operand_combinations.append(expression)
            return
        # Add the current element
        backtrack(index + 1, expression + arr[index])
        # Subtract the current element
        backtrack(index + 1, expression + arr[index])

    operand_combinations = []
    backtrack(1, arr[0])
    return operand_combinations

def generate_all_combinations(arr):
    combinations = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                combinations.append([arr[i], arr[j], arr[k]])
    return combinations

def generate_all_operand_combinations(arr):
    all_combinations = generate_all_combinations(arr)
    operand_combinations = []
    for combination in all_combinations:
        operand_combinations.extend(generate_operand_combinations(combination))
    return operand_combinations

# Example usage:
arr = [1, 2, 3, 4]
all_operand_combinations = generate_all_operand_combinations(arr)
print(all_operand_combinations)

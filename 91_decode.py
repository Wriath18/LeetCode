def decode_patterns(s: str) -> list:
    if not s or s[0] == '0':
        return []

    stack = [([], 0)]
    results = []

    while stack:
        path, index = stack.pop()

        if index == len(s):
            results.append(path)
            continue

        # Check for single digit decode
        if s[index] != '0':
            stack.append((path + [s[index]], index + 1))

        # Check for double digit decode
        if index + 1 < len(s) and '10' <= s[index:index + 2] <= '26':
            stack.append((path + [s[index:index + 2]], index + 2))

    return results

# Example usage
decoded_patterns = decode_patterns("226")
decoded_patterns



# def decode_patterns(s: str) -> list:
#     def backtrack(index, path):
#         # When we reach the end of the string, add the current path to the results
#         if index == len(s):
#             results.append(path.copy())
#             return
        
#         # Single digit decode (must not be '0')
#         if s[index] != '0':
#             path.append(s[index])
#             backtrack(index + 1, path)
#             path.pop()
        
#         # Double digit decode (must be between 10 and 26)
#         if index < len(s) - 1 and '10' <= s[index:index + 2] <= '26':
#             path.append(s[index:index + 2])
#             backtrack(index + 2, path)
#             path.pop()

#     results = []
#     backtrack(0, [])
#     return results

# # Test the function with different lengths
# test_numbers = ["12"]
# decoded_patterns = {num: decode_patterns(num) for num in test_numbers}
# decoded_patterns


def majority(nums):
    mydict = {}
    for i in nums:
        if i in mydict:
            mydict[i] += 1
        else:
            mydict[i] = 1

    majority_element = None  # Initialize the majority element to None
    max_count = 0  # Initialize the maximum count to 0
        
    for num, count in mydict.items():
        if count > max_count:
            majority_element = num  # Update the majority element if a new one is found
            max_count = count

    return majority_element

val = majority([2,1,1,1,1,2,2])
print(val)
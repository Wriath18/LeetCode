# def gasstation(gas, cost):
#     lenght = len(gas)
    
#     i = 0
#     while(i < lenght):
#         tank = 0
#         j = i
#         current = i
#         while(tank >= 0):
#             if j == lenght:
#                 j = 0
#             tank += gas[j]
#             tank -= cost[j]
#             j += 1
#             if (j == current):
#                 return i
            
#         i += 1

#     return -1

def gasstation(gas, cost):
    length = len(gas)
    for i, num in enumerate(gas):
        tank = 0
        j = i
        current = i
        while(tank >= 0):
            if j == length:
                j = 0
            tank += gas[j]
            tank -= cost[j]
            if (tank < 0):
                break
            else:
                j += 1
            if (j == current):
                return i
            
    return -1


val = gasstation([2,3,4],[3,4,3])
print(val)



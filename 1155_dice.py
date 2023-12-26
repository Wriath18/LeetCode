from itertools import product

class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """

def count_sum(n, k, target):
    all_combinations = product(range(1, k+1), repeat=n)
    valid_combinations = [combo for combo in all_combinations if sum(combo) == target]
    val = len(valid_combinations)
    if val >  10000:
        return int(val % ((10**9) + 7))
    else:
        return val


s = Solution
val = count_sum(n=30, k=30, target=500)
print(val)

        
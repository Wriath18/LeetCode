import numpy as np
import math
class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ideal_val = math.floor((len(arr) * 0.25))
        new_arr = np.array(arr)
        b = np.unique(new_arr, return_counts=True)
        for i in range(len(arr)):
            if b[1][i] > ideal_val:
                return b[0][i]

        



s = Solution()
val = s.findSpecialInteger([1,2,2,6,6,6,6,7,10])
print(val)
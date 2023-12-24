# class Solution(object):
#     def maxProduct(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         final = []
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 final.append((nums[i]-1)*(nums[j]-1))

#         return max(final)

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        final = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i]-1)*(nums[j]-1) > final:
                    final = (nums[i]-1)*(nums[j]-1)

        return final
    

s = Solution()
val = s.maxProduct([1,5,4,5])
print(val)
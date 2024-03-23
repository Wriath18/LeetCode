class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        sums = {}
        for i in range(len(nums)):
            elements = 0
            sum = 0
            ind = i
            for j in range(i, len(nums)):
                if sum <= target:
                    sum += nums[i]
                    elements += 1
                    
            sums[elements] = ind

        return sums
        

s = Solution()
val  = s.minSubArrayLen(7, [2,3,1,2,4,3])
print(val)
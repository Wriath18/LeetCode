class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sorted_nums = sorted(nums)
        triplets = []

        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
                
            for l in range(i + 1, len(sorted_nums) - 1):
                if l > i + 1 and sorted_nums[l] == sorted_nums[l - 1]:
                    continue

                for r in range(len(sorted_nums) - 1, l, -1):
                    if r < len(sorted_nums) - 1 and sorted_nums[r] == sorted_nums[r + 1]:
                        continue
                        
                    if sorted_nums[i] + sorted_nums[l] + sorted_nums[r] == 0:
                        triplets.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                        break

        return triplets

    

S = Solution()
val = S.threeSum([-1,0,1,2,-1,-4])
print(val)
            
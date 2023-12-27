class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        total_time = 0
        max_time = 0

        for i in range(len(colors)):
            # If it's the first balloon or a different color, update max_time
            if i == 0 or colors[i] != colors[i - 1]:
                max_time = neededTime[i]
            else:
                # Increment total time by the lesser of the two adjacent same-colored balloons
                total_time += min(max_time, neededTime[i])
                # Update max_time to the higher of the two
                max_time = max(max_time, neededTime[i])
        
        return total_time





s = Solution()
s.minCost("aabaa", [1,2,3,4,1])
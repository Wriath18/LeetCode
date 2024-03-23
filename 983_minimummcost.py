class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        min_cost = 0
        one_day_index = 0
        seven_day_index = 0
        thirty_day_index = 0
        
        for i in range(len(days)):
            day = days[i]
            one_day_cost = min_cost + costs[0]
            
            while days[seven_day_index] <= day - 7:
                seven_day_index += 1
            
            seven_day_cost = min_cost + costs[1] if seven_day_index == 0 else min_cost + costs[1] - costs[0] * (day - days[seven_day_index - 1])
            
            while days[thirty_day_index] <= day - 30:
                thirty_day_index += 1
            
            thirty_day_cost = min_cost + costs[2] if thirty_day_index == 0 else min_cost + costs[2] - costs[0] * (day - days[thirty_day_index - 1])
            
            min_cost = min(one_day_cost, seven_day_cost, thirty_day_cost)
        
        return min_cost

    


# class Solution:
#   def mincostTickets(self, days, costs):
#     min_cost = 0
#     current_day = 0
#     i = 0

#     while i < len(days):
#       if days[i] > current_day:
#         cheapest_pass = min(costs)
#         days_to_cover = days[i] - current_day
#         if days_to_cover >= 30:
#           cheapest_pass = costs[2]
#         elif days_to_cover >= 7:
#           cheapest_pass = costs[1]
#         min_cost += cheapest_pass
#         current_day = max(days[i], current_day + 30, current_day + 7, current_day + 1)
#       i += 1

#     return min_cost

        


s = Solution()
val = s.mincostTickets([1,4,6,7,8,20],[2,7,15])
print(val)
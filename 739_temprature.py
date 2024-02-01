class Solution(object):
    def dailyTemperatures(self, temperatures) -> list:
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        days = [i*0 for i in temperatures]
        print(days)
        for i in range(len(temperatures)):
            mark = 0
            flag = False
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    flag = True
                    mark = (j-i)
                    break
            days[i] = mark if flag == True else 0

        return days
    

s = Solution()
val = s.dailyTemperatures([30,40,50,60])
print(val)

             

class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        return min(self.returncount(s, '0'), self.returncount(s, '1'))


    def returncount(self, s, start):
        s = list(s)
        print(len(s))
        count = 0

        for i in range(len(s)):
            if s[i] == start:
                count += 1
            start = '1' if start == '0' else '0'
        return count
    

s = Solution()
val = s.minOperations("10")
print(val)



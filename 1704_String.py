class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        arr = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        l = len(s)
        str1, str2 = s[0:(l//2)], s[l//2:]
        count1 = sum([i in arr for i in str1])
        count2 = sum([j in arr for j in str2])
        
        return True if count1 == count2 else False
            


s = Solution()
val = s.halvesAreAlike("textbook")
print(val)
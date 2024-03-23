# class Solution(object):
#     def longestCommonSubsequence(self, text1, text2):
#         """
#         :type text1: str
#         :type text2: str
#         :rtype: int
#         """
#         last_index = 0
#         count = 0
#         for i in range(len(text2)):
#             if text2[i] in text1:
#                 found_index = text1.index(text2[i], last_index)
#                 if found_index >= last_index:
#                     last_index = found_index
#                     count += 1
#                     continue
#                 else:
#                     return 0
#             else:
#                 continue
                
#         return count

# class Solution(object):
#     def longestCommonSubsequence(self, text1, text2):
#         db = []
#         for i in range(len(text2)):
#             if text2[i] in text1:
#                 db.append(i)
#             else:
#                 continue

#         return len(db) if db == db.sort() else 0

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        db = []
        last_index = -1
        for i in range(len(text2)):
            if text2[i] in text1:
                try:
                    found_index = text1.index(text2[i], last_index + 1)
                except:
                    continue
                if found_index >= last_index:
                    db.append(i)
                    last_index = found_index
                else:
                    continue
        return len(db)


# class Solution(object):
#     def longestCommonSubsequence(self, text1, text2):
#         """
#         :type text1: str
#         :type text2: str
#         :rtype: int
#         """
#         count = 0
#         last_index = 0
        
#         for char in text2:
#             if char in text1:
#                 found_index = text1.find(char, last_index + 1)
#                 if found_index >= last_index:
#                     count += 1
#                     last_index = found_index
#                 else:
#                     return 0
#             else:
#                 return 0
#         return count


s = Solution()
val = s.longestCommonSubsequence("ezupkr","ubmrapg")
print(val)
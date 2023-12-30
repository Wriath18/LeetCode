import collections
class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        # longest_word = max(words, key=len)
        # index = words.index(longest_word)

        # for i in words:
        #     for j in words[index]:
        #         if j not in i:
        #             i += j
        #             words[index] = words[index].replace(j, "")

        # # Check if all words are now equal
        # print(words)
        # return all(word == longest_word for word in words)
        char_counts = collections.Counter()
        for word in words:
            char_counts.update(word)

        # Check if every character count is divisible by the number of words
        return all(count % len(words) == 0 for count in char_counts.values())

                    




s = Solution()
val = s.makeEqual(["abc","aabc","bc"])
print(val)
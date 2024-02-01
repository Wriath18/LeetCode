import random
class RandomizedSet(object):

    def __init__(self):
        self.nums = set()
        self.pos = dict()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.nums:
            self.nums.add(val)
            self.pos[val] = len(self.nums) - 1
            return True
        
        return False
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.nums:
            idpos = self.pos[val]
            last_num = list(self.nums)[-1]
            self.nums.remove(val)
            del(self.pos[val])
            if idpos != len(self.nums) - 1:
                self.pos[last_num] = idpos
            return True
        return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choie(list(self.nums))
        
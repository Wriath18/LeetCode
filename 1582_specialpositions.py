class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        final = 0
        rows = len(mat)
        cols = len(mat[0])
        for i in range(0,rows):
            for j in range(0, cols):
                if mat[i][j] == 1:
                    count = 0
                    for k in range(0, cols):
                        if mat[i][k] == 1:
                            count += 1
                    for k in range(0, rows):
                        if mat[k][j] == 1:
                            count += 1
                    if count == 2:
                        final += 1

        return final
                    

s = Solution()
s.numSpecial([[1,0,0],[0,1,0],[0,0,1]])
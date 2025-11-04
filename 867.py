class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n=len(matrix)
        n1=len(matrix[0])
        m=[[matrix[i][j] for i in range(n)] for j in range (n1)]
        for i in range(n1):
            for j in range(n):
                (m[i])[j]=(matrix[j])[i]
        return m

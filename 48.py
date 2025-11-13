class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        import copy
        n=len(matrix)
        m=copy.deepcopy(matrix)
        for i in range(n):
            for j in range(n):
                matrix[j][n-i-1]=m[i][j]

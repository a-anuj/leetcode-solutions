class Solution(object):
    def setZeroes(self, matrix):
        rows = []
        cols = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    rows.append(i)
                    cols.append(j)
        
        for i in range(len(matrix)):
            if i in rows:
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j in cols:
                    matrix[i][j]=0
        
        return matrix
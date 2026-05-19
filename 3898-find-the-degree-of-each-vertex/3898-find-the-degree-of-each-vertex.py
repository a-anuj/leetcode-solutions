class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        count = 0
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    count+=1
            res.append(count)
            count = 0
        return res
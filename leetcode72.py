class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rowL, colL = len(word1) + 1, len(word2) + 1
        def initMatrix():
            res = [[0] * colL for i in range(rowL)]
            for i in range(rowL):
                res[i][0] = i
            for i in range(colL):
                res[0][i] = i
            return res
        matrix = initMatrix()

        def getCurrentStep(r,c):
            if word1[r-1] == word2[c-1]:
                return min(matrix[r][c-1] + 1, matrix[r-1][c] + 1, matrix[r-1][c-1])
            else:
                return min(matrix[r][c-1] + 1, matrix[r-1][c] + 1, matrix[r-1][c-1] + 1)
            return 1
        for i in range(1, rowL):
            for j in range(1, colL):
                matrix[i][j] = getCurrentStep(i,j)
        return matrix[-1][-1]